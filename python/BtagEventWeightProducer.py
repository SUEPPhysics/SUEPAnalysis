import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class BtagEventWeightProducer(Module):
    def __init__(self,targetfile,name="btagEventWeight",norm=True,verbose=False,doSysVar=True):
	print targetfile
	self.targetfile = targetfile
        self.name = name
        self.norm = norm
        self.verbose = verbose
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
        pass
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
	#Weight calclulated on an event-by-event basis assuming a bjet veto following:
	#https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagSFMethods#1b_Event_reweighting_using_scale
        weight = 1.0
	weight_up = 1.0
	weight_down = 1.0
	jets = list(Collection(event, "Jet"))
        for i,j in enumerate(jets):
            flavor =  j.hadronFlavour
            SF = j.btagSF # lets see if this works
            SFup = j.btagSF_up
            SFdown = j.btagSF_down	
            if flavor == 5: #this is for the actual bottom events
                hist = self.loadHisto(self.targetfile,"bottom_eff")
            elif flavor == 4: #this is for the charm events
                hist = self.loadHisto(self.targetfile,"charm_eff")
            elif flavor == 0: #this is for the light flavored jets
                hist = self.loadHisto(self.targetfile,"light_eff")
            else:
                print "The jet flavor does not make sense!!!!!!"
                continue
            #Now for Bin loops
            nxBins = 5
            nyBins = 12
            searchbinx = -1
            searchbiny = -1
            for xbin in range(1,nxBins+1):
                if j.pt > hist.GetXaxis().GetBinLowEdge(nxBins) + hist.GetXaxis().GetBinWidth(nxBins):
                    searchbinx = 12
                    break
                if j.pt > hist.GetXaxis().GetBinLowEdge(xbin) and j.pt < hist.GetXaxis().GetBinLowEdge(xbin) + hist.GetXaxis().GetBinWidth(xbin) :
                    searchbinx = xbin
            for ybin in range(1,nyBins+1):
                if j.eta > hist.GetYaxis().GetBinLowEdge(nyBins) + hist.GetYaxis().GetBinWidth(nyBins):
                    searchbiny = 5
                    break
                if j.eta > hist.GetYaxis().GetBinLowEdge(ybin) and j.eta < hist.GetYaxis().GetBinLowEdge(ybin) + hist.GetYaxis().GetBinWidth(ybin) :
                    searchbiny = ybin
	    
            eff = hist.GetBinContent(searchbinx,searchbiny)                
            err = np.sqrt(eff*(1-eff)/5000.)
            test = hist.GetBinError(searchbinx,searchbiny)

            weight *= (1.0 - SF * eff)
            weight_up *= (1.0 - SFup * (eff + err))
            weight_down *= (1.0 - SFdown * (eff - err))

        if int(getattr(event,"ngood_bjets")) > 0:
		weight = 1.0 - weight
	  	weight_up = 1.0 - weight_up
		weight_down = 1.0 - weight_down
        self.out.fillBranch(self.name, weight)
        if self.doSysVar:
            self.out.fillBranch(self.name+"Up", weight_up)
            self.out.fillBranch(self.name+"Down", weight_down)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
BtagEff_2016 = "%s/src/PhysicsTools/MonoZ/data/BTagEff/BTagEff_2016.root" % os.environ['CMSSW_BASE']
BtagEventWeight_2016 = lambda : BtagEventWeightProducer(BtagEff_2016,verbose=False, doSysVar=True)

BtagEff_2017 = "%s/src/PhysicsTools/MonoZ/data/BTagEff/BTagEff_2017.root" % os.environ['CMSSW_BASE']
BtagEventWeight_2017 = lambda : BtagEventWeightProducer(BtagEff_2017,verbose=False, doSysVar=True)

BtagEff_2018 = "%s/src/PhysicsTools/MonoZ/data/BTagEff/BTagEff_2018.root" % os.environ['CMSSW_BASE']
BtagEventWeight_2018 = lambda : BtagEventWeightProducer(BtagEff_2018,verbose=False, doSysVar=True)
