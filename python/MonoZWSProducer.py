import ROOT
from importlib import import_module

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

ROOT.PyConfig.IgnoreCommandLineOptions = True


class MonoZWSProducer(Module):
    def __init__(self, isMC, era=2017, sample="DY", do_syst=False, syst_var=''):
        self.isMC = isMC
        self.era = era
        self.sample = sample
        self.do_syst = do_syst
        self.syst_var = syst_var
        if self.syst_var !='':
            self.syst_suffix = '_sys_' + syst_var if do_syst else ''
        else:
            self.syst_suffix = syst_var
        self.writeHistFile=True
    
    def beginJob(self, histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)
        self.cats = {
            0 : "NOL",
            1 : "EE",
            2 : "EM",
            3 : "MM",
            4 : "EEL",
            5 : "MML",
            6 : "EELL",
            7 : "MMLL"
        }
        
        self.h_met = {}
        for i,cat in self.cats.items():
            self.h_met[i] = ROOT.TH1F(
                'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                'measMET{}{}{}'.format("_" + self.sample, "_" + cat, self.syst_suffix),
                50, 100, 600
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
            
        if lep_category < 3:
            measMET = getattr(event, "met_pt{}".format(self.syst_suffix))
        else:
            measMET = getattr(event, "emulatedMET{}".format(self.syst_suffix))
            
        weight = event.lumiWeight
        # pu uncertainty
        print " -- systematic  : ", self.syst_suffix
        if self.isMC: 
            weight *= event.genWeight
            #if "puWeight" in self.syst_suffix:
            #    if "Up" in self.syst_suffix:
            #        weight *= event.puWeightUp
            #    else:
            #        weight *= event.puWeightDown
            #else:
            weight *= event.puWeight
            
        # PDF uncertainty
        
        # QCD Scale weights
        
        # Filling histograms
        self.h_met[int(lep_category)].Fill(measMET, weight)
	return True
