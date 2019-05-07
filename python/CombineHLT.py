import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class CombineHLT(Module, object):
    def __init__(self, *args, **kwargs):
        import yaml

        #super(CombineHLT, self).__init__(*args, **kwargs)
        self.outName = kwargs.get("outName") if "outName" in kwargs else "HLT"
        self.doFilter = kwargs.get("doFilter") if "doFilter" in kwargs else False
	if "/CombineHLTCppWorker_cc.so" not in  ROOT.gSystem.GetLibraries():
            base = os.getenv("NANOAODTOOLS_BASE")
            if base:
                ROOT.gROOT.ProcessLine(".L %s/src/CombineHLTCppWorker.cc+O" % base)
            else:
                base = "%s/src/PhysicsTools/MonoZ"%os.getenv("CMSSW_BASE")
		print "[DEBUG] loading libs : ROOT.gSystem.Load('libPhysicsToolsNanoAODTools.so')"
		ROOT.gSystem.Load("libPhysicsToolsNanoAODTools.so")
                print "[DEBUG] compiling : .L %s/interface/CombineHLTCppWorker.h+O"
		#ROOT.gROOT.ProcessLine(".L %s/interface/CombineHLTCppWorker.h" % base)
		ROOT.gROOT.ProcessLine(".L %s/src/CombineHLTCppWorker.cc+O" % base)
        fName = kwargs.get("fileName")
        setName = kwargs.get("hltSet")
        #base = "%s/src/PhysicsTools/MonoZ"%os.getenv("CMSSW_BASE")
        d = yaml.load(open(fName))

        formula = d[setName].replace('\n', '')
        oprs = ["(", ")", "||", "&&", "!"]
        for opr in oprs: formula = formula.replace(opr, " %s " % opr)
        formula = formula.strip()

        self.names = []
        self.shortFormula = []
        for tok in formula.split():
            if tok in oprs:
                self.shortFormula.append(tok)
                continue

            idx = -1
            if tok in self.names:
                idx = self.names.index(tok)
            else:
                idx = len(self.names)
                self.names.append(tok)
            self.shortFormula.append("[%d]" % idx)
        self.shortFormula = ''.join(self.shortFormula)

        pass
    def beginJob(self):
        self.worker = ROOT.CombineHLTCppWorker(str(self.shortFormula), self.outName)
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch(self.outName, "O")
        self.initReaders(inputTree)
        pass
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def initReaders(self,tree):
        self.worker.reset();
        for i, name in enumerate(self.names):
            setattr(self, "b_"+name, tree.valueReader(name))
            self.worker.addHLT(getattr(self, "b_"+name))

        self._ttreereaderversion = tree._ttreereaderversion

        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        if event._tree._ttreereaderversion > self._ttreereaderversion:
            self.initReaders(event._tree)

        res = self.worker.analyze()
        self.out.fillBranch(self.outName, res)

        if self.doFilter: return res
        return True
