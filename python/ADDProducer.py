import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ADDProducer(Module):
    def __init__(self, MD=100, dim=0, era = 2015,  do_syst=False, syst_var=''):
        self.do_syst = do_syst
        self.syst_var = syst_var
        self.MD = MD
	self.dim = dim
	self.era = era
    def loadWeights(self,filename):
	weights = []
	print ( filename)
	with open(filename) as f:
		for line in f: # read rest of lines
        		weights.append([float(x) for x in line.split()])
		print (weights)
        return weights
    def beginJob(self):
	    pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("ADDWeight", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
	ADD_file = ''
        if str(self.era) == str(2016):
		if str(self.MD) == str(3):#Stupid ADD name issue in 2016 (ADDMonoZ_ZToLL vs ADDMonoZ_ZtoLL)
			ADD_file = "{}/src/PhysicsTools/MonoZ/data/ADD_ratios/ADDMonoZ_ZToLL_MD-{}_d-{}_TuneCUETP8M1_13TeV-pythia8_2016.txt".format(os.environ['CMSSW_BASE'],str(self.MD),str(self.dim))
		else:
			ADD_file = "{}/src/PhysicsTools/MonoZ/data/ADD_ratios/ADDMonoZ_ZtoLL_MD-{}_d-{}_TuneCUETP8M1_13TeV-pythia8_2016.txt".format(os.environ['CMSSW_BASE'],str(self.MD),str(self.dim))
        if str(self.era) == str(2017):
		ADD_file = "{}/src/PhysicsTools/MonoZ/data/ADD_ratios/ADDMonoZ2017_MD_{}_d_{}_2017.txt".format(os.environ['CMSSW_BASE'],str(self.MD),str(self.dim))
        if str(self.era) == str(2018):
		ADD_file = "{}/src/PhysicsTools/MonoZ/data/ADD_ratios/ADDMonoZ_MD_{}_d_{}_2018.txt".format(os.environ['CMSSW_BASE'],str(self.MD),str(self.dim))
        print (ADD_file)


        if hasattr(event,"GEN_Z_pt"):
            gen_pt = float(getattr(event,"GEN_Z_pt"))
	weights = self.loadWeights(ADD_file)
	weight = 1
	if gen_pt >= 50 and gen_pt<= 100 : weight = weights[0][0]
	if gen_pt > 100 and gen_pt<= 150 : weight = weights[1][0]
	if gen_pt > 150 and gen_pt<= 200 : weight = weights[2][0]
	if gen_pt > 200 and gen_pt<= 300 : weight = weights[3][0]
	if gen_pt > 300 and gen_pt<= 400 : weight = weights[4][0]
	if gen_pt > 400 and gen_pt<= 600 : weight = weights[5][0]
	if gen_pt > 600 and gen_pt<= 1000 : weight = weights[6][0]
	if gen_pt > 1000 and gen_pt <= 5000 : weight = weights[7][0]
	if gen_pt > 5000 : weight = 1
        self.out.fillBranch("ADDWeight", weight)
        return True
