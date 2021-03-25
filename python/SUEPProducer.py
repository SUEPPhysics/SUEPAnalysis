import ROOT
import sys, os
import numpy as np
import math
from importlib import import_module
import itertools
from copy import deepcopy
from pyjet import cluster
from pyjet.testdata import get_event
from root_numpy import stretch
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import PhysicsTools.NanoAODTools.postprocessing.tools as tk

ROOT.PyConfig.IgnoreCommandLineOptions = True


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
        self.out.branch("ngood_leptons{}".format(self.syst_suffix), "I")
        self.out.branch("nextra_leptons{}".format(self.syst_suffix), "I")

        self.out.branch("nCleaned_Cands{}".format(self.syst_suffix), "I")
        self.out.branch("HTTot{}".format(self.syst_suffix), "F")
        self.out.branch("ave_cand_pt{}".format(self.syst_suffix), "F")
        self.out.branch("ngood_fastjets".format(self.syst_suffix), "I")

        self.out.branch("SUEP_isr_pt{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_isr_m{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_isr_eta{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_isr_phi{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_isr_nconst{}".format(self.syst_suffix), "I")
        #self.out.branch("SUEP_isr_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_isr_pt_ave{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_isr_girth{}".format(self.syst_suffix), "F")

        self.out.branch("SUEP_pt_pt{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_m{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_eta{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_phi{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_nconst{}".format(self.syst_suffix), "I")
        #self.out.branch("SUEP_pt_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_pt_ave{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_pt_girth{}".format(self.syst_suffix), "F")

        self.out.branch("SUEP_mult_pt{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_m{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_eta{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_phi{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_nconst{}".format(self.syst_suffix), "I")
        #self.out.branch("SUEP_mult_spher{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_pt_ave{}".format(self.syst_suffix), "F")
        self.out.branch("SUEP_mult_girth{}".format(self.syst_suffix), "F")

        self.out.branch("ngood_fatjets{}".format(self.syst_suffix), "I")
        #self.out.branch("SUEP_pt_pt{}".format(self.syst_suffix), "F")
        #self.out.branch("SUEP_pt_eta{}".format(self.syst_suffix), "F")
        #self.out.branch("SUEP_pt_phi{}".format(self.syst_suffix), "F")
        #self.out.branch("SUEP_pt_m{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_fatjet_met{}".format(self.syst_suffix), "F")

        self.out.branch("leading_lep_pt{}".format(self.syst_suffix), "F")
        self.out.branch("leading_lep_eta{}".format(self.syst_suffix), "F")
        self.out.branch("trailing_lep_pt{}".format(self.syst_suffix), "F")
        self.out.branch("trailing_lep_eta{}".format(self.syst_suffix), "F")
        self.out.branch("leading_lep_flavor{}".format(self.syst_suffix), "I")

        self.out.branch("met_filter{}".format(self.syst_suffix), "I")

        self.out.branch("ngood_jets{}".format(self.syst_suffix), "I")
        self.out.branch("ngood_bjets{}".format(self.syst_suffix), "I")
        self.out.branch("lead_jet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("lead_bjet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_j_met{}".format(self.syst_suffix), "F")

        self.out.branch("nhad_taus{}".format(self.syst_suffix), "I")
        self.out.branch("lead_tau_pt{}".format(self.syst_suffix), "F")

        if self.isMC and len(self.syst_suffix)==0:
            self.out.branch("w_muon_SF{}".format(self.syst_suffix), "F")
            self.out.branch("w_muon_SFUp{}".format(self.syst_suffix), "F")
            self.out.branch("w_muon_SFDown{}".format(self.syst_suffix), "F")
            self.out.branch("w_electron_SF{}".format(self.syst_suffix), "F")
            self.out.branch("w_electron_SFUp{}".format(self.syst_suffix), "F")
            self.out.branch("w_electron_SFDown{}".format(self.syst_suffix), "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def electron_id(self, electron, wp):
        pass_id = 0
        if (self.era == "2016" and wp == "80"):
            return electron.mvaSpring16GP_WP80
        elif (self.era == "2016" and wp == "90"):
            return electron.mvaSpring16GP_WP90

        elif (self.era == "2017" and wp == "80"):
            try:
                pass_id = electron.mvaFall17V2Iso_WP80
            except:
                try:
                    pass_id = electron.mvaFall17V1Iso_WP80
                except:
                    try:
                        pass_id = electron.mvaFall17Iso_WP80
                    except ValueError:
                        print "[error] not mvaFall17 electron id found ... "

            return pass_id
        elif (self.era == "2017" and wp == "90"):
            try:
                pass_id = electron.mvaFall17V2Iso_WP90
            except:
                try:
                    pass_id = electron.mvaFall17V1Iso_WP90
                except:
                    try:
                        pass_id = electron.mvaFall17Iso_WP90
                    except ValueError:
                        print "[error] not mvaFall17 electron id found ... "

            return pass_id
        elif (self.era == "2017" and wp == "WPL"):
            try:
                pass_id = electron.mvaFall17V2Iso_WPL
            except:
                try:
                    pass_id = electron.mvaFall17V1Iso_WPL
                except:
                    try:
                        pass_id = electron.mvaFall17Iso_WPL
                    except ValueError:
                        print "[error] not mvaFall17 electron id found ... "

        elif (self.era == "2018" and wp == "80"):
            try:
                pass_id = electron.mvaFall17V2Iso_WP80
            except:
                try:
                    pass_id = electron.mvaFall17V1Iso_WP80
                except:
                    try:
                        pass_id = electron.mvaFall17Iso_WP80
                    except ValueError:
                        print "[error] not mvaFall17 electron id found ... "

            return pass_id
        elif (self.era == "2018" and wp == "90"):
            try:
                pass_id = electron.mvaFall17V2Iso_WP90
            except:
                try:
                    pass_id = electron.mvaFall17V1Iso_WP90
                except:
                    try:
                        pass_id = electron.mvaFall17Iso_WP90
                    except ValueError:
                        print "[error] not mvaFall17 electron id found ... "

            return pass_id
        elif (self.era == "2018" and wp == "WPL"):
            try:
                pass_id = electron.mvaFall17V2Iso_WPL
            except:
                try:
                    pass_id = electron.mvaFall17V1Iso_WPL
                except:
                    try:
                        pass_id = electron.mvaFall17Iso_WPL
                    except ValueError:
                        print "[error] not mvaFall18 electron id found ... "

            return pass_id


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


    def analyze(self, event):
        """
        process event, return True (go to next module)
        or False (fail, go to next event)
        """
        electrons = list(Collection(event, "Electron"))
        muons = list(Collection(event, "Muon"))
        jets = list(Collection(event, "Jet"))
        fatjets = list(Collection(event, "FatJet"))
        taus = list(Collection(event, "Tau"))
        PFCands = list(Collection(event, "PFCands"))
        flag = Object(event, "Flag")
        met = Object(event, "MET")

        # in case of systematic take the shifted values are default
        # For the central values, need to include jetMetTool all the time
        # Jet systematics
        if self.syst_var == "":
            syst_var = "nom"
        else:
            syst_var = self.syst_var
        # checking something
        try:
            var_jet_pts = getattr(event,  "Jet_pt_{}".format(syst_var), None)
            if var_jet_pts:
                for i,jet in enumerate(jets):
                    jet.pt = var_jet_pts[i]
            else:
                print 'WARNING: jet pts with variation {}'
                'not available, using the nominal value'.format(syst_var)
        except:
            var_jet_pts = getattr(event,  "Jet_pt_nom", None)
            for i,jet in enumerate(jets):
                jet.pt = var_jet_pts[i]

        try:
            var_met_pt  = getattr(event,  "MET_pt_{}".format(syst_var), None)
            var_met_phi = getattr(event, "MET_phi_{}".format(syst_var), None)
            if var_met_pt:
                met.pt = var_met_pt
            else:
                print 'WARNING: MET pt with variation '
                '{} not available, using the nominal value'.format(syst_var)
            if var_met_phi:
                met.phi = var_met_phi
            else:
                print 'WARNING: MET phi with variation {}'
                'not available, using the nominal value'.format(syst_var)
        except:
            var_met_pt  = getattr(event,  "MET_pt_nom", None)
            var_met_phi = getattr(event, "MET_phi_nom", None)
            if var_met_pt:
                met.pt = var_met_pt
            if var_met_phi:
                met.phi = var_met_phi

        met_p4 = ROOT.TLorentzVector()
        met_p4.SetPtEtaPhiM(met.pt,0.0,met.phi, 0.0)


        # Electrons Energy
        if "ElectronEn" in self.syst_var:
            (met_px, met_py) = ( met.pt*np.cos(met.phi), met.pt*np.sin(met.phi) )
            if "Up" in self.syst_var:
                for i, elec in enumerate(electrons):
                    met_px = met_px + (elec.energyErr)*np.cos(elec.phi)/math.cosh(elec.eta)
                    met_py = met_py + (elec.energyErr)*np.sin(elec.phi)/math.cosh(elec.eta)
                    elec.pt = elec.pt + elec.energyErr/math.cosh(elec.eta)
            else:
                for i, elec in enumerate(electrons):
                    met_px = met_px - (elec.energyErr)*np.cos(elec.phi)/math.cosh(elec.eta)
                    met_py = met_py - (elec.energyErr)*np.sin(elec.phi)/math.cosh(elec.eta)
                    elec.pt = elec.pt - elec.energyErr/math.cosh(elec.eta)
            met.pt  = math.sqrt(met_px**2 + met_py**2)
            met.phi = math.atan2(met_py, met_px)

        # Muons Energy
        if self.isMC:
            muons_pts = getattr(event, "Muon_corrected_pt")
            for i, muon in enumerate(muons):
                muon.pt = muons_pts[i]

        if "MuonEn" in self.syst_var:
            (met_px, met_py) = ( met.pt*np.cos(met.phi), met.pt*np.sin(met.phi) )
            if "Up" in self.syst_var:
                muons_pts = getattr(event, "Muon_correctedUp_pt")
                for i, muon in enumerate(muons):
                    met_px = met_px - (muons_pts[i] - muon.pt)*np.cos(muon.phi)
                    met_py = met_py - (muons_pts[i] - muon.pt)*np.sin(muon.phi)
                    muon.pt = muons_pts[i]
            else:
                muons_pts = getattr(event, "Muon_correctedDown_pt")
                for i, muon in enumerate(muons):
                    met_px =met_px - (muons_pts[i] - muon.pt)*np.cos(muon.phi)
                    met_py =met_py - (muons_pts[i] - muon.pt)*np.sin(muon.phi)
                    muon.pt = muons_pts[i]
            met.pt  = math.sqrt(met_px**2 + met_py**2)
            met.phi = math.atan2(met_py, met_px)
            
        # filling and contructing the event categorisation
        self.out.fillBranch("met_pt{}".format(self.syst_suffix), met.pt)
        self.out.fillBranch("met_phi{}".format(self.syst_suffix), met.phi)

        pass_met_filter = self.met_filter(flag, True)
        self.out.fillBranch("met_filter{}".format(self.syst_suffix), pass_met_filter)

        # count electrons and muons
        good_leptons = []
        good_muons = []
        good_electrons = []

	muons.sort(key=lambda muon: muon.pt, reverse=True)
        electrons.sort(key=lambda el: el.pt, reverse=True)
        # Choose tight-quality e/mu for event categorization
        for idx,mu in enumerate(muons):
            isoLep   = mu.pfRelIso04_all
            pass_ips = abs(mu.dxy) < 0.02 and abs(mu.dz) < 0.1
            pass_fid = abs(mu.eta) < 2.4 and mu.pt >= (25 if idx==0 else 20)
            pass_ids = mu.tightId and isoLep <= 0.15
            if pass_fid and pass_ids and pass_ips:
                good_muons.append(mu)
        for idy,el in enumerate(electrons):
            id_CB = el.cutBased
            # changing to MVA based ID :
            if el.pt >= (25 if idy==0 else 20) and abs(el.eta) <= 2.5 and self.electron_id(el, "90"):
                good_electrons.append(el)

        # let sort the muons in pt
        good_muons.sort(key=lambda x: x.pt, reverse=True)
        good_electrons.sort(key=lambda x: x.pt, reverse=True)

        # Find any remaining e/mu that pass looser selection
        extra_leptons = []
        for mu in muons:
            isoLep   = mu.pfRelIso04_all
            pass_ids = mu.softId and isoLep <= 0.25
            pass_fid = abs(mu.eta) < 2.4 and mu.pt >= 10
            if tk.closest(mu, good_muons)[1] < 0.01:
                continue
            if pass_fid and pass_ids:
                extra_leptons.append(mu)

        for el in electrons:
            pass_fid = abs(el.eta) < 2.5 and el.pt >= 10
            if tk.closest(el, good_electrons)[1] < 0.01:
                continue
            if pass_fid and self.electron_id(el, "WPL"):
                extra_leptons.append(el)


        good_leptons = good_electrons + good_muons
        good_leptons.sort(key=lambda x: x.pt, reverse=True)

        _lead_lep_pt = good_leptons[0].pt if len(good_leptons) else 0.0
        _lead_lep_eta = good_leptons[0].eta if len(good_leptons) else 0.0
        _trail_lep_pt = good_leptons[1].pt if len(good_leptons) >= 2 else 0.0
        _trail_lep_eta = good_leptons[1].eta if len(good_leptons) >= 2 else 0.0
	_leading_lep_flavor = 0
	if len(good_muons) and len(good_electrons):
		if good_muons[0].pt > good_electrons[0].pt: _leading_lep_flavor = 1

        self.out.fillBranch("leading_lep_pt{}".format(self.syst_suffix), _lead_lep_pt)
        self.out.fillBranch("leading_lep_eta{}".format(self.syst_suffix), _lead_lep_eta)
        self.out.fillBranch("trailing_lep_pt{}".format(self.syst_suffix), _trail_lep_pt)
        self.out.fillBranch("trailing_lep_eta{}".format(self.syst_suffix), _trail_lep_eta)
        self.out.fillBranch("leading_lep_flavor{}".format(self.syst_suffix), _leading_lep_flavor)

        ngood_leptons = len(good_leptons)
        nextra_leptons = len(extra_leptons)

        if False:
            print "number of leptons [all, good, extra]: ", ngood_leptons, " : ", nextra_leptons
            print "        CBId electrons : ", [e.cutBased for e in good_electrons]
            print "        WP90 electrons : ", [e.mvaFall17Iso_WP90 for e in good_electrons]
            print "             muons     : ", [e.tightId for e in good_muons]
            print "        lepton pts     : ", [e.pt for e in good_leptons]

        self.out.fillBranch("ngood_leptons{}".format(self.syst_suffix), ngood_leptons)
        self.out.fillBranch("nextra_leptons{}".format(self.syst_suffix), nextra_leptons)

        # Leptons efficiency/Trigger/Isolation Scale factors
        # These are applied only of the first 2 leading leptons
        if self.isMC:
            w_muon_SF     = w_electron_SF     = 1.0
            w_muon_SFUp   = w_electron_SFUp   = 1.0
            w_muon_SFDown = w_electron_SFDown = 1.0
            if ngood_leptons >= 2:
                if abs(good_leptons[0].pdgId) == 11:
                    w_electron_SF     *=  good_leptons[0].SF
                    w_electron_SFUp   *= (good_leptons[0].SF + good_leptons[0].SFErr)
                    w_electron_SFDown *= (good_leptons[0].SF - good_leptons[0].SFErr)
                if abs(good_leptons[0].pdgId) == 11:
                    w_electron_SF     *=  good_leptons[1].SF
                    w_electron_SFUp   *= (good_leptons[1].SF + good_leptons[1].SFErr)
                    w_electron_SFDown *= (good_leptons[1].SF - good_leptons[1].SFErr)
                if abs(good_leptons[0].pdgId) == 13:
                    w_muon_SF     *=  good_leptons[0].SF
                    w_muon_SFUp   *= (good_leptons[0].SF + good_leptons[0].SFErr)
                    w_muon_SFDown *= (good_leptons[0].SF - good_leptons[0].SFErr)
                if abs(good_leptons[1].pdgId) == 13:
                    w_muon_SF     *=  good_leptons[1].SF
                    w_muon_SFUp   *= (good_leptons[1].SF + good_leptons[1].SFErr)
                    w_muon_SFDown *= (good_leptons[1].SF - good_leptons[1].SFErr)
            self.out.fillBranch("w_muon_SF"        , w_muon_SF        )
            self.out.fillBranch("w_muon_SFUp"      , w_muon_SFUp      )
            self.out.fillBranch("w_muon_SFDown"    , w_muon_SFDown    )
            self.out.fillBranch("w_electron_SF"    , w_electron_SF    )
            self.out.fillBranch("w_electron_SFUp"  , w_electron_SFUp  )
            self.out.fillBranch("w_electron_SFDown", w_electron_SFDown)

        #look through all the PFCands. See here (https://github.com/SUEPPhysics/SUEPNano/blob/autumn18/python/addPFCands_cff.py)
        good_cands   = []
        fastjet_list = []
        sum_cand_pt = 0.0
        for cand in PFCands:
             if cand.trkPt < 1 or cand.fromPV >= 2 or cand.trkEta > 2.5:
                 continue
             good_cands.append(cand)
             sum_cand_pt += cand.trkPt
             fastjet_prep = (cand.trkPt,cand.trkEta ,cand.trkPhi ,cand.mass)
             fastjet_list.append(fastjet_prep)
        nCands = len(good_cands)
        ave_cand_pt = sum_cand_pt / nCands

        #make new jet collection based on fastjet
        fastjet_in = np.array(fastjet_list[:], dtype=[('pT', 'f8'), ('eta', 'f8'), ('phi', 'f8'), ('mass', 'f8')])
        sequence = cluster(fastjet_in, R=1.5, p=1) #p=-1,0,1 for anti-kt, aachen, and kt respectively
        fastjets = sequence.inclusive_jets(ptmin=3)

        #fill out the basics
        self.out.fillBranch("nCleaned_Cands{}".format(self.syst_suffix), nCands)
        self.out.fillBranch("HTTot{}".format(self.syst_suffix), sum_cand_pt)
        self.out.fillBranch("ave_cand_pt{}".format(self.syst_suffix), ave_cand_pt)
        self.out.fillBranch("ngood_fastjets".format(self.syst_suffix), len(fastjets))

        #remove the 10 hardest tracks for SUEP_isr
        good_cands.sort(key=lambda cand: cand.trkPt, reverse=True)
        i=0
        sum_SUEP = 0.0
        SUEP_isr = ROOT.TLorentzVector()
        tmp = ROOT.TLorentzVector()
        for cand in good_cands:
            if i < 9: continue
            i += 1
            sum_SUEP += cand.trkPt
            tmp.SetPtEtaPhiM(cand.trkPt,cand.trkEta ,cand.trkPhi ,cand.mass)
            SUEP_isr += tmp
        if nCands > 10:
            self.out.fillBranch("SUEP_isr_pt{}".format(self.syst_suffix), SUEP_isr.Pt())
            self.out.fillBranch("SUEP_isr_m{}".format(self.syst_suffix), SUEP_isr.M())
            self.out.fillBranch("SUEP_isr_eta{}".format(self.syst_suffix), SUEP_isr.Eta())
            self.out.fillBranch("SUEP_isr_phi{}".format(self.syst_suffix), SUEP_isr.Phi())
            self.out.fillBranch("SUEP_isr_nconst{}".format(self.syst_suffix), nCands - 10)
            self.out.fillBranch("SUEP_isr_pt_ave{}".format(self.syst_suffix), sum_SUEP/(nCands - 10))
        else:
            self.out.fillBranch("SUEP_isr_pt{}".format(self.syst_suffix), -99.0)
            self.out.fillBranch("SUEP_isr_m{}".format(self.syst_suffix), -99.0)
            self.out.fillBranch("SUEP_isr_eta{}".format(self.syst_suffix), -99.0)
            self.out.fillBranch("SUEP_isr_phi{}".format(self.syst_suffix), -99.0)
            self.out.fillBranch("SUEP_isr_nconst{}".format(self.syst_suffix), -1)
            self.out.fillBranch("SUEP_isr_pt_ave{}".format(self.syst_suffix), -99.0)
        i=0
        girth_isr = 0.0
        for cand in good_cands:
            if i < 9: continue
            i += 1
            dR = abs(tk.deltaR(cand.trkEta, cand.trkPhi, SUEP_isr.Eta(), SUEP_isr.Phi(),))
            girth_isr += dR * cand.trkPt / SUEP_isr.Pt()
        if nCands > 10:
            self.out.fillBranch("SUEP_isr_girth{}".format(self.syst_suffix), girth_isr)
        else:
            self.out.fillBranch("SUEP_isr_girth{}".format(self.syst_suffix), -99.0)

        if len(fastjets)>0:  
            #looking at the highest pT fastjet for SUEP_pt
            self.out.fillBranch("SUEP_pt_pt{}".format(self.syst_suffix), fastjets[0].pt)
            self.out.fillBranch("SUEP_pt_m{}".format(self.syst_suffix), fastjets[0].mass)
            self.out.fillBranch("SUEP_pt_eta{}".format(self.syst_suffix), fastjets[0].eta)
            self.out.fillBranch("SUEP_pt_phi{}".format(self.syst_suffix), fastjets[0].phi)
            self.out.fillBranch("SUEP_pt_nconst{}".format(self.syst_suffix), len(fastjets[0]))
            sum_SUEP_pt = 0.0
            girth_pt = 0.0
            for const in fastjets[0]:
                sum_SUEP_pt += const.pt
                dR = abs(tk.deltaR(const.eta, const.phi, fastjets[0].eta, fastjets[0].phi,))
                girth_pt += dR * const.pt / fastjets[0].pt
            self.out.fillBranch("SUEP_pt_pt_ave{}".format(self.syst_suffix), sum_SUEP_pt / len(fastjets[0]))
            self.out.fillBranch("SUEP_pt_girth{}".format(self.syst_suffix), girth_pt)

            #look at the fastjet with the most constituents for SUEP_mult
            fastjets.sort(key=lambda fastjet: len(fastjet), reverse=True)
            self.out.fillBranch("SUEP_mult_pt{}".format(self.syst_suffix), fastjets[0].pt)
            self.out.fillBranch("SUEP_mult_m{}".format(self.syst_suffix), fastjets[0].mass)
            self.out.fillBranch("SUEP_mult_eta{}".format(self.syst_suffix), fastjets[0].eta)
            self.out.fillBranch("SUEP_mult_phi{}".format(self.syst_suffix), fastjets[0].phi)
            self.out.fillBranch("SUEP_mult_nconst{}".format(self.syst_suffix), len(fastjets[0]))
            sum_SUEP_mult = 0.0
            girth_mult = 0.0
            for const in fastjets[0]:
                sum_SUEP_mult += const.pt
                dR = abs(tk.deltaR(const.eta, const.phi, fastjets[0].eta, fastjets[0].phi,))
                girth_mult += dR * const.pt / fastjets[0].pt
            self.out.fillBranch("SUEP_mult_pt_ave{}".format(self.syst_suffix), sum_SUEP_mult / len(fastjets[0]))
            self.out.fillBranch("SUEP_mult_girth{}".format(self.syst_suffix), girth_mult)

        # process jet
        good_jets  = []
        good_bjets = []
        for jet in jets:
            if jet.pt < 30.0 or abs(jet.eta) > 4.7:
                continue
            if not jet.jetId:
                continue
            if tk.closest(jet, good_leptons)[1] < 0.4:
                continue
            good_jets.append(jet)
            # Count b-tag with medium WP DeepCSV
            # ref : https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            if abs(jet.eta) <= 2.4 and jet.btagDeepB > self.btag_id("medium"):
                good_bjets.append(jet)

        good_jets.sort(key=lambda jet: jet.pt, reverse=True)
        good_bjets.sort(key=lambda jet: jet.pt, reverse=True)

        _dphi_j_met = tk.deltaPhi(good_jets[0], met.phi) if len(good_jets) else -99.0
        _lead_jet_pt = good_jets[0].pt if len(good_jets) else 0.0
        _lead_bjet_pt = good_bjets[0].pt if len(good_bjets) else 0.0

        self.out.fillBranch("ngood_jets{}".format(self.syst_suffix), len(good_jets))
        self.out.fillBranch("ngood_bjets{}".format(self.syst_suffix), len(good_bjets))
        self.out.fillBranch("lead_jet_pt{}".format(self.syst_suffix), _lead_jet_pt)
        self.out.fillBranch("lead_bjet_pt{}".format(self.syst_suffix), _lead_bjet_pt)
        self.out.fillBranch("delta_phi_j_met{}".format(self.syst_suffix), _dphi_j_met)

        # process fatjet
        good_fatjets  = []
        for fatjet in fatjets:
            if fatjet.pt < 30.0 or abs(fatjet.eta) > 4.7:
                continue
            if not fatjet.jetId:
                continue
            if tk.closest(fatjet, good_leptons)[1] < 0.4:
                continue
            good_fatjets.append(fatjet)
        good_fatjets.sort(key=lambda fatjet: fatjet.pt, reverse=True)

        _dphi_fatjet_met = tk.deltaPhi(good_fatjets[0], met.phi) if len(good_fatjets) else -99.0

        self.out.fillBranch("ngood_fatjets{}".format(self.syst_suffix), len(good_fatjets))
        self.out.fillBranch("delta_phi_fatjet_met{}".format(self.syst_suffix), _dphi_fatjet_met)

        # process taus
        had_taus = []
        for tau in taus:
            if tk.closest(tau, good_leptons)[1] < 0.4:
                continue
            # only hadronic tau decay
            if tau.decayMode != 5:
                continue
            if tau.pt > 18 and abs(tau.eta) <= 2.3:
                had_taus.append(tau)
        self.out.fillBranch("nhad_taus{}".format(self.syst_suffix), len(had_taus))
        self.out.fillBranch("lead_tau_pt{}".format(self.syst_suffix), had_taus[0].pt if len(had_taus) else 0)

        # Let remove the negative categories with no obvious meaning meaning
        # This will reduce the size of most of the bacground and data
        if ("len(fastjets)>0"):
            return True
        else:
            return False

