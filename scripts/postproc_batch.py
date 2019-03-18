import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.monoZ.MonoZProducer import *
from PhysicsTools.NanoAODTools.postprocessing.monoZ.GenMonoZProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetRecalib import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.mht import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import *
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

import argparse


isMC = True
era = "2017"
dataRun = ""

parser = argparse.ArgumentParser("")
parser.add_argument('-inputs', '--inputs', type=str, default ="", help="")
parser.add_argument('-isMC', '--isMC', type=int, default=1, help="")
parser.add_argument('-jobNum', '--jobNum', type=int, default=1, help="")
parser.add_argument('-era', '--era', type=str, default="2017", help="")
parser.add_argument('-doSyst', '--doSyst', type=int, default=0, help="")
parser.add_argument('-dataRun', '--dataRun', type=str, default="X", help="")

options  = parser.parse_args()
print(" -- options = ", options)
isMC = options.isMC
era = options.era
dataRun = options.dataRun

print("isMC = ", isMC, "era = ", era, "dataRun = ", dataRun)

pre_selection = " || ".join([
    "(Sum$(Electron_pt > 20) >= 2)",
    "(Sum$(Muon_pt > 20) >= 2)",
    "(Sum$(Muon_pt > 20 && Muon_tightId) >= 1)"
])

modules_2017 = [
    #puAutoWeight(),
    muonScaleRes2017(),
    #btagSFProducer("2017", "deepcsv"),
    #GenMonoZProducer(),
    MonoZProducer(options.isMC, str(options.era))
]

if options.isMC:
   modules_2017.insert(0, puAutoWeight())
   modules_2017.insert(1, GenMonoZProducer())
   modules_2017.insert(2, btagSFProducer("2017", "deepcsv"))   

if options.doSyst:
    modules_2017.insert(
        0, jetmetUncertainties2017All()
    )
    modules_2017.insert(
        1, MonoZProducer(
            isMC=options.isMC, era=str(options.era),
            do_syst=options.doSyst, syst_var='jesTotalUp'
        )
    )
    modules_2017.insert(
        2, MonoZProducer(
            isMC=options.isMC, era=str(options.era),
            do_syst=options.doSyst, syst_var='jesTotalDown'
        )
    )

p = PostProcessor(
    ".", [options.inputs], 
    cut=pre_selection,
    branchsel="keep_and_drop.txt",
    outputbranchsel="keep_and_drop.txt",
    modules=modules_2017,
    provenance=True,
    noOut=False,
    fwkJobReport=True
)

p.run()
