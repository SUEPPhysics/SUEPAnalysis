import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class nvtxWeightProducer(Module):
    def __init__(self,targetfile,targethist="npvWeights",name="nvtxWeight",norm=True,verbose=False,nvtx_var="PV_npvs",doSysVar=True):
	print targetfile
        self.targeth = self.loadHisto(targetfile,targethist)
        self.name = name
        self.norm = norm
        self.verbose = verbose
        self.nvtxVar = nvtx_var
        self.doSysVar = doSysVar
    def loadHisto(self,filename,hname):
        tf = ROOT.TFile.Open(filename)
        hist = tf.Get(hname)
        hist.SetDirectory(None)
        tf.Close()
        return hist
    def beginJob(self):
	pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
	self.out = wrappedOutputTree
        self.out.branch(self.name, "F")
        self.out.branch(self.name+"Up", "F")
	self.out.branch(self.name+"Down", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        if hasattr(event,self.nvtxVar):
            nvtx = int(getattr(event,self.nvtxVar))
	    nBins = 40
            weight = 1
            weightError = 0
	    for bin in range(1,nBins+1):
		if nvtx > self.targeth.GetBinLowEdge(bin) and nvtx < self.targeth.GetBinLowEdge(bin) + self.targeth.GetBinWidth(bin) :
			weight = self.targeth.GetBinContent(bin)
			weightError = self.targeth.GetBinError(bin)/2
	    self.out.fillBranch(self.name, weight)
	    if self.doSysVar:	    
 		self.out.fillBranch(self.name+"Up", weight+weightError)
                self.out.fillBranch(self.name+"Down", weight-weightError)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
#nvtx_2016 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/npvWeights_2016.root" % os.environ['CMSSW_BASE']
nvtx_2016 = "%s/src/PhysicsTools/MonoZ/data/npvWeights_2016.root" % os.environ['CMSSW_BASE']
nvtxWeight_2016 = lambda : nvtxWeightProducer(nvtx_2016,verbose=False, doSysVar=True)

#nvtx_2017 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/npvWeights_2017.root" % os.environ['CMSSW_BASE']
nvtx_2017 = "%s/src/PhysicsTools/MonoZ/data/npvWeights_2017.root" % os.environ['CMSSW_BASE']
nvtxWeight_2017 = lambda : nvtxWeightProducer(nvtx_2017,verbose=False, doSysVar=True)

#nvtx_2018 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/npvWeights_2018.root" % os.environ['CMSSW_BASE']
nvtx_2018 = "%s/src/PhysicsTools/MonoZ/data/npvWeights_2018.root" % os.environ['CMSSW_BASE']
nvtxWeight_2018 = lambda : nvtxWeightProducer(nvtx_2018,verbose=False, doSysVar=True)