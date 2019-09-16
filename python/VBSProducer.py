# VBS
import ROOT
import sys, os
import numpy as np
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

        self.out.branch( "lead_jet_eta{}".format(self.syst_suffix), "F" )
        self.out.branch( "trail_jet_pt{}".format(self.syst_suffix), "F" )
        self.out.branch( "trail_jet_eta{}".format(self.syst_suffix), "F" )
        self.out.branch( "dijet_abs_delta_eta{}".format(self.syst_suffix), "F" )
        self.out.branch( "dijet_Mjj{}".format(self.syst_suffix), "F" )
        self.out.branch( "dijet_Zep{}".format(self.syst_suffix), "F" )
        self.out.branch( "dijet_centrality_gg{}".format(self.syst_suffix), "F" )

        self.out.branch( "x_Z{}".format(self.syst_suffix), "F" )
        self.out.branch( "x_jet20{}".format(self.syst_suffix), "F" )
        self.out.branch( "x_jet30{}".format(self.syst_suffix), "F" )
        self.out.branch( "x_MET{}".format(self.syst_suffix), "F" )
        self.out.branch( "zeppenfeld{}".format(self.syst_suffix), "F" )
        self.out.branch( "H_T{}".format(self.syst_suffix), "F" )
        self.out.branch( "HT_F{}".format(self.syst_suffix), "F" )
        self.out.branch( "Jet_pt_Ratio{}".format(self.syst_suffix), "F" )
        self.out.branch( "R_pt{}".format(self.syst_suffix), "F" )
        self.out.branch( "Jet_etas_multiplied{}".format(self.syst_suffix), "F" )    
        self.out.branch( "dPT_OZ{}".format(self.syst_suffix), "F" )
        self.out.branch( "CJV_Pt{}".format(self.syst_suffix), "F" )
        self.out.branch( "CJV_Pt_Sum{}".format(self.syst_suffix), "F" )
        self.out.branch( "deltaPhiLeadingJetMet{}".format(self.syst_suffix), "F" )
        self.out.branch( "deltaPhiClosestJetMet{}".format(self.syst_suffix), "F" )
        self.out.branch( "deltaPhiFarthestJetMet{}".format(self.syst_suffix), "F" )
        self.out.branch( "etaThirdJet{}".format(self.syst_suffix), "F" )


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def electron_id(self, electron, wp):
        pass_id = 0
        if (self.era == "2016" and wp == "80" ):
            return electron.mvaSpring16GP_WP80
        elif (self.era == "2016" and wp == "90" ):
            return electron.mvaSpring16GP_WP90

        elif (self.era == "2017" and wp == "80" ):
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
        elif (self.era == "2017" and wp == "90" ):
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
        elif (self.era == "2017" and wp == "WPL" ):
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

        elif (self.era == "2018" and wp == "80" ):
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
        elif (self.era == "2018" and wp == "90" ):
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
        elif (self.era == "2018" and wp == "WPL" ):
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

        # Get collection from event tree
        electrons = list(Collection(event, "Electron"))
        muons = list(Collection(event, "Muon"))
        jets = list(Collection(event, "Jet"))

        # Get variables from event tree
        Z_pt = event.Z_pt
        Z_eta = event.Z_eta
        met_pt = event.met_pt
        met_phi = event.met_phi

        # ngood_leptons = event.ngood_leptons
        # lead_lep_pt = event.leading_lep_pt
        # trail_lep_pt = event.trailing_lep_pt

        # ngood_jets = event.ngood_jets
        # lead_jet_pt = event.lead_jet_pt

        # count leptons
        good_leptons = []
        # Choose tight-quality e/mu for event categorization
        for idx,mu in enumerate(muons):
            isoLep   = mu.pfRelIso04_all
            pass_ips = abs(mu.dxy) < 0.02 and abs(mu.dz) < 0.1
            pass_fid = abs(mu.eta) < 2.4 and mu.pt >= (25 if idx==0 else 20)
            pass_ids = mu.tightId and isoLep <= 0.15
            if pass_fid and pass_ids and pass_ips:
                good_leptons.append(mu)
        for idy,el in enumerate(electrons):
            id_CB = el.cutBased
            # changing to MVA based ID :
            if el.pt >= (25 if idy==0 else 20) and abs(el.eta) <= 2.5 and self.electron_id(el, "90" ):
                good_leptons.append(el)
        # sort the leptons in pt
        good_leptons.sort(key=lambda x: x.pt, reverse=True)
        ngood_leptons = len(good_leptons)
        if ngood_leptons!=event.ngood_leptons:
            print 'ngood_leptons: {} in VBSProducer, {} in MonoZProducer'.format(ngood_leptons, event.ngood_leptons)
        lead_lep_pt = good_leptons[0].pt if ngood_leptons else 0.0
        trail_lep_pt = good_leptons[1].pt if ngood_leptons >= 2 else 0.0

        # process jet
        good_jets  = []
        et_jets20 = 0.0
        et_jets30 = 0.0
        for jet in jets:
            if not jet.jetId:
                continue
            if tk.closest(jet, good_leptons)[1] < 0.4:
                continue
            if jet.pt <= 20 or abs(jet.eta) > 4.7:
                continue
            et_jets20 += jet.p4().Et()
            if jet.pt < 30.0:
                continue
            et_jets30 += jet.p4().Et()
            good_jets.append(jet)
        x_denom20 = ( et_jets20 + met_pt + Z_pt )
        x_denom30 = ( et_jets30 + met_pt + Z_pt )
        # sort the jets in pt
        good_jets.sort(key=lambda jet: jet.pt, reverse=True)
        ngood_jets = len(good_jets)
        if ngood_jets!=event.ngood_jets:
            print 'ngood_jets: {} in VBSProducer, {} in MonoZProducer'.format(ngood_jets, event.ngood_jets)
        lead_jet_pt = good_jets[0].pt if len(good_jets) else 0.0
        lead_jet_eta = good_jets[0].eta if len(good_jets) else -99.0
        trail_jet_pt = good_jets[1].pt if len(good_jets)>1 else 0.0
        trail_jet_eta = good_jets[1].eta if len(good_jets)>1 else -99.0

        dijet_abs_delta_eta = abs(lead_jet_eta-trail_jet_eta) if ngood_jets >= 2 else -99.0
        dijet_Mjj = (good_jets[0].p4() + good_jets[1].p4()).M() if ngood_jets >= 2 else 0.0
        dijet_Zep = Z_eta - 0.5*(lead_jet_eta + trail_jet_eta) if ngood_leptons >=2 and ngood_jets >= 2 else -99.0
        dijet_centrality_gg = np.exp(-4*(dijet_Zep/lead_jet_eta)**2) if ngood_jets >= 2 else -99.0

        x_Z = Z_pt / x_denom30 if x_denom30!=0 else -10.0
        x_jet20 = et_jets20 / x_denom20 if x_denom20!=0 else -10.0 
        x_jet30 = et_jets30 / x_denom30 if x_denom30!=0 else -10.0
        x_MET = met_pt / x_denom30 if x_denom30!=0 else -10.0
        zeppenfeld = Z_eta - (lead_jet_eta + trail_jet_eta) / 2
        H_T = sum( [jet.pt for jet in good_jets] )
        HT_F = (lead_jet_pt +trail_jet_pt) / H_T if H_T != 0 else 0.0
        Jet_pt_Ratio = trail_jet_pt / lead_jet_pt if ngood_jets >=2 else -99.0
        R_pt = lead_lep_pt * trail_lep_pt / (lead_jet_pt * trail_jet_pt) if ngood_leptons >=2 and ngood_jets >=2 else -99.0
        Jet_etas_multiplied = lead_jet_eta * trail_jet_eta
        dPT_OZ = (lead_jet_pt + trail_jet_pt) / Z_pt if Z_pt!=0 else -99.0
        #dPT_OZ = (good_jets[0].pt + good_jets[1].pt) / Z_pt if Z_pt!=0 else -10.0

        CJV_Pt = 0.0
        CJV_Pt_Sum = 0.0
        for jet in good_jets:
            if lead_jet_eta > 0 and jet.eta < lead_jet_eta:
                if jet.eta > trail_jet_eta:
                    if jet.pt > CJV_Pt:
                        CJV_Pt = jet.pt
                    CJV_Pt_Sum += jet.pt
            elif lead_jet_eta < 0 and jet.eta > lead_jet_eta:
                if jet.eta < trail_jet_eta:
                    if jet.pt > CJV_Pt:
                        CJV_Pt = jet.pt
                    CJV_Pt_Sum += jet.pt

        deltaPhiLeadingJetMet = abs(tk.deltaPhi(good_jets[0].phi,met_phi)) if ngood_jets else abs(met_phi) 
        deltaPhiClosestJetMet = 10.0
        deltaPhiFarthestJetMet = -1.0
        for jet in good_jets:
            if deltaPhiClosestJetMet > abs(tk.deltaPhi(jet.phi,met_phi)):
                deltaPhiClosestJetMet = abs(tk.deltaPhi(jet.phi,met_phi))
            if deltaPhiFarthestJetMet < abs(tk.deltaPhi(jet.phi,met_phi)):
                deltaPhiFarthestJetMet = abs(tk.deltaPhi(jet.phi,met_phi))
    
        etaThirdJet = good_jets[2].eta if ngood_jets >=3 else -99.0

        self.out.fillBranch( "lead_jet_eta{}".format(self.syst_suffix), lead_jet_eta )
        self.out.fillBranch( "trail_jet_pt{}".format(self.syst_suffix), trail_jet_pt )
        self.out.fillBranch( "trail_jet_eta{}".format(self.syst_suffix), trail_jet_eta )
        self.out.fillBranch( "dijet_abs_delta_eta{}".format(self.syst_suffix), dijet_abs_delta_eta )
        self.out.fillBranch( "dijet_Mjj{}".format(self.syst_suffix), dijet_Mjj )
        self.out.fillBranch( "dijet_Zep{}".format(self.syst_suffix), dijet_Zep )
        self.out.fillBranch( "dijet_centrality_gg{}".format(self.syst_suffix), dijet_centrality_gg )

        self.out.fillBranch( "x_Z{}".format(self.syst_suffix), x_Z )
        self.out.fillBranch( "x_jet20{}".format(self.syst_suffix), x_jet20 )
        self.out.fillBranch( "x_jet30{}".format(self.syst_suffix), x_jet30 )
        self.out.fillBranch( "x_MET{}".format(self.syst_suffix), x_MET )
        self.out.fillBranch( "zeppenfeld{}".format(self.syst_suffix), zeppenfeld )
        self.out.fillBranch( "H_T{}".format(self.syst_suffix), H_T )
        self.out.fillBranch( "HT_F{}".format(self.syst_suffix), HT_F )
        self.out.fillBranch( "Jet_pt_Ratio{}".format(self.syst_suffix), Jet_pt_Ratio )
        self.out.fillBranch( "R_pt{}".format(self.syst_suffix), R_pt )
        self.out.fillBranch( "Jet_etas_multiplied{}".format(self.syst_suffix), Jet_etas_multiplied )
        self.out.fillBranch( "dPT_OZ{}".format(self.syst_suffix), dPT_OZ )
        self.out.fillBranch( "CJV_Pt{}".format(self.syst_suffix), CJV_Pt )
        self.out.fillBranch( "CJV_Pt_Sum{}".format(self.syst_suffix), CJV_Pt_Sum )
        self.out.fillBranch( "deltaPhiLeadingJetMet{}".format(self.syst_suffix), deltaPhiLeadingJetMet )
        self.out.fillBranch( "deltaPhiClosestJetMet{}".format(self.syst_suffix), deltaPhiClosestJetMet )
        self.out.fillBranch( "deltaPhiFarthestJetMet{}".format(self.syst_suffix), deltaPhiFarthestJetMet )
        self.out.fillBranch( "etaThirdJet{}".format(self.syst_suffix), etaThirdJet )

        return True

