# VBS
import ROOT
import sys, os
import numpy as np
import math
from importlib import import_module
import itertools
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import PhysicsTools.NanoAODTools.postprocessing.tools as tk

ROOT.PyConfig.IgnoreCommandLineOptions = True


class VBSProducer(Module):
    def __init__(self, isMC, era, do_syst=False, syst_var=None):
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

        self.out.branch("lead_jet_eta{}".format(self.syst_suffix), "F")
        self.out.branch("lead_jet_phi{}".format(self.syst_suffix), "F")
        self.out.branch("trail_jet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("trail_jet_eta{}".format(self.syst_suffix), "F")
        self.out.branch("trail_jet_phi{}".format(self.syst_suffix), "F")
        self.out.branch("dijet_abs_dEta{}".format(self.syst_suffix), "F")
        self.out.branch("dijet_Mjj{}".format(self.syst_suffix), "F")
        self.out.branch("dijet_Zep{}".format(self.syst_suffix), "F")
        self.out.branch("dijet_centrality{}".format(self.syst_suffix), "F")
        self.out.branch("S_T_hard{}".format(self.syst_suffix), "F")
        self.out.branch("S_T_jets{}".format(self.syst_suffix), "F")
        self.out.branch("S_T_all{}".format(self.syst_suffix), "F")

        self.out.branch("x_Z{}".format(self.syst_suffix), "F")
        self.out.branch("x_jet20{}".format(self.syst_suffix), "F")
        self.out.branch("x_jet30{}".format(self.syst_suffix), "F")
        self.out.branch("x_MET{}".format(self.syst_suffix), "F")
        self.out.branch("H_T{}".format(self.syst_suffix), "F")
        self.out.branch("HT_F{}".format(self.syst_suffix), "F")
        self.out.branch("Jet_pt_Ratio{}".format(self.syst_suffix), "F")
        self.out.branch("R_pt{}".format(self.syst_suffix), "F")
        self.out.branch("Jet_etas_multiplied{}".format(self.syst_suffix), "F")    
        self.out.branch("dPT_OZ{}".format(self.syst_suffix), "F")
        self.out.branch("CJV_Pt{}".format(self.syst_suffix), "F")
        self.out.branch("CJV_Pt_Sum{}".format(self.syst_suffix), "F")
        self.out.branch("deltaPhiClosestJetMet{}".format(self.syst_suffix), "F")
        self.out.branch("deltaPhiFarthestJetMet{}".format(self.syst_suffix), "F")
        self.out.branch("etaThirdJet{}".format(self.syst_suffix), "F")

        self.out.branch("Z_pt_bst{}".format(self.syst_suffix), "F")
        self.out.branch("Z_phi_bst{}".format(self.syst_suffix), "F")
        self.out.branch("met_pt_bst{}".format(self.syst_suffix), "F")
        self.out.branch("met_phi_bst{}".format(self.syst_suffix), "F")
        self.out.branch("emulatedMET_pt_bst{}".format(self.syst_suffix), "F")
        self.out.branch("emulatedMET_phi_bst{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_ZMet_bst{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_ll_bst{}".format(self.syst_suffix), "F")
        self.out.branch("delta_eta_ll_bst{}".format(self.syst_suffix), "F")


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


    def analyze(self, event):
        """
        process event, return True (go to next module)
        or False (fail, go to next event)
        """

        # skip useless events
        if event.lep_category <= 0:
            return False

        # Get collection from event tree
        electrons = list(Collection(event, "Electron"))
        muons = list(Collection(event, "Muon"))
        jets = list(Collection(event, "Jet"))

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

        # Get variables from event tree
        Z_pt = event.Z_pt
        Z_eta = event.Z_eta
        Z_phi = event.Z_phi
        Z_mass = event.Z_mass
        Z_p4 = ROOT.TLorentzVector()
        Z_p4.SetPtEtaPhiM(Z_pt, Z_eta, Z_phi, Z_mass)
        Z_p4_bst = ROOT.TLorentzVector(Z_p4)

        met_pt = event.met_pt
        met_phi = event.met_phi
        met_p4 = ROOT.TLorentzVector()
        met_p4.SetPtEtaPhiM(met_pt, 0., met_phi, 0.)
        met_p4_bst = ROOT.TLorentzVector(met_p4)

        emulatedMET_pt_bst = event.emulatedMET
        emulatedMET_phi = event.emulatedMET_phi
        emulatedMET_p4 = ROOT.TLorentzVector()
        emulatedMET_p4.SetPtEtaPhiM(emulatedMET_pt_bst, 0., emulatedMET_phi, 0.)
        emulatedMET_p4_bst = ROOT.TLorentzVector(emulatedMET_p4)

        # process leptons
        good_leptons = []
        good_muons = []
        good_electrons = []
        # Choose tight-quality e/mu for event categorization
        for idx, mu in enumerate(muons):
            isoLep   = mu.pfRelIso04_all
            pass_ips = abs(mu.dxy) < 0.02 and abs(mu.dz) < 0.1
            pass_fid = abs(mu.eta) < 2.4 and mu.pt >= (25 if idx==0 else 20)
            pass_ids = mu.tightId and isoLep <= 0.15
            if pass_fid and pass_ids and pass_ips:
                good_muons.append(mu)
        for idy, el in enumerate(electrons):
            if el.pt >= (25 if idy==0 else 20) and abs(el.eta) <= 2.5 and self.electron_id(el, "90"):
                good_electrons.append(el)

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

        # sort the leptons in pt
        good_muons.sort(key=lambda x: x.pt, reverse=True)
        good_electrons.sort(key=lambda x: x.pt, reverse=True)
        good_leptons = good_electrons + good_muons
        good_leptons.sort(key=lambda x: x.pt, reverse=True)
        extra_leptons.sort(key=lambda x: x.pt, reverse=True)
        ngood_leptons = len(good_leptons)
        nextra_leptons = len(extra_leptons)
        if ngood_leptons!=event.ngood_leptons or nextra_leptons!=event.nextra_leptons:
            print('n good (extra) leptons: {} ({}) in VBSProducer, {} ({}) in MonoZProducer.'
                .format(ngood_leptons, nextra_leptons, event.ngood_leptons, event.nextra_leptons))
        lead_lep_p4 = good_leptons[0].p4() if ngood_leptons else ROOT.TLorentzVector(0., 0., 0., 0.)
        lead_lep_p4_bst = ROOT.TLorentzVector(lead_lep_p4)
        lead_lep_pt = good_leptons[0].pt if ngood_leptons else 0.
        trail_lep_p4 = good_leptons[1].p4() if ngood_leptons >= 2 else ROOT.TLorentzVector(0., 0., 0., 0.)
        trail_lep_p4_bst = ROOT.TLorentzVector(trail_lep_p4)
        trail_lep_pt = good_leptons[1].pt if ngood_leptons >= 2 else 0.

        # process jet
        good_jets  = []
        good_jets_p4 = ROOT.TLorentzVector(0., 0., 0., 0.)
        et_jets20 = 0.
        et_jets30 = 0.
        for jet in jets:
            if not jet.jetId:
                continue
            if tk.closest(jet, good_leptons)[1] < 0.4:
                continue
            if jet.pt <= 20 or abs(jet.eta) > 4.7:
                continue
            et_jets20 += jet.p4().Et()
            if jet.pt < 30.:
                continue
            et_jets30 += jet.p4().Et()
            good_jets.append(jet)
            good_jets_p4 += jet.p4()
        # sort the jets by pt
        good_jets.sort(key=lambda jet: jet.pt, reverse=True)
        ngood_jets = len(good_jets)
        if ngood_jets!=event.ngood_jets:
            print 'ngood_jets: {} in VBSProducer, {} in MonoZProducer'.format(ngood_jets, event.ngood_jets)
        lead_jet_p4 = good_jets[0].p4() if ngood_jets else ROOT.TLorentzVector(0., 0., 0., 0.)
        lead_jet_pt = good_jets[0].pt if ngood_jets else 0.
        lead_jet_phi = good_jets[0].phi if ngood_jets else 0.
        lead_jet_eta = good_jets[0].eta if ngood_jets else -99.
        trail_jet_p4 = good_jets[1].p4() if ngood_jets > 1 else ROOT.TLorentzVector(0., 0., 0., 0.)
        trail_jet_pt = good_jets[1].pt if ngood_jets > 1 else 0.
        trail_jet_phi = good_jets[1].phi if ngood_jets > 1 else 0.
        trail_jet_eta = good_jets[1].eta if ngood_jets > 1 else -99.

        # boosting 4 vectors
        boost_vet = good_jets_p4.BoostVector()
        lead_lep_p4_bst.Boost(boost_vet)
        trail_lep_p4_bst.Boost(boost_vet)
        Z_p4_bst.Boost(boost_vet)
        met_p4_bst.Boost(boost_vet)
        emulatedMET_p4_bst.Boost(boost_vet)

        # variables in bossted frame
        delta_eta_ll_bst = abs(lead_lep_p4_bst.Eta() - trail_lep_p4_bst.Eta())
        delta_phi_ll_bst = tk.deltaPhi(lead_lep_p4_bst.Phi(), trail_lep_p4_bst.Phi())
        delta_phi_ZMet_bst = tk.deltaPhi(Z_p4_bst.Phi(), met_p4_bst.Phi())

        # more variables
        x_denom20 = (et_jets20 + met_pt + Z_pt)
        x_denom30 = (et_jets30 + met_pt + Z_pt)
        x_Z = Z_pt / x_denom30 if x_denom30 > 0. else -99.
        x_jet20 = et_jets20 / x_denom20 if x_denom20 > 0. else -99. 
        x_jet30 = et_jets30 / x_denom30 if x_denom30 > 0. else -99.
        x_MET = met_pt / x_denom30 if x_denom30 > 0. else -99.
        H_T = sum([jet.pt for jet in good_jets])
        HT_F = (lead_jet_pt + trail_jet_pt) / H_T if H_T > 0. else 0.
        Jet_etas_multiplied = lead_jet_eta * trail_jet_eta

        # more variables
        if ngood_jets >= 2:
            S_T_jets = (lead_jet_p4+trail_jet_p4).Pt() / (lead_jet_pt+trail_jet_pt)
            S_T_hard = (lead_jet_p4+trail_jet_p4+Z_p4).Pt() / (lead_jet_pt+trail_jet_pt+Z_pt)
            S_T_all = (lead_jet_p4+trail_jet_p4+Z_p4+met_p4).Pt() / (lead_jet_pt+trail_jet_pt+Z_pt+met_pt)
            Jet_pt_Ratio = trail_jet_pt / lead_jet_pt
            R_pt = lead_lep_pt * trail_lep_pt / (lead_jet_pt * trail_jet_pt)
            dijet_abs_dEta = abs(lead_jet_eta-trail_jet_eta)
            dijet_Mjj = (lead_jet_p4 + trail_jet_p4).M()
            dijet_Zep = Z_eta - 0.5 * (lead_jet_eta + trail_jet_eta)
            dijet_centrality = np.exp(-4 * (dijet_Zep / dijet_abs_dEta)**2) if dijet_abs_dEta>0 else -99.
            # study jets between leading and trailing jets
            eta_range = sorted([lead_jet_eta, trail_jet_eta])
            pT_mid_Jets = [jet.pt for jet in good_jets[2:] if eta_range[0]<jet.eta<eta_range[1]]
            CJV_Pt = pT_mid_Jets[0] if len(pT_mid_Jets) else 0.
            CJV_Pt_Sum = sum(pT_mid_Jets) if len(pT_mid_Jets) else 0.
        else:
            S_T_jets = -99.
            S_T_hard = -99.
            S_T_all = -99.
            Jet_pt_Ratio = -99.
            R_pt = -99.
            dijet_abs_dEta = -99.
            dijet_Mjj = -99.
            dijet_Zep = -99.
            dijet_centrality = -99.
            CJV_Pt = 0.
            CJV_Pt_Sum = 0.

        # more variables
        dPT_OZ = (lead_jet_pt + trail_jet_pt) / Z_pt if Z_pt > 0. else -99.
        etaThirdJet = good_jets[2].eta if ngood_jets >= 3 else -99.
        deltaPhiClosestJetMet = 99.
        deltaPhiFarthestJetMet = -99.
        for jet in good_jets:
            if deltaPhiClosestJetMet > abs(tk.deltaPhi(jet.phi,met_phi)):
                deltaPhiClosestJetMet = abs(tk.deltaPhi(jet.phi,met_phi))
            if deltaPhiFarthestJetMet < abs(tk.deltaPhi(jet.phi,met_phi)):
                deltaPhiFarthestJetMet = abs(tk.deltaPhi(jet.phi,met_phi))

        self.out.fillBranch("lead_jet_eta{}".format(self.syst_suffix), lead_jet_eta)
        self.out.fillBranch("lead_jet_phi{}".format(self.syst_suffix), lead_jet_phi)
        self.out.fillBranch("trail_jet_pt{}".format(self.syst_suffix), trail_jet_pt)
        self.out.fillBranch("trail_jet_eta{}".format(self.syst_suffix), trail_jet_eta)
        self.out.fillBranch("trail_jet_phi{}".format(self.syst_suffix), trail_jet_phi)
        self.out.fillBranch("dijet_abs_dEta{}".format(self.syst_suffix), dijet_abs_dEta)
        self.out.fillBranch("dijet_Mjj{}".format(self.syst_suffix), dijet_Mjj)
        self.out.fillBranch("dijet_Zep{}".format(self.syst_suffix), dijet_Zep)
        self.out.fillBranch("dijet_centrality{}".format(self.syst_suffix), dijet_centrality)
        self.out.fillBranch("S_T_hard{}".format(self.syst_suffix), S_T_hard)
        self.out.fillBranch("S_T_jets{}".format(self.syst_suffix), S_T_jets)
        self.out.fillBranch("S_T_all{}".format(self.syst_suffix), S_T_all)

        self.out.fillBranch("x_Z{}".format(self.syst_suffix), x_Z)
        self.out.fillBranch("x_jet20{}".format(self.syst_suffix), x_jet20)
        self.out.fillBranch("x_jet30{}".format(self.syst_suffix), x_jet30)
        self.out.fillBranch("x_MET{}".format(self.syst_suffix), x_MET)
        self.out.fillBranch("H_T{}".format(self.syst_suffix), H_T)
        self.out.fillBranch("HT_F{}".format(self.syst_suffix), HT_F)
        self.out.fillBranch("Jet_pt_Ratio{}".format(self.syst_suffix), Jet_pt_Ratio)
        self.out.fillBranch("R_pt{}".format(self.syst_suffix), R_pt)
        self.out.fillBranch("Jet_etas_multiplied{}".format(self.syst_suffix), Jet_etas_multiplied)
        self.out.fillBranch("dPT_OZ{}".format(self.syst_suffix), dPT_OZ)
        self.out.fillBranch("CJV_Pt{}".format(self.syst_suffix), CJV_Pt)
        self.out.fillBranch("CJV_Pt_Sum{}".format(self.syst_suffix), CJV_Pt_Sum)
        self.out.fillBranch("deltaPhiClosestJetMet{}".format(self.syst_suffix), deltaPhiClosestJetMet)
        self.out.fillBranch("deltaPhiFarthestJetMet{}".format(self.syst_suffix), deltaPhiFarthestJetMet)
        self.out.fillBranch("etaThirdJet{}".format(self.syst_suffix), etaThirdJet)

        self.out.fillBranch("Z_pt_bst{}".format(self.syst_suffix), Z_p4_bst.Pt())
        self.out.fillBranch("Z_phi_bst{}".format(self.syst_suffix), Z_p4_bst.Phi())
        self.out.fillBranch("met_pt_bst{}".format(self.syst_suffix), met_p4_bst.Pt())
        self.out.fillBranch("met_phi_bst{}".format(self.syst_suffix), met_p4_bst.Phi())
        self.out.fillBranch("emulatedMET_pt_bst{}".format(self.syst_suffix), emulatedMET_p4_bst.Pt())
        self.out.fillBranch("emulatedMET_phi_bst{}".format(self.syst_suffix), emulatedMET_p4_bst.Phi())
        self.out.fillBranch("delta_phi_ll_bst{}".format(self.syst_suffix), delta_phi_ll_bst)
        self.out.fillBranch("delta_eta_ll_bst{}".format(self.syst_suffix), delta_eta_ll_bst)
        self.out.fillBranch("delta_phi_ZMet_bst{}".format(self.syst_suffix), delta_phi_ZMet_bst)

        return True

