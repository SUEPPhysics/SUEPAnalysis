import ROOT
from importlib import import_module

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import array as ar


ROOT.PyConfig.IgnoreCommandLineOptions = True

class MonoZWSProducer(Module):
    def __init__(self, isMC, era=2017, sample="DY", do_syst=False, syst_var='', weight_syst=False):
        self.isMC = isMC
        self.era = era
        self.sample = sample
        self.do_syst = do_syst
        self.syst_var = syst_var
        self.weight_syst = weight_syst
        if self.syst_var !='':
            self.syst_suffix = '_sys_' + syst_var if do_syst else ''
        else:
            self.syst_suffix = syst_var
        self.writeHistFile=True

    def passbut(self, event, excut=None, cat="signal"):
        event_pass = True
        for cut in self.selection[cat]:
            if self.weight_syst:
                cut = cut.format(sys="")
            else:
                cut = cut.format(sys=self.syst_suffix)
            if excut is not None:
                if excut in cut:
                    continue
            if eval(cut) is False:
                event_pass = False
        return event_pass

    def beginJob(self, histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)
        self.cats = {
            1  : "catSignal-0jet" ,
            2  : "catEM" ,
            3  : "catSignal-1jet" ,
            4  : "cat3L" ,
            5  : "cat4L" ,
            6  : "catNRB",
            7  : "catTOP",
            8  : "catDY",
        }
        self.selection = {
            "signal" : [
                "event.Z_pt{sys}        >  60" ,
                "abs(event.Z_mass{sys} - 91.1876) < 15",
                "event.ngood_jets{sys}  <=  1" ,
                "event.ngood_bjets{sys} ==  0" ,
                "event.nhad_taus{sys}   ==  0" ,
                "event.met_pt{sys}      >  50" ,
                "abs(event.MET_phi - event.Z_phi{sys}) > 2.6",
                "abs(event.sca_balance{sys}    ) < 1.5",
                "abs(event.delta_phi_j_met{sys}) > 0.5",
                "event.delta_R_ll{sys} < 1.8"
            ],
            "cat3L": [
                "event.Z_pt{sys}        >  60" ,
                "abs(event.Z_mass{sys} - 91.1876) < 15",
                "event.ngood_jets{sys}  <=  1" ,
                "event.ngood_bjets{sys} ==  0" ,
                "event.met_pt{sys}      >  30" ,
                "event.mass_alllep{sys} > 100" ,
                "abs(event.sca_balance{sys})     < 1.5",
                "abs(event.MET_phi - event.Z_phi{sys}) > 2.6",
            ],
            "cat4L": [
                "event.Z_pt{sys}        >  60" ,
                "abs(event.Z_mass{sys} - 91.1876) < 35",
                "event.ngood_jets{sys}  <=  1" ,
                "abs(event.MET_phi - event.Z_phi{sys}) > 2.6",
            ],
            "catNRB": [
                "event.Z_pt{sys}        >  60" ,
                "abs(event.Z_mass{sys} - 91.1876) < 15",
                "event.ngood_jets{sys}  <=  1" ,
                "event.ngood_bjets{sys} ==  0" ,
                "event.met_pt{sys}      >  30"
            ],
            "catTOP": [
                "event.Z_pt{sys}        >  60" ,
                "abs(event.Z_mass{sys} - 91.1876) < 15",
                "event.ngood_jets{sys}  >   2" ,
                "event.ngood_bjets{sys} >=  1" ,
                "event.met_pt{sys}      >  30"
            ]
        }
        self.h_bal = ROOT.TH1F(
            'balance{}{}'.format("_" + self.sample, self.syst_suffix),
            'balance{}{}'.format("_" + self.sample, self.syst_suffix),
            50, 0, 1
        )
        self.h_phi = ROOT.TH1F(
            'phizmet{}{}'.format("_" + self.sample, self.syst_suffix),
            'phizmet{}{}'.format("_" + self.sample, self.syst_suffix),
            50, 0, 1
        )
        self.h_njet = ROOT.TH1F(
            'njet{}{}'.format("_" + self.sample, self.syst_suffix),
            'njet{}{}'.format("_" + self.sample, self.syst_suffix),
            6, 0, 6
        )
        self.h_met = {}
        self.h_mT = {}
        for i,cat in self.cats.items():
	    self.h_mT[i] = ROOT.TH1F(
                'MT{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                'MT{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                200, 0, 400
            )
            # different binning for different regions
            if cat == 'catNRB' or cat=="catTOP" or cat=="catDY":
                self.h_met[i] = ROOT.TH1F(
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    10, ar.array('d', [50,55,60,65,70,75,80,85,90,95,100])
                )
            else:
                self.h_met[i] = ROOT.TH1F(
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    11, ar.array('d', [50,100,125,150,175,200,250,300,350,400,500,600])
                )

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        prevdir = ROOT.gDirectory
        outputFile.cd()
        for i,cat in self.cats.items():
            self.h_met[i].Write()
            self.h_mll[i].Write()
        self.h_bal.Write()
        self.h_phi.Write()
        self.h_njet.Write()
        prevdir.cd()

    def analyze(self, event):
        # only valid in the MC samples

        meas_MET     = 0
        meas_Mll     = 0
        emul_MET     = 0
        meas_Njet    = -1
        meas_ZMETPHI = -1
        meas_BAL     = -1
        lep_category = 0

        try:
            lep_category = getattr(event, "lep_category{}".format(self.syst_suffix))
        except:
            lep_category = getattr(event, "lep_category")

        if self.weight_syst:
            meas_MET = getattr(event, "met_pt")
            emul_MET = getattr(event, "emulatedMET")
            meas_Mll = getattr(event, "Z_mass")
            meas_Njet= getattr(event, "ngood_jets")
            meas_BAL = getattr(event, "sca_balance")
            meas_ZMETPHI = getattr(event, "delta_phi_ZMet")
        else:
            meas_MET = getattr(event, "met_pt{}".format(self.syst_suffix))
            emul_MET = getattr(event, "emulatedMET{}".format(self.syst_suffix))
            meas_Mll = getattr(event, "Z_mass{}".format(self.syst_suffix))
            meas_Njet= getattr(event, "ngood_jets{}".format(self.syst_suffix))
            meas_BAL = getattr(event, "sca_balance{}".format(self.syst_suffix))
            meas_ZMETPHI = getattr(event, "delta_phi_ZMet{}".format(self.syst_suffix))

        new_lepcat = lep_category
        if (lep_category == 1 or lep_category == 3) and meas_Njet==0:
            new_lepcat = 1
        elif (lep_category == 1 or lep_category == 3) and meas_Njet==1:
            new_lepcat = 3
        elif lep_category == 2:
            new_lepcat = 2
        elif (lep_category == 4 or lep_category == 5):
            new_lepcat = 4
        elif (lep_category == 6 or lep_category == 7):
            new_lepcat = 5
        else:
            new_lepcat = lep_category

        # cross-section
        weight = 1.0
        try:
            weight = getattr(event, "xsecscale")
        except:
            return "ERROR: weight branch doesn't exist"

        # pu uncertainty
        if self.isMC:
            # weight *= event.genWeight
            if "puWeight" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.puWeightUp
                else:
                    weight *= event.puWeightDown
            else:
            	weight *= event.puWeight
            # Electroweak
            try:
                if "EWK" in self.syst_suffix:
                    if "Up" in self.syst_suffix:
                        weight *= event.kEWUp
                    else:
                        weight *= event.kEWDown
                else:
                    weight *= event.kEW
            except:
                pass
            # NNLO crrection
            try:
                weight *= event.kNNLO
            except:
                pass
            # PDF uncertainty
            if "PDF" in self.syst_suffix:
                try:
                    if "Up" in self.syst_suffix:
                        weight *= event.pdfw_Up
                    else:
                        weight *= event.pdfw_Down
                except:
                    pass
            # QCD Scale weights
            # TODO: add various variations
            if "QCDScale" in self.syst_suffix:
                weight *= 1.0

            if "MuonSF" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.w_muon_SFUp
                else:
                    weight *= event.w_muon_SFDown
            else:
                weight *= event.w_muon_SF
            # Electron SF
            if "ElecronSF" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.w_electron_SFUp
                else:
                    weight *= event.w_electron_SFDown
            else:
                weight *= event.w_electron_SF
	    #Prefire Weight
            try:
                if "PrefireWeight" in self.syst_suffix:
                    if "Up" in self.syst_suffix:
                        weight *= event.PrefireWeight_Up
                    else:
                        weight *= event.PrefireWeight_Down
                else:
                    weight *= event.PrefireWeight
            except:
                pass
            #nvtx Weight
            if "nvtxWeight" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.nvtxWeightUp
                else:
                    weight *= event.nvtxWeightDown
            else:
                weight *= event.nvtxWeight
            #TriggerSFWeight
            if "TriggerSFWeight" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.TriggerSFWeightUp
                else:
                    weight *= event.TriggerSFWeightDown
            else:
                weight *= event.TriggerSFWeight
            #BTagEventWeight
            if "btagEventWeight" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.btagEventWeightUp
                else:
                    weight *= event.btagEventWeightDown
            else:
                weight *= event.btagEventWeight

        # NJETS: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "ngood_jets", "signal") ):
            self.h_njet.Fill(meas_Njet, weight)

        # Balance: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "sca_balance", "signal") ):
            self.h_bal.Fill(meas_BAL, weight)

        # ZMET-Phi : Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "MET_phi", "signal") ):
            self.h_phi.Fill(meas_ZMETPHI, weight)

        # MET: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "met_pt", "signal") ):
            self.h_met[int(new_lepcat)].Fill(meas_MET, weight)
            self.h_met[8].Fill(meas_MET, weight)
        # MET: CatNRB
        if ( (new_lepcat == 2) and self.passbut(event, "met_pt", "catNRB") ):
            self.h_met[6].Fill(meas_MET, weight)
            self.h_met[2].Fill(meas_MET, weight)
        # MET: CatTOP
        if ( (new_lepcat == 2) and self.passbut(event, "met_pt", "catTOP") ):
            self.h_met[7].Fill(meas_MET, weight)
        # MET: Cat3L
        if ( (new_lepcat == 4) and self.passbut(event, "emulatedMET", "cat3L") ):
            self.h_met[4].Fill(emul_MET, weight)
        # MET: Cat4L
        if ( (new_lepcat == 5) and self.passbut(event, "emulatedMET", "cat4L") ):
            self.h_met[5].Fill(emul_MET, weight)


        # Mass: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, cat="signal") ):
            self.h_mT[int(new_lepcat)].Fill(meas_MET, weight)
            self.h_mT[8].Fill(meas_Mll, weight)
        # Mass: CatNRB
        if ( (new_lepcat == 2) and self.passbut(event, cat="catNRB") ):
            self.h_mT[6].Fill(meas_Mll, weight)
            self.h_mT[2].Fill(meas_Mll, weight)
        # Mass: CatTOP
        if ( (new_lepcat == 2) and self.passbut(event, cat="catTOP") ):
            self.h_mT[7].Fill(meas_Mll, weight)
        # Mass: Cat3L
        if ( (new_lepcat == 4) and self.passbut(event, cat="cat3L") ):
            self.h_mT[4].Fill(meas_Mll, weight)
        # Mass: Cat4L
        if ( (new_lepcat == 5) and self.passbut(event, cat="cat4L") ):
            self.h_mT[5].Fill(meas_Mll, weight)



        return True
