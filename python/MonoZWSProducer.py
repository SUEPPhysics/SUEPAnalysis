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

    def beginJob(self, histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)
        self.cats = {
            1 : "EE",
            2 : "EM",
            3 : "MM",
            4 : "3L",
            5 : "4L",
            6 : "NRB",
            7 : "TOP"
        }

        self.h_met  = {}
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
            if cat == 'NRB' or cat=="TOP":
                self.h_met[i] = ROOT.TH1F(
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    12, ar.array('d', [40,45,50,55,60,65,70,75,80,85,90,95,100])
                    )
            elif cat == "EE" or cat=="MM" or cat=="EM":
                self.h_met[i] = ROOT.TH1F(
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    13, ar.array('d', [40,50,75,100,125,150,175,200,250,300,350,400,500,600])
                )
            else:
                self.h_met[i] = ROOT.TH1F(
                    'emulatedMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'emulatedMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    20, 0, 200
                )

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        prevdir = ROOT.gDirectory
        outputFile.cd()
        for i,cat in self.cats.items():
            self.h_met[i].Write()
            self.h_mll[i].Write()
        self.h_njet.Write()
        prevdir.cd()

    def analyze(self, event):
        # only valid in the MC samples
        if False:
            print " puWeight        : ", event.puWeight
            print " lepton_category : ", event.lep_category
            print " lumiWeight      : ", event.lumiWeight

        measMET = 0
        measMll = 0
        Njets = -1
        lep_category = 0
        try:
            lep_category = getattr(event, "lep_category{}".format(self.syst_suffix))
        except:
            lep_category = getattr(event, "lep_category")

        if lep_category <= 3:
            if self.weight_syst:
                measMET = getattr(event, "met_pt")
                measMll = getattr(event, "Z_mass")
                Njets   = getattr(event, "ngood_jets")
            else:
                measMET = getattr(event, "met_pt{}".format(self.syst_suffix))
                measMll = getattr(event, "Z_mass{}".format(self.syst_suffix))
                Njets   = getattr(event, "ngood_jets{}".format(self.syst_suffix))
        else:
            if self.weight_syst:
                measMET = getattr(event, "emulatedMET")
                measMll = getattr(event, "Z_mass")
                Njets   = getattr(event, "ngood_jets")
            else:
                measMET = getattr(event, "emulatedMET{}".format(self.syst_suffix))
                measMll = getattr(event, "Z_mass{}".format(self.syst_suffix))
                Njets   = getattr(event, "ngood_jets{}".format(self.syst_suffix))

        #    0 : "NOL",
        #    1 : "EE",
        #    2 : "EM",
        #    3 : "MM",
        #    4 : "EEL",
        #    5 : "MML",
        #    6 : "EELL",
        #    7 : "MMLL"
        new_lepcat = lep_category
        if (lep_category == 4 or lep_category == 5):
            new_lepcat = 4
        elif (lep_category == 6 or lep_category == 7):
            new_lepcat = 5
        weight = event.weightRaw # wieght without deviding on number of events
        # pu uncertainty
        if self.isMC:
            #weight *= event.genWeight
            if "puWeight" in self.syst_suffix:
                if "Up" in self.syst_suffix:
                    weight *= event.puWeightUp
                else:
                    weight *= event.puWeightDown
            else:
            	weight *= event.puWeight
            # PDF uncertainty

            # QCD Scale weights

        # Filling histograms for given selection only:

        if ( abs(event.Z_mass - 91.1876) < 15
             and event.Z_pt        >  60
             and event.nhad_taus   == 0
             and event.met_pt      >  100
             and abs(event.MET_phi-event.Z_phi) > 2.6
             and abs(event.Z_pt-event.met_pt)/event.Z_pt < 0.4
             and abs(event.delta_phi_j_met) > 0.5
             and event.delta_R_ll < 1.8):
            self.h_njet.Fill(Njets, weight)
        # Signal region
        if ( (new_lepcat == 1 or new_lepcat == 3)
            and abs(event.Z_mass - 91.1876) < 15
            and event.ngood_jets  <= 1
            and event.ngood_bjets == 0
            and event.Z_pt        >  60
            and event.nhad_taus   == 0
            and event.met_pt      >  100
            and abs(event.MET_phi-event.Z_phi) > 2.6
            and abs(event.Z_pt-event.met_pt)/event.Z_pt < 0.4
            and abs(event.delta_phi_j_met) > 0.5
            and event.delta_R_ll < 1.8):
            #print " -- signal region"
            self.h_met[int(new_lepcat)].Fill(measMET, weight)
            self.h_mll[int(new_lepcat)].Fill(measMll, weight)
        if (new_lepcat == 4
            and event.Z_pt > 60
            and abs(event.Z_mass - 91.1876) < 15.0
            and event.ngood_jets  <= 1
            and event.ngood_bjets == 0
            and event.met_pt      >  30
            and event.mass_alllep > 100
            and abs(event.Z_pt - event.emulatedMET)/event.Z_pt < 0.4
            and abs(event.emulatedMET_phi-event.Z_phi) > 2.8):
            #print " -- WZ categiry"
            self.h_met[4].Fill(measMET, weight)
            self.h_mll[4].Fill(measMll, weight)
        if (new_lepcat == 5
            and event.Z_pt  > 60
            and abs(event.Z_mass - 91.1876) < 30.0
            and event.ngood_jets <= 1
            and abs(event.emulatedMET_phi-event.Z_phi) > 2.8 ):
            #print " -- ZZ categiry"
            self.h_met[5].Fill(measMET, weight)
            self.h_mll[5].Fill(measMll, weight)
        if (new_lepcat == 2
            and event.Z_pt  > 60
            and abs(event.Z_mass - 91.1876) < 15
            and event.ngood_jets  <= 1
            and event.ngood_bjets == 0
            and event.met_pt      >  50 ):
            #print " -- NRB categiry"
            self.h_met[6].Fill(measMET, weight)
            self.h_mll[6].Fill(measMll, weight)
        if (new_lepcat == 2
            and event.Z_pt  > 60
            and abs(event.Z_mass - 91.1876) < 15
            and event.ngood_jets  >  2
            and event.ngood_bjets >= 1
            and event.met_pt      >  50):
            #print " -- TOP categiry"
            self.h_met[7].Fill(measMET, weight)
            self.h_mll[7].Fill(measMll, weight)

        return True
