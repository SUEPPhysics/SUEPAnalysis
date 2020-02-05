import ROOT
import sys, os
import numpy as np
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

ROOT.PyConfig.IgnoreCommandLineOptions = True


class ADDWeightProducer(Module):
    def __init__(self, MD=100, do_syst=False, syst_var=''):
        self.do_syst = do_syst
        self.syst_var = syst_var
	self.MD = MD
        if self.syst_var !='':
            self.syst_suffix = '_sys_' + syst_var if do_syst else ''
        else:
            self.syst_suffix = syst_var


    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("ADDWeight"    , "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def analyze(self, event):
        # EW correction
        gen_part = Collection(event, "GenPart")
        fq1 = abs(gen_part[0].pdgId)
        fq2 = abs(gen_part[1].pdgId)

        if ( (fq1>=1 and fq1<=6) or fq1==21 ):
            q1 = ROOT.TLorentzVector( 0, 0, 100., 100. )
        else:
            print "[WARNING] MonoZ/ADDcorrection, GenParticle element 0 is neither a quark nor a gluon. weight set to 1"
            self.out.fillBranch("ADDWeight"    , 1)
            return True
        if ( (fq2>=1 and fq2<=6) or fq2==21 ):
            q2 = ROOT.TLorentzVector( 0, 0, -100., 100. )
        else:
            print "[WARNING] MonoZ/ADDcorrection, GenParticle element 1 is neither a quark nor a gluon. weight set to 1"
            self.out.fillBranch("ADDWeight"    , 1)
            return True
        if ( gen_part[2].pdgId==5000039 or gen_part[2].pdgId==23 ):
            v1 = gen_part[2].p4()
        else:
            print "[WARNING] MonoZ/ADDcorrection, GenParticle element 2 is neither Z quark nor Graviton. weight set to 1"
            self.out.fillBranch("ADDWeight"    , 1)
            return True

        if ( gen_part[3].pdgId==5000039 or gen_part[3].pdgId==23):
            v2 = gen_part[3].p4()
        else:
            print "[WARNING] MonoZADDcorrection, GenParticle element 3 is neither Z quark nor Graviton. weight set to 1"
            self.out.fillBranch("ADDWeight"    , 1)
            return True

	print v1.M(),v2.M()
        # Z and graviton center of mass
	print "the first particle is:    ",gen_part[0].pdgId, "    the second particle is:    ", gen_part[1].pdgId
        vv = v1 + v2
        shat = vv.Mag()/1000
	shat = shat**2
	ADDweight = 1
	MD=self.MD
	print "the shat is:   ", shat, "    and the MD is:   ", MD**2, "    the ratio is:   ", MD**2/shat
 	if shat > MD**2:
		ADDweight = MD**4/shat**2
		print "making ADD weights now" 
        self.out.fillBranch("ADDWeight", ADDweight)
        return True

