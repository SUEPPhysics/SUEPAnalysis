import ROOT
import sys
import numpy as np
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.treeReaderArrayTools import getValueReader

ROOT.PyConfig.IgnoreCommandLineOptions = True


class GenMonoZProducer(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("GEN_Z_pt", "F")
        self.out.branch("GEN_Z_mass", "F")
        self.out.branch("GEN_Z_eta", "F")
        self.out.branch("GEN_Z_phi", "F")
        self.out.branch("GEN_n_jets_30", "F")
        self.out.branch("GEN_n_leptons", "F")
        self.out.branch("GEN_leadjet_pt", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        # only valid in the MC samples

        gen_part = Collection(event, "GenPart")
        gen_jets = Collection(event, "GenJet")
        p4Gen_ms = ROOT.TLorentzVector()
        p4Gen_ll = ROOT.TLorentzVector()
	# trying to get the weights from the GlobalWeight producer
	print "+++++++++++++++++++++++++"
	#print " dir event : ", dir(event)
	print " -----------------------"
	print " puWeight : ", event.puWeight
        #print " monoz_ngood_jet : ", getattr(event, "ngood_jets", None)
	print " lumiWeight      : ", getattr(event, "lumiWeight", None)
	print "+++++++++++++++++++++++++"
	n_leptons = 0
        for part in gen_part:
            if (part.statusFlags & 128) == 0:
                continue
            id_gen_part = part.pdgId
            if abs(id_gen_part) == 12 or abs(id_gen_part) == 14 or abs(id_gen_part) == 16:
                n_leptons += 1
                p4Gen_ms += part.p4()
            elif abs(id_gen_part) == 11 or abs(id_gen_part) == 13:
                n_leptons += 1
                p4Gen_ll += part.p4()
        mZ = p4Gen_ll.M()

        self.out.fillBranch("GEN_Z_pt", p4Gen_ll.Pt())
        self.out.fillBranch("GEN_Z_mass", mZ)
        self.out.fillBranch("GEN_Z_eta", p4Gen_ll.Eta())
        self.out.fillBranch("GEN_Z_phi", p4Gen_ll.Phi())

        _gen_jets = []
        for gen_j in gen_jets:
            if gen_j.pt > 30.0 and abs(gen_j.eta) < 5.0:
                _gen_jets.append(gen_j)
        self.out.fillBranch("GEN_n_jets_30" , len(_gen_jets))
        self.out.fillBranch("GEN_n_leptons" , n_leptons)
        self.out.fillBranch("GEN_leadjet_pt", _gen_jets[0].pt if len(_gen_jets) > 0 else 0)
        return True
