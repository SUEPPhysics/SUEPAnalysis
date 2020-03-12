import ROOT
import sys, os
import numpy as np
import math
from importlib import import_module
import itertools
from copy import deepcopy
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import PhysicsTools.NanoAODTools.postprocessing.tools as tk

ROOT.PyConfig.IgnoreCommandLineOptions = True


class MonoZProducer(Module):
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
        self.out.branch("lep_category{}".format(self.syst_suffix), "I")

        self.out.branch("leading_lep_pt{}".format(self.syst_suffix), "F")
        self.out.branch("leading_lep_eta{}".format(self.syst_suffix), "F")
        self.out.branch("trailing_lep_pt{}".format(self.syst_suffix), "F")
        self.out.branch("trailing_lep_eta{}".format(self.syst_suffix), "F")
        self.out.branch("leading_lep_flavor{}".format(self.syst_suffix), "I")

        self.out.branch("met_filter{}".format(self.syst_suffix), "I")

        self.out.branch("Z_pt{}".format(self.syst_suffix), "F")
        self.out.branch("Z_eta{}".format(self.syst_suffix), "F")
        self.out.branch("Z_phi{}".format(self.syst_suffix), "F")
        self.out.branch("Z_mass{}".format(self.syst_suffix), "F")
        self.out.branch("Z_mt{}".format(self.syst_suffix), "F")

        self.out.branch("delta_phi_ZMet{}".format(self.syst_suffix), "F")
        self.out.branch("vec_balance{}".format(self.syst_suffix), "F")
        self.out.branch("sca_balance{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_ll{}".format(self.syst_suffix), "F")
        self.out.branch("delta_eta_ll{}".format(self.syst_suffix), "F")
        self.out.branch("delta_R_ll{}".format(self.syst_suffix), "F")

        self.out.branch("ngood_jets{}".format(self.syst_suffix), "I")
        self.out.branch("ngood_bjets{}".format(self.syst_suffix), "I")
        self.out.branch("lead_jet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("lead_bjet_pt{}".format(self.syst_suffix), "F")
        self.out.branch("delta_phi_j_met{}".format(self.syst_suffix), "F")

        self.out.branch("delta_met_rec{}".format(self.syst_suffix), "F")
        self.out.branch("hadronic_recoil{}".format(self.syst_suffix), "F")

        self.out.branch("emulatedMET{}".format(self.syst_suffix), "F")
        self.out.branch("emulatedMET_phi{}".format(self.syst_suffix), "F")

        self.out.branch("mass_alllep{}".format(self.syst_suffix), "F")
        self.out.branch("trans_mass{}".format(self.syst_suffix), "F")
        self.out.branch("remll_mass{}".format(self.syst_suffix), "F")
        self.out.branch("pt_alllep{}".format(self.syst_suffix), "F")
        
        self.out.branch("MT{}".format(self.syst_suffix), "F")
        self.out.branch("altMT{}".format(self.syst_suffix), "F")
	
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
        #elif (self.era == "2018" and wp == "80"):
        #    return electron.mvaFall17V1Iso_WP80
        #elif (self.era == "2018" and wp == "90"):
        #    return electron.mvaFall17V1Iso_WP90
        #elif (self.era == "2018" and wp == "WPL"):
        #    return electron.mvaFall17V1Iso_WPL


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

    def duplicate_removal(self):
        """
        For data, same event could come from different datasets
        FIXME: need to be implemented check the source from
        the old MonoZ code
        https://github.com/NEUAnalyses/monoZ_Analysis/blob/master/src/MonoZSelector.cc#L463
        """
        pass

    def analyze(self, event):
        """
        process event, return True (go to next module)
        or False (fail, go to next event)
        """
        electrons = list(Collection(event, "Electron"))
        muons = list(Collection(event, "Muon"))
        jets = list(Collection(event, "Jet"))
        taus = list(Collection(event, "Tau"))
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
        lep_category = -1

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

        # find categories
        z_candidate = []
        zcand_p4 = ROOT.TLorentzVector()
        emulated_met = ROOT.TLorentzVector()
        all_lepton_p4 = ROOT.TLorentzVector()
        rem_lepton_p4 = ROOT.TLorentzVector()

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




        lep_category = 0
        if ngood_leptons < 2:
            lep_category = -1

        if ngood_leptons == 2 and nextra_leptons==0:
            # constructing the signal region
            if (good_leptons[0].pdgId * good_leptons[1].pdgId) == -11*11:
                lep_category = 1 # EE category
            if (good_leptons[0].pdgId * good_leptons[1].pdgId) == -11*13:
                lep_category = 2 # EM category
            if (good_leptons[0].pdgId * good_leptons[1].pdgId) == -13*13:
                lep_category = 3 # MM category
            z_candidate = [good_leptons[0], good_leptons[1]]
            zcand_p4 = good_leptons[0].p4() + good_leptons[1].p4()
            all_lepton_p4 = zcand_p4
        elif ngood_leptons == 3 and nextra_leptons==0:
            # constructing the 3 leptons CR
            for pair in itertools.combinations(good_leptons, 2):
                if pair[0].pdgId == -pair[1].pdgId:
                    zcand_ = pair[0].p4() + pair[1].p4()
                    if abs(zcand_.M()-self.zmass) < abs(zcand_p4.M()-self.zmass):
                        zcand_p4 = zcand_
                        z_candidate = list(pair)
                        lep3_idx_ = 3 - good_leptons.index(pair[0]) - good_leptons.index(pair[1])
                        emulated_met = good_leptons[lep3_idx_].p4() + met_p4
                        all_lepton_p4 = zcand_ + good_leptons[lep3_idx_].p4()
                        rem_lepton_p4 = good_leptons[lep3_idx_].p4()
                        if abs(pair[0].pdgId) == 11:
                            lep_category = 4 # EEL category
                        if abs(pair[0].pdgId) == 13:
                            lep_category = 5 # MML category
        elif len(good_leptons)>=2 and (len(good_leptons) + len(extra_leptons)) == 4:
            # constructing the 4 leptons CR
            for pair in itertools.combinations(good_leptons, 2):
                # checking if OSSF pair
                rem_pair = [x for x in good_leptons + extra_leptons if x not in pair]
                if (pair[0].pdgId == -pair[1].pdgId) and (rem_pair[0].pdgId == -rem_pair[1].pdgId):
                    zcand_0 = pair[0].p4() + pair[1].p4()
                    zcand_1 = rem_pair[0].p4() + rem_pair[1].p4()

                    if abs(zcand_0.M()-self.zmass) < abs(zcand_p4.M()-self.zmass):
                        zcand_p4 = zcand_0
                        z_candidate = pair
                        emulated_met =  zcand_1 + met_p4
                        all_lepton_p4 = zcand_p4 + zcand_1
                        rem_lepton_p4 = zcand_1
                        if abs(pair[0].pdgId) == 11:
                            lep_category = 6 # EELL category
                        if abs(pair[0].pdgId) == 13:
                            lep_category = 7 # MMLL category
        else:
            # too many bad leptons, with no obvious meaning ?
            if len(good_leptons)==1 and (len(good_leptons) + len(extra_leptons))>=1:
                lep_category = -2
            elif len(good_leptons)>=2 and (len(good_leptons) + len(extra_leptons))>=2:
                lep_category = -3
            else:
                lep_category = -4

        self.out.fillBranch("lep_category{}".format(self.syst_suffix), lep_category)
        # filling MonoZ type of variables
        self.out.fillBranch("Z_pt{}".format(self.syst_suffix), zcand_p4.Pt())
        self.out.fillBranch("Z_eta{}".format(self.syst_suffix), zcand_p4.Eta())
        self.out.fillBranch("Z_phi{}".format(self.syst_suffix), zcand_p4.Phi())
        self.out.fillBranch("Z_mass{}".format(self.syst_suffix), zcand_p4.M())
        self.out.fillBranch("Z_mt{}".format(self.syst_suffix), zcand_p4.Mt())
        _delta_zphi = tk.deltaPhi(z_candidate[0].phi, z_candidate[1].phi) if lep_category > 0 else -99
        _delta_zdR  = tk.deltaR(z_candidate[0].eta, z_candidate[0].phi,
                                z_candidate[1].eta, z_candidate[1].phi,) if lep_category > 0 else -99
        _delta_zeta     = abs(z_candidate[0].eta - z_candidate[1].eta) if lep_category > 0 else -99
        _delta_phi_zmet = tk.deltaPhi(zcand_p4.Phi(), met.phi)
        _vec_delta_balance  = (met_p4 - zcand_p4).Pt()/zcand_p4.Pt() if zcand_p4.Pt() != 0 else -1
        _sca_delta_balance  = met.pt/zcand_p4.Pt() if zcand_p4.Pt() != 0 else -1

        # hadronic recoil
        had_recoil_p4 = ROOT.TLorentzVector()
        had_recoil_p4 += met_p4
        for lep in good_leptons + extra_leptons:
            had_recoil_p4 += lep.p4()
        had_recoil_p4 = -had_recoil_p4
        _delta_met_rec = tk.deltaPhi(met.phi, had_recoil_p4.Phi()) if lep_category > 0 else -99

        self.out.fillBranch("delta_phi_ll{}".format(self.syst_suffix), _delta_zphi)
        self.out.fillBranch("delta_eta_ll{}".format(self.syst_suffix), _delta_zeta)
        self.out.fillBranch("delta_R_ll{}".format(self.syst_suffix), _delta_zdR)
        self.out.fillBranch("delta_phi_ZMet{}".format(self.syst_suffix), _delta_phi_zmet)
        self.out.fillBranch("vec_balance{}".format(self.syst_suffix), _vec_delta_balance)
        self.out.fillBranch("sca_balance{}".format(self.syst_suffix), _sca_delta_balance)
        self.out.fillBranch("hadronic_recoil{}".format(self.syst_suffix), had_recoil_p4.Pt())
        self.out.fillBranch("delta_met_rec{}".format(self.syst_suffix), _delta_met_rec)
        self.out.fillBranch("emulatedMET{}".format(self.syst_suffix), emulated_met.Pt())
        self.out.fillBranch("emulatedMET_phi{}".format(self.syst_suffix), emulated_met.Phi())
        self.out.fillBranch("mass_alllep{}".format(self.syst_suffix), all_lepton_p4.M())
        self.out.fillBranch("pt_alllep{}".format(self.syst_suffix), all_lepton_p4.Pt())
        self.out.fillBranch("remll_mass{}".format(self.syst_suffix), rem_lepton_p4.M())
        
        self.out.fillBranch("MT{}".format(self.syst_suffix), 
			    np.sqrt(2*zcand_p4.Pt()*var_met_pt*(1 - np.cos(_delta_phi_zmet))))
	# defined as from https://arxiv.org/pdf/1808.09054.pdf
	Ell = np.sqrt(zcand_p4.Mag2() + zcand_p4.M2())
	self.out.fillBranch("altMT{}".format(self.syst_suffix),
			    np.sqrt(np.power(Ell + met_p4.Pt(),2) + (met_p4 + zcand_p4).Mag2()) 
			    )
        # checking the transverse mass
        _rem_p4 = ROOT.TLorentzVector()
        _rem_p4.SetPtEtaPhiM(rem_lepton_p4.Pt(), 0, rem_lepton_p4.Phi(), 0)
        self.out.fillBranch("trans_mass{}".format(self.syst_suffix), (_rem_p4 + met_p4).M())

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
        if (lep_category > 0 and zcand_p4.Pt()>60 and zcand_p4.M() > 55 and zcand_p4.M() < 127):
            return True
        else:
            return False

