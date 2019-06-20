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
            1 : "catEE" ,
            2 : "catEM" ,
            3 : "catMM" ,
            4 : "cat3L" ,
            5 : "cat4L" ,
            6 : "catNRB",
            7 : "catTOP",
            8 : "catDY",
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
        self.h_met  = {}
        self.h_bal = ROOT.TH1F(
            'balance{}{}'.format("_" + self.sample, self.syst_suffix),
            'balance{}{}'.format("_" + self.sample, self.syst_suffix),
            10, 0, 1
        )
        self.h_phi = ROOT.TH1F(
            'phizmet{}{}'.format("_" + self.sample, self.syst_suffix),
            'phizmet{}{}'.format("_" + self.sample, self.syst_suffix),
            10, 0, 1
        )
        self.h_njet = ROOT.TH1F(
            'njet{}{}'.format("_" + self.sample, self.syst_suffix),
            'njet{}{}'.format("_" + self.sample, self.syst_suffix),
            6, 0, 6
        )

        self.h_mll = {}
        for i,cat in self.cats.items():
            self.h_mll[i] = ROOT.TH1F(
                'mll{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                'mll{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                50, 50, 150
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
        #if not outputFile.Get("Shapes"):
        #    outputFile.mkdir("Shapes")
        #outputFile.cd("Shapes")
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
            meas_Mll = getattr(event, "Z_mass")
            meas_Njet= getattr(event, "ngood_jets")
            meas_BAL = getattr(event, "sca_balance")
            meas_ZMETPHI = getattr(event, "delta_phi_ZMet")
        else:
            meas_MET = getattr(event, "met_pt{}".format(self.syst_suffix))
            meas_Mll = getattr(event, "Z_mass{}".format(self.syst_suffix))
            meas_Njet= getattr(event, "ngood_jets{}".format(self.syst_suffix))
            meas_BAL = getattr(event, "sca_balance{}".format(self.syst_suffix))
            meas_ZMETPHI = getattr(event, "delta_phi_ZMet{}".format(self.syst_suffix))

        new_lepcat = lep_category
        if   (lep_category  <= 3):
            new_lepcat = lep_category
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
                    weight *= kEW
            except:
                pass
            # NNLO crrection
            try:
                weight *= event.kNNLO
            except:
                pass
            # PDF uncertainty
            if "PDF" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.pdfw_Up
                else:
                    weight *= event.pdfw_Down
            # QCD Scale weights
            # TODO: add various variations
            if "QCDScale" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.pdfw_Up
                else:
                    weight *= event.pdfw_Down
            # bTagSF
            #if "bTagSF" in self.syst_suffix:
            #    if "Up" in self.syst_suffix:
            #        weight *= event.Jet_btagSF_up
            #    else:
            #        weight *= event.Jet_btagSF_down
            #else:
            #    weight *= event.Jet_btagSF
            # Muon SF
            if "MuonSFEff" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.w_muon_SFUp
                else:
                    weight *= event.w_muon_SFDown
            else:
                weight *= event.w_muon_SF
            # Electron SF
            if "ElecronSFEff" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.w_electron_SFUp
                else:
                    weight *= event.w_electron_SFDown
            else:
                weight *= event.w_electron_SF
	    #Prefire Weight
            if "PrefireWeight" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.PrefireWeight_Up
                else:
                    weight *= event.PrefireWeight_Down
            else:
                weight *= event.PrefireWeight


        # NJETS: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "ngood_jets", "signal") ):
            self.h_njet.Fill(meas_Njet)

        # Balance: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "sca_balance", "signal") ):
            self.h_bal.Fill(meas_BAL)

        # ZMET-Phi : Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "delta_phi_j_met", "signal") ):
            self.h_phi.Fill(meas_ZMETPHI)

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
            self.h_met[4].Fill(meas_MET, weight)
        # MET: Cat4L
        if ( (new_lepcat == 5) and self.passbut(event, "emulatedMET", "cat4L") ):
            self.h_met[5].Fill(meas_MET, weight)


        # Mass: Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3) and self.passbut(event, "Z_mass", "signal") ):
            self.h_mll[int(new_lepcat)].Fill(meas_MET, weight)
            self.h_mll[8].Fill(meas_Mll, weight)
        # Mass: CatNRB
        if ( (new_lepcat == 2) and self.passbut(event, "Z_mass", "catNRB") ):
            self.h_mll[6].Fill(meas_Mll, weight)
            self.h_mll[2].Fill(meas_Mll, weight)
        # Mass: CatTOP
        if ( (new_lepcat == 2) and self.passbut(event, "Z_mass", "catTOP") ):
            self.h_mll[7].Fill(meas_Mll, weight)
        # Mass: Cat3L
        if ( (new_lepcat == 4) and self.passbut(event, "Z_mass", "cat3L") ):
            self.h_mll[4].Fill(meas_Mll, weight)
        # Mass: Cat4L
        if ( (new_lepcat == 5) and self.passbut(event, "Z_mass", "cat4L") ):
            self.h_mll[5].Fill(meas_Mll, weight)



        return True
