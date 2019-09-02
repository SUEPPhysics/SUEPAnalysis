import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class TriggerSFProducer(Module):
    def __init__(self,targetfile,name="TriggerSFWeight",norm=True,verbose=False,doSysVar=True):
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
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        lep_cat = 0
        if hasattr(event,"lep_category"):
            lep_cat = int(getattr(event,"lep_category"))
        if lep_cat < 1 :
            l1_pt = 0
            l1_eta = 0
            l2_pt = 0
            l2_eta = 0
            l1_flavor = 0
        else:
            l1_pt = float(getattr(event,"leading_lep_pt"))
            l1_eta = abs(float(getattr(event,"leading_lep_eta")))
            l2_pt = float(getattr(event,"trailing_lep_pt"))
            l2_eta = abs(float(getattr(event,"trailing_lep_eta")))
            l1_flavor = int(getattr(event,"leading_lep_flavor"))
        weight = 1
        weightError = 0
        if lep_cat==3 or lep_cat==5 or lep_cat==7 : #these are MM. MML and MMLL lepton categories
	    if l1_eta <= 1.5 and l2_eta <= 1.5:
	    	hist = self.loadHisto(self.targetfile,"trgSFMMBB")
            elif l1_eta >= 1.5 and l2_eta <= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFMMEB")
            elif l1_eta <= 1.5 and l2_eta >= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFMMBE")
            elif l1_eta >= 1.5 and l2_eta >= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFMMEE")
        elif lep_cat==1 or lep_cat==4 or lep_cat==6 : #these are EE. EEL and EELL lepton categories
            if l1_eta <= 1.5 and l2_eta <= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFEEBB")
            elif l1_eta >= 1.5 and l2_eta <= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFEEEB")
            elif l1_eta <= 1.5 and l2_eta >= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFEEBE")
            elif l1_eta >= 1.5 and l2_eta >= 1.5:
                hist = self.loadHisto(self.targetfile,"trgSFEEEE")
        else : #This is the EM and ME categories
	    if l1_flavor == 1: #This is the muon leading
            	if l1_eta <= 1.5 and l2_eta <= 1.5:
            	    hist = self.loadHisto(self.targetfile,"trgSFMEBB")
            	elif l1_eta >= 1.5 and l2_eta <= 1.5:
            	    hist = self.loadHisto(self.targetfile,"trgSFMEEB")
            	elif l1_eta <= 1.5 and l2_eta >= 1.5:
            	    hist = self.loadHisto(self.targetfile,"trgSFMEBE")
            	elif l1_eta >= 1.5 and l2_eta >= 1.5:
            	    hist = self.loadHisto(self.targetfile,"trgSFMEEE")
            elif l1_flavor == 0: #This is the electron leading
                if l1_eta <= 1.5 and l2_eta <= 1.5:
                    hist = self.loadHisto(self.targetfile,"trgSFEMBB")
                elif l1_eta >= 1.5 and l2_eta <= 1.5:
                    hist = self.loadHisto(self.targetfile,"trgSFEMEB")
                elif l1_eta <= 1.5 and l2_eta >= 1.5:
                    hist = self.loadHisto(self.targetfile,"trgSFEMBE")
                elif l1_eta >= 1.5 and l2_eta >= 1.5:
                    hist = self.loadHisto(self.targetfile,"trgSFEMEE")
        nxBins = 7
	nyBins = 7
	searchbinx = -1
	searchbiny = -1
        for xbin in range(1,nxBins+1):
            if l1_pt > hist.GetXaxis().GetBinLowEdge(nxBins) + hist.GetXaxis().GetBinWidth(nxBins):
                searchbinx = 7
                break
            if l1_pt > hist.GetXaxis().GetBinLowEdge(xbin) and l1_pt < hist.GetXaxis().GetBinLowEdge(xbin) + hist.GetXaxis().GetBinWidth(xbin) :
                searchbinx = xbin
        for ybin in range(1,nyBins+1):
            if l2_pt > hist.GetYaxis().GetBinLowEdge(nyBins) + hist.GetYaxis().GetBinWidth(nyBins):
                searchbiny = 7
                break
            if l2_pt > hist.GetYaxis().GetBinLowEdge(ybin) and l2_pt < hist.GetYaxis().GetBinLowEdge(ybin) + hist.GetYaxis().GetBinWidth(ybin) :
                searchbiny = ybin

        weight = hist.GetBinContent(searchbinx,searchbiny)
        self.out.fillBranch(self.name, weight)
        if self.doSysVar:
            weightError = hist.GetBinErrorUp(searchbinx,searchbiny)
            self.out.fillBranch(self.name+"Up", weight+weightError)
            weightError = hist.GetBinErrorLow(searchbinx,searchbiny)
            self.out.fillBranch(self.name+"Down", weight-weightError)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
TrigSF_2016 = "%s/src/PhysicsTools/MonoZ/data/TriggerSFs/histo_triggerEff_sel0_2016.root" % os.environ['CMSSW_BASE']
TriggerSF_2016 = lambda : TriggerSFProducer(TrigSF_2016,verbose=False, doSysVar=True)

TrigSF_2017 = "%s/src/PhysicsTools/MonoZ/data/TriggerSFs/histo_triggerEff_sel0_2017.root" % os.environ['CMSSW_BASE']
TriggerSF_2017 = lambda : TriggerSFProducer(TrigSF_2017,verbose=False, doSysVar=True)

TrigSF_2018 = "%s/src/PhysicsTools/MonoZ/data/TriggerSFs/histo_triggerEff_sel0_2018.root" % os.environ['CMSSW_BASE']
TriggerSF_2018 = lambda : TriggerSFProducer(TrigSF_2018,verbose=False, doSysVar=True)

