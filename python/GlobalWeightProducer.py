import ROOT
import sys
import numpy as np
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

ROOT.PyConfig.IgnoreCommandLineOptions = True


class GlobalWeightProducer(Module):
    def __init__(self, isMC, lumiWeight, do_syst=False, syst_var=None):
        self.isMC = isMC
        self.lumiWeight = lumiWeight
        self.do_syst = do_syst
        self.syst_var = syst_var

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("weight", "F")
        self.out.branch("lumiWeight", "F")
        

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        # only valid in the MC samples
        if self.isMC:
            weight = event.genWeight * self.lumiWeight 
        else:
            weight = 1.0
        
        self.out.fillBranch("weight", weight)
        self.out.fillBranch("lumiWeight", self.lumiWeight if self.isMC else 1.0)
        return True
