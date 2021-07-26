import ROOT
import sys, os
import numpy as np
import scipy.linalg as la
import math
from importlib import import_module
import imp
import itertools
from copy import deepcopy
#from pyjet import cluster
#from pyjet.testdata import get_event
import pyjet
from numba import jit
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import PhysicsTools.NanoAODTools.postprocessing.tools as tk

ROOT.PyConfig.IgnoreCommandLineOptions = True

#local_path = ['/home/freerc/.local/lib/python2.7/site-packages/']
#def _get_module(name):
#    found = imp.find_module(name,local_path)
#    return imp.load_module(name,*found)
#pyjet = _get_module('pyjet')

class SUEPProducer(Module):
    def __init__(self, isMC, era, do_syst=False, syst_var=''):
        self.isMC = isMC
        self.era = era
        self.do_syst = do_syst
        self.syst_var = syst_var
        self.zmass = 91.1873
	if self.syst_var !='':
          self.syst_suffix = '_sys_' + self.syst_var if self.do_syst else ''
	else:
          self.syst_suffix = syst_var

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("met_pt{}".format(self.syst_suffix), "F")
        self.out.branch("met_phi{}".format(self.syst_suffix), "F")

        self.out.branch("nCleaned_Cands{}".format(self.syst_suffix), "I")
        self.out.branch("HTTot{}".format(self.syst_suffix), "F")
        self.out.branch("ave_cand_pt{}".format(self.syst_suffix), "F")
        self.out.branch("ngood_fastjets".format(self.syst_suffix), "I")

        self.out.branch("SUEP_ch_nconst{}".format(self.syst_suffix), "I")
        self.out.branch("SUEP_ch_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_ch_aplan{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_ch_FW2M{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_ch_D{}".format(self.syst_suffix), "F")

        self.out.branch("SUEP_pt_pt{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_m{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_eta{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_phi{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_nconst{}".format(self.syst_suffix), "I")
        self.out.branch("SUEP_pt_pt_ave{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_girth{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_aplan{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_FW2M{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_D{}".format(self.syst_suffix), "F")

        self.out.branch("SUEP_mult_pt{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_m{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_eta{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_phi{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_nconst{}".format(self.syst_suffix), "I")
        self.out.branch("SUEP_mult_pt_ave{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_girth{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_aplan{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_FW2M{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_D{}".format(self.syst_suffix), "F")

        self.out.branch("SUEP_dphi1_nconst{}".format(self.syst_suffix),"I")
        self.out.branch("SUEP_dphi1_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_dphi3_nconst{}".format(self.syst_suffix),"I")
        self.out.branch("SUEP_dphi3_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_dphi5_nconst{}".format(self.syst_suffix),"I")
        self.out.branch("SUEP_dphi5_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_dphi7_nconst{}".format(self.syst_suffix),"I")
        self.out.branch("SUEP_dphi7_spher{}".format(self.syst_suffix), "F")

        self.out.branch("met_filter{}".format(self.syst_suffix), "I")

        self.out.branch("HT{}".format(self.syst_suffix), "F")
        self.out.branch("ngood_jets{}".format(self.syst_suffix), "I")
        self.out.branch("ngood_bjets{}".format(self.syst_suffix), "I")
        self.out.branch("lead_jet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("lead_bjet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_j_met{}".format(self.syst_suffix), "F")

        self.out.branch("nhad_taus{}".format(self.syst_suffix), "I")
        self.out.branch("lead_tau_pt{}".format(self.syst_suffix), "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def btag_id(self, wp):
        # ref : https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
        if (self.era == "2016" and wp == "loose"):
            return 0.2219
        elif (self.era == "2016" and wp == "medium"):
            return 0.6324
        elif (self.era == "2016" and wp == "tight"):
            return 0.8958
        elif (self.era == "2017" and wp == "loose"):
            return 0.1522
        elif (self.era == "2017" and wp == "medium"):
            return 0.4941
        elif (self.era == "2017" and wp == "tight"):
            return 0.8001
        elif (self.era == "2018" and wp == "loose"):
            return 0.1241
        elif (self.era == "2018" and wp == "medium"):
            return 0.4184
        elif (self.era == "2018" and wp == "tight"):
            return 0.7527

    def met_filter(self, flag, filter_mask=True):
        return filter_mask and (
              (flag.HBHENoiseFilter)
           and (flag.HBHENoiseIsoFilter)
           and (flag.EcalDeadCellTriggerPrimitiveFilter)
           and (flag.goodVertices)
           and (flag.eeBadScFilter)
           and (flag.globalTightHalo2016Filter)
           and (flag.BadChargedCandidateFilter)
           and (flag.BadPFMuonFilter)
        )

    @jit #Use Numba for this function
    def sphericity(self, vector_list, r):
        pxx = pyy = pzz = pxy = pxz = pyz = p_sum = 0.0
        for vector in vector_list:
            P = np.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
            p_sum += P**(r)
            p_i = P**(r-2.0)
            pxx += (vector[0]*vector[0]) / p_i
            pyy += (vector[1]*vector[1]) / p_i
            pzz += (vector[2]*vector[2]) / p_i
            pxy += (vector[0]*vector[1]) / p_i
            pxz += (vector[0]*vector[2]) / p_i
            pyz += (vector[1]*vector[2]) / p_i
        Spher_Mat = np.array([[pxx,pxy,pxz],[pxy,pyy,pyz],[pxz,pyz,pzz]]) / p_sum
        evals = la.eigvalsh(Spher_Mat)
        return evals

    def analyze(self, event):
        """
        process event, return True (go to next module)
        or False (fail, go to next event)
        """
        jets = list(Collection(event, "Jet"))
        fatjets = list(Collection(event, "FatJet"))
        taus = list(Collection(event, "Tau"))
        PFCands = list(Collection(event, "PFCands"))
        flag = Object(event, "Flag")
        met = Object(event, "MET")
        genpart = list(Collection(event, "GenPart"))

        met_p4 = ROOT.TLorentzVector()
        met_p4.SetPtEtaPhiM(met.pt,0.0,met.phi, 0.0)

            
        # filling and contructing the event categorisation
        self.out.fillBranch("met_pt{}".format(self.syst_suffix), met.pt)
        self.out.fillBranch("met_phi{}".format(self.syst_suffix), met.phi)

        pass_met_filter = self.met_filter(flag, True)
        self.out.fillBranch("met_filter{}".format(self.syst_suffix), pass_met_filter)
 
        #look through all the PFCands. See here (https://github.com/SUEPPhysics/SUEPNano/blob/autumn18/python/addPFCands_cff.py)
        good_cands   = []
        fastjet_list = []
        sum_cand_pt = 0.0
        for cand in PFCands:
             if cand.trkPt < 1 or cand.fromPV < 2 or cand.trkEta > 2.5:
                 continue
             good_cands.append(cand)
             sum_cand_pt += cand.trkPt
             fastjet_prep = (cand.trkPt,cand.trkEta ,cand.trkPhi ,cand.mass)
             fastjet_list.append(fastjet_prep)
        nCands = len(good_cands)
        ave_cand_pt = sum_cand_pt / nCands if nCands >= 1 else 0.0 

        #fill out the basics
        self.out.fillBranch("nCleaned_Cands{}".format(self.syst_suffix), nCands)
        self.out.fillBranch("HTTot{}".format(self.syst_suffix), sum_cand_pt)
        self.out.fillBranch("ave_cand_pt{}".format(self.syst_suffix), ave_cand_pt)

        #make new jet collection based on fastjet
        fastjet_in = np.array(fastjet_list[:], dtype=[('pT', 'f8'), ('eta', 'f8'), ('phi', 'f8'), ('mass', 'f8')])
        sequence = pyjet.cluster(fastjet_in, R=1.5, p=-1) #p=-1,0,1 for anti-kt, aachen, and kt respectively
        fastjets = sequence.inclusive_jets(ptmin=3)
        self.out.fillBranch("ngood_fastjets".format(self.syst_suffix), len(fastjets))

        #remove the 10 hardest tracks for SUEP_isr
        #fastjets.sort(key=lambda fastjet: len(fastjet), reverse=True)
        spher_tmp = ROOT.TLorentzVector()
        if len(fastjets)>1:
            SUEP_cand = fastjets[0]
            ISR_cand = fastjets[1]
            if len(fastjets[1]) > len(fastjets[0]):
                SUEP_cand = fastjets[1]
                ISR_cand = fastjets[0]

            SUEP_pt = ROOT.TLorentzVector()
            SUEP_pt.SetPtEtaPhiM(SUEP_cand.pt, SUEP_cand.eta, SUEP_cand.phi, SUEP_cand.mass)
            boost_pt = SUEP_pt.BoostVector()
            boosted_cands = []
            for cands in good_cands:
                 spher_tmp.SetPtEtaPhiM(cands.trkPt, cands.trkEta, cands.trkPhi, cands.mass)
                 spher_tmp.Boost(-boost_pt)
                 if abs(tk.deltaPhi(spher_tmp.Phi(),ISR_cand.phi)) < 1.6: continue
                 boosted_cands.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
            try:
                sorted_evals = self.sphericity(boosted_cands,2.0)
            except:
                sorted_evals = [0.0, 0.0, 0.0]
            SUEP_ch_spher = 1.5 * (sorted_evals[1]+sorted_evals[0])
            SUEP_ch_aplan = 1.5 * sorted_evals[0]
            SUEP_ch_FW2M  = 1.0 - 3.0 * (sorted_evals[2]*sorted_evals[1] + sorted_evals[2]*sorted_evals[0] + sorted_evals[1]*sorted_evals[0])
            SUEP_ch_D     = 27.0 * sorted_evals[2]*sorted_evals[1]*sorted_evals[0]
            self.out.fillBranch("SUEP_ch_nconst{}".format(self.syst_suffix), len(boosted_cands))
            self.out.fillBranch("SUEP_ch_spher{}".format(self.syst_suffix), SUEP_ch_spher)
            self.out.fillBranch("SUEP_ch_aplan{}".format(self.syst_suffix), SUEP_ch_aplan)
            self.out.fillBranch("SUEP_ch_FW2M{}".format(self.syst_suffix), SUEP_ch_FW2M)
            self.out.fillBranch("SUEP_ch_D{}".format(self.syst_suffix), SUEP_ch_D)     






        if len(fastjets)>0:  
            #looking at the highest pT fastjet for SUEP_pt
            self.out.fillBranch("SUEP_pt_pt{}".format(self.syst_suffix), fastjets[0].pt)
            self.out.fillBranch("SUEP_pt_m{}".format(self.syst_suffix), fastjets[0].mass)
            self.out.fillBranch("SUEP_pt_eta{}".format(self.syst_suffix), fastjets[0].eta)
            self.out.fillBranch("SUEP_pt_phi{}".format(self.syst_suffix), fastjets[0].phi)
            self.out.fillBranch("SUEP_pt_nconst{}".format(self.syst_suffix), len(fastjets[0]))
            sum_SUEP_pt = 0.0
            girth_pt = 0.0
            SUEP_pt = ROOT.TLorentzVector()
            SUEP_pt.SetPtEtaPhiM(fastjets[0].pt, fastjets[0].eta, fastjets[0].phi, fastjets[0].mass)
            boost_pt = SUEP_pt.BoostVector()
            spher_pt = []
            for const in fastjets[0]:
                sum_SUEP_pt += const.pt
                dR = abs(tk.deltaR(const.eta, const.phi, fastjets[0].eta, fastjets[0].phi,))
                girth_pt += dR * const.pt / fastjets[0].pt
                spher_tmp.SetPtEtaPhiM(const.pt, const.eta, const.phi, const.mass)
                spher_tmp.Boost(-boost_pt)
                spher_pt.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
            try:
                sorted_evals = self.sphericity(spher_pt,2.0)
            except:
                sorted_evals = [0.0, 0.0, 0.0]
            SUEP_pt_spher = 1.5 * (sorted_evals[1]+sorted_evals[0])
            SUEP_pt_aplan = 1.5 * sorted_evals[0]
            SUEP_pt_FW2M  = 1.0 - 3.0 * (sorted_evals[2]*sorted_evals[1] + sorted_evals[2]*sorted_evals[0] + sorted_evals[1]*sorted_evals[0])
            SUEP_pt_D     = 27.0 * sorted_evals[2]*sorted_evals[1]*sorted_evals[0]
            self.out.fillBranch("SUEP_pt_pt_ave{}".format(self.syst_suffix), sum_SUEP_pt / len(fastjets[0]))
            self.out.fillBranch("SUEP_pt_girth{}".format(self.syst_suffix), girth_pt)
            self.out.fillBranch("SUEP_pt_spher{}".format(self.syst_suffix), SUEP_pt_spher)
            self.out.fillBranch("SUEP_pt_aplan{}".format(self.syst_suffix), SUEP_pt_aplan)
            self.out.fillBranch("SUEP_pt_FW2M{}".format(self.syst_suffix), SUEP_pt_FW2M)
            self.out.fillBranch("SUEP_pt_D{}".format(self.syst_suffix), SUEP_pt_D)
  
            nconst_dphi1 = nconst_dphi3 = nconst_dphi5 = nconst_dphi7 = 0
            if len(fastjets)>1:
                if len(fastjets[0]) > len(fastjets[1]):
                   SUEP_dphi_cand = fastjets[0]
                   ISR_dphi_cand = fastjets[1]
                else:
                   SUEP_dphi_cand = fastjets[1]
                   ISR_dphi_cand = fastjets[0]


                SUEP_dphi_vector = ROOT.TLorentzVector()
                SUEP_dphi_vector.SetPtEtaPhiM(SUEP_dphi_cand.pt, SUEP_dphi_cand.eta, SUEP_dphi_cand.phi, SUEP_dphi_cand.mass)
                boost_dphi = SUEP_dphi_vector.BoostVector()
                spher_dphi1 = []
                spher_dphi3 = []
                spher_dphi5 = []
                spher_dphi7 = []
                for const in SUEP_dphi_cand:
                    #dphi = abs(tk.deltaPhi(const.phi, ISR_dphi_cand.phi))
                    spher_tmp.SetPtEtaPhiM(const.pt, const.eta, const.phi, const.mass)
                    spher_tmp.Boost(-boost_dphi)
                    dphi = abs(tk.deltaPhi(spher_tmp.Phi(), ISR_dphi_cand.phi))
                    if dphi < 0.1:
                       continue
                    nconst_dphi1 += 1
                    spher_dphi1.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
                    if dphi < 0.3:
                       continue
                    nconst_dphi3 += 1
                    spher_dphi3.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
                    if dphi < 0.5:
                       continue
                    nconst_dphi5 += 1
                    spher_dphi5.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
                    if dphi < 0.7:
                       continue
                    nconst_dphi7 += 1
                    spher_dphi7.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
            try:
                sorted_dphi1 = self.sphericity(spher_dphi1,2.0)
                sorted_dphi3 = self.sphericity(spher_dphi3,2.0)
                sorted_dphi5 = self.sphericity(spher_dphi5,2.0)
                sorted_dphi7 = self.sphericity(spher_dphi7,2.0)
            except:
                sorted_dphi1 = [0.0, 0.0, 0.0]
                sorted_dphi3 = [0.0, 0.0, 0.0]
                sorted_dphi5 = [0.0, 0.0, 0.0]
                sorted_dphi7 = [0.0, 0.0, 0.0]
            SUEP_dphi1_spher = 1.5 * (sorted_dphi1[1]+sorted_dphi1[0])
            SUEP_dphi3_spher = 1.5 * (sorted_dphi3[1]+sorted_dphi3[0])
            SUEP_dphi5_spher = 1.5 * (sorted_dphi5[1]+sorted_dphi5[0])
            SUEP_dphi7_spher = 1.5 * (sorted_dphi7[1]+sorted_dphi7[0])

            self.out.fillBranch("SUEP_dphi1_nconst{}".format(self.syst_suffix), nconst_dphi1)
            self.out.fillBranch("SUEP_dphi1_spher{}".format(self.syst_suffix), SUEP_dphi1_spher)
            self.out.fillBranch("SUEP_dphi3_nconst{}".format(self.syst_suffix), nconst_dphi3)
            self.out.fillBranch("SUEP_dphi3_spher{}".format(self.syst_suffix), SUEP_dphi3_spher)
            self.out.fillBranch("SUEP_dphi5_nconst{}".format(self.syst_suffix), nconst_dphi5)
            self.out.fillBranch("SUEP_dphi5_spher{}".format(self.syst_suffix), SUEP_dphi5_spher)
            self.out.fillBranch("SUEP_dphi7_nconst{}".format(self.syst_suffix), nconst_dphi7)
            self.out.fillBranch("SUEP_dphi7_spher{}".format(self.syst_suffix), SUEP_dphi7_spher)

            #look at the fastjet with the most constituents for SUEP_mult
            fastjets.sort(key=lambda fastjet: len(fastjet), reverse=True)
            self.out.fillBranch("SUEP_mult_pt{}".format(self.syst_suffix), fastjets[0].pt)
            self.out.fillBranch("SUEP_mult_m{}".format(self.syst_suffix), fastjets[0].mass)
            self.out.fillBranch("SUEP_mult_eta{}".format(self.syst_suffix), fastjets[0].eta)
            self.out.fillBranch("SUEP_mult_phi{}".format(self.syst_suffix), fastjets[0].phi)
            self.out.fillBranch("SUEP_mult_nconst{}".format(self.syst_suffix), len(fastjets[0]))
            sum_SUEP_mult = 0.0
            girth_mult = 0.0
            SUEP_mult = ROOT.TLorentzVector()
            SUEP_mult.SetPtEtaPhiM(fastjets[0].pt, fastjets[0].eta, fastjets[0].phi, fastjets[0].mass)
            boost_mult = SUEP_mult.BoostVector()
            spher_mult = []
            unboost = []
            #for const in fastjets[0]:
            #    print(const.eta, const.phi, const.pt)
            #print("now for boosted")
            for const in fastjets[0]:
                sum_SUEP_mult += const.pt
                dR = abs(tk.deltaR(const.eta, const.phi, fastjets[0].eta, fastjets[0].phi,))
                girth_mult += dR * const.pt / fastjets[0].pt
                spher_tmp.SetPtEtaPhiM(const.pt, const.eta, const.phi, const.mass)
                unboost.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
                spher_tmp.Boost(-boost_mult)
                #print(spher_tmp.Eta(), spher_tmp.Phi(), spher_tmp.Pt())
                spher_mult.append([spher_tmp.Px(),spher_tmp.Py(),spher_tmp.Pz()])
            try:
                sorted_evals = self.sphericity(unboost,2.0)
            except:
                sorted_evals = [0.0, 0.0, 0.0]
            #print(sorted_evals)
            try:
                sorted_evals = self.sphericity(spher_mult,2.0)
            except:
                sorted_evals = [0.0, 0.0, 0.0]
            #print(sorted_evals)
            SUEP_mult_spher = 1.5 * (sorted_evals[1]+sorted_evals[0])
            SUEP_mult_aplan = 1.5 * sorted_evals[0]
            SUEP_mult_FW2M  = 1.0 - 3.0 * (sorted_evals[2]*sorted_evals[1] + sorted_evals[2]*sorted_evals[0] + sorted_evals[1]*sorted_evals[0])
            SUEP_mult_D     = 27.0 * sorted_evals[2]*sorted_evals[1]*sorted_evals[0]
            self.out.fillBranch("SUEP_mult_pt_ave{}".format(self.syst_suffix), sum_SUEP_mult / len(fastjets[0]))
            self.out.fillBranch("SUEP_mult_girth{}".format(self.syst_suffix), girth_mult)
            self.out.fillBranch("SUEP_mult_spher{}".format(self.syst_suffix), SUEP_mult_spher)
            self.out.fillBranch("SUEP_mult_aplan{}".format(self.syst_suffix), SUEP_mult_aplan)
            self.out.fillBranch("SUEP_mult_FW2M{}".format(self.syst_suffix), SUEP_mult_FW2M)
            self.out.fillBranch("SUEP_mult_D{}".format(self.syst_suffix), SUEP_mult_D)

        good_jets  = []
        good_bjets = []
        HT = 0.0
        for jet in jets:
            if jet.pt < 30.0 or abs(jet.eta) > 4.7:
                continue
            if not jet.jetId:
                continue
            #if tk.closest(jet, good_leptons)[1] < 0.4:
            #    continue
            good_jets.append(jet)
            HT += jet.pt
            # Count b-tag with medium WP DeepCSV
            # ref : https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            if abs(jet.eta) <= 2.4 and jet.btagDeepB > self.btag_id("medium"):
                good_bjets.append(jet)

        good_jets.sort(key=lambda jet: jet.pt, reverse=True)
        good_bjets.sort(key=lambda jet: jet.pt, reverse=True)

        _dphi_j_met = tk.deltaPhi(good_jets[0], met.phi) if len(good_jets) else -99.0
        _lead_jet_pt = good_jets[0].pt if len(good_jets) else 0.0
        _lead_bjet_pt = good_bjets[0].pt if len(good_bjets) else 0.0
        
        self.out.fillBranch("HT{}".format(self.syst_suffix), HT)
        self.out.fillBranch("ngood_jets{}".format(self.syst_suffix), len(good_jets))
        self.out.fillBranch("ngood_bjets{}".format(self.syst_suffix), len(good_bjets))
        self.out.fillBranch("lead_jet_pt{}".format(self.syst_suffix), _lead_jet_pt)
        self.out.fillBranch("lead_bjet_pt{}".format(self.syst_suffix), _lead_bjet_pt)
        self.out.fillBranch("delta_phi_j_met{}".format(self.syst_suffix), _dphi_j_met)

        # process taus
        had_taus = []
        for tau in taus:
            #if tk.closest(tau, good_leptons)[1] < 0.4:
            #    continue
            # only hadronic tau decay
            if tau.decayMode != 5:
                continue
            if tau.pt > 18 and abs(tau.eta) <= 2.3:
                had_taus.append(tau)
        self.out.fillBranch("nhad_taus{}".format(self.syst_suffix), len(had_taus))
        self.out.fillBranch("lead_tau_pt{}".format(self.syst_suffix), had_taus[0].pt if len(had_taus) else 0)
        

        # This will reduce the size of most of the background and data
        if (len(fastjets)>0):
            return True
        else:
            return False

