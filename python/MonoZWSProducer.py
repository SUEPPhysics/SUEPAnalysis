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
        #self.cats = {
        #    0 : "NOL",
        #    1 : "EE",
        #    2 : "EM",
        #    3 : "MM",
        #    4 : "EEL",
        #    5 : "MML",
        #    6 : "EELL",
        #    7 : "MMLL"
        #}
        self.cats = {
            1 : "EE",
            2 : "EM",
            3 : "MM",
            4 : "3L",
            5 : "4L",
            6 : "LowMET",
        }
        
        self.h_met = {}
        for i,cat in self.cats.items():
            if cat == 'LowMET':
                self.h_met[i] = ROOT.TH1F(
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    6, ar.array('d', [40,50,60,70,80,90,100])
                )
            else:
                self.h_met[i] = ROOT.TH1F(
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                    10, ar.array('d', [100,125,150,175,200,250,300,350,400,500,600])
                )
            
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        prevdir = ROOT.gDirectory
        outputFile.cd()
        for i,cat in self.cats.items():
            self.h_met[i].Write()
        prevdir.cd()
        
    def analyze(self, event):
        # only valid in the MC samples
        if False:
            print " puWeight        : ", event.puWeight
            print " lepton_category : ", event.lep_category
            print " lumiWeight      : ", event.lumiWeight
        
        measMET = 0
        lep_category = 0
        try:
            lep_category = getattr(event, "lep_category{}".format(self.syst_suffix))
        except:
            lep_category = getattr(event, "lep_category")
            
        if lep_category <= 3:
            if self.weight_syst: 
                measMET = getattr(event, "met_pt")
            else:
                measMET = getattr(event, "met_pt{}".format(self.syst_suffix))
        else:
            if self.weight_syst: 
                measMET = getattr(event, "emulatedMET")
            else:
                measMET = getattr(event, "emulatedMET{}".format(self.syst_suffix))
                #self.cats = {
        #    0 : "NOL",
        #    1 : "EE",
        #    2 : "EM",
        #    3 : "MM",
        #    4 : "EEL",
        #    5 : "MML",
        #    6 : "EELL",
        #    7 : "MMLL"
        #}
        new_lepcat = lep_category
        if lep_category <= 3:
            if measMET < 100:
                new_lepcat = 6 
        elif (lep_category == 4 or lep_category == 5):
            new_lepcat = 3
        else:
            new_lepcat = 4
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
        if (event.Z_pt > 60.0 and event.ngood_jets < 2 and new_lepcat > 0 and 
            event.ngood_bjets == 0 and #measMET > 100 and 
            event.nhad_taus==0 and event.delta_R_ll < 1.8 and 
            event.delta_phi_ZMet > 2.8 and abs(event.Z_mass - 91.1876) < 15.0):
            self.h_met[int(new_lepcat)].Fill(measMET, weight)
	return True
