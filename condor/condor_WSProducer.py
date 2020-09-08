import os, sys, re
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import yaml
#Import the NanoAOD-tools that we will need
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.MonoZ.MonoZWSProducer import *

import argparse

parser = argparse.ArgumentParser("")
parser.add_argument('-isMC'   , '--isMC'   , type=int, default=1     , help="")
parser.add_argument('-jobNum' , '--jobNum' , type=int, default=1     , help="")
parser.add_argument('-era'    , '--era'    , type=str, default="2018", help="")
parser.add_argument('-doSyst' , '--doSyst' , type=int, default=1     , help="")
parser.add_argument('-infile' , '--infile' , type=str, default=None  , help="")
parser.add_argument('-dataset', '--dataset', type=str, default="X"   , help="")

options  = parser.parse_args()

def inputfile(nanofile):
   tested   = False
   forceaaa = False
   pfn=os.popen("edmFileUtil -d %s"%(nanofile)).read()
   pfn=re.sub("\n","",pfn)
   print nanofile," -> ",pfn
   if (os.getenv("GLIDECLIENT_Group","") != "overflow" and
       os.getenv("GLIDECLIENT_Group","") != "overflow_conservative" and not
       forceaaa ):
      if not tested:
         print "Testing file open"
         testfile=ROOT.TFile.Open(pfn)
         if testfile and testfile.IsOpen() :
            print "Test OK"
            nanofile=pfn
            testfile.Close()
         else:
            if "root://cms-xrd-global.cern.ch/" not in nanofile:
               nanofile = "root://cms-xrd-global.cern.ch/" + nanofile
            forceaaa=True
      else:
         nanofile = pfn
   else:
       if "root://cms-xrd-global.cern.ch/" not in nanofile:
          nanofile = "root://cms-xrd-global.cern.ch/" + nanofile
   return nanofile

options.infile = inputfile(options.infile)

print "---------------------------"
print " -- options  = ", options
print " -- is MC    = ", options.isMC
print " -- jobNum   = ", options.jobNum
print " -- era      = ", options.era
print " -- in file  = ", options.infile
print " -- dataset  = ", options.dataset
print "---------------------------"

if options.isMC:
   condtag_ = "NANOAODSIM"
   if options.dataset == "X":
      options.dataset = options.infile
      options.dataset = options.dataset.split('/store')[1].split("/")
      condtag_ = options.dataset[5]
      options.dataset = options.dataset[3]
   print "[check] condtag_ == ", condtag_
   print "[check] dataset  == ", options.dataset
else:
   if options.dataset == "X":
      options.dataset = options.infile
      options.dataset = options.dataset.split('/store')[1].split("/")
      condtag_ = options.dataset[2]
      options.dataset = options.dataset[3]
   else:
      options.dataset = options.dataset.split("/")
      condtag_ = options.dataset[2]
      options.dataset = options.dataset[1]


pro_syst = [ "ElectronEn", "MuonEn", "jesTotal", "jer"]
ext_syst = [ "puWeight", "PDF", "MuonSF", "ElecronSF", "EWK", "nvtxWeight","TriggerSFWeight","btagEventWeight", "QCDScale0w", "QCDScale1w", "QCDScale2w"]

modules_era   = []

#Do the nom and the data
modules_era.append(MonoZWSProducer(
    isMC=options.isMC, era=int(options.era),
    do_syst=1, syst_var='', sample=options.dataset
))

#Do the systematic variations
if options.isMC:
   for sys in pro_syst:
      for var in ["Up", "Down"]:
         modules_era.append(MonoZWSProducer(options.isMC, str(options.era), do_syst=1,
                                            syst_var=sys+var, sample=options.dataset))
   
   for sys in ext_syst:
      for var in ["Up", "Down"]:
         modules_era.append(
            MonoZWSProducer(
               options.isMC, str(options.era),
               do_syst=1, syst_var=sys+var,
               weight_syst=True,
               sample=options.dataset
            )
         )

p = PostProcessor(
   ".", [options.infile],
   cut="",
   outputbranchsel="keep_and_drop_WS.txt",
   haddFileName="WS_tree_%s.root" % str(options.jobNum),
   modules=modules_era,
   provenance=True,
   noOut=False,
   fwkJobReport=True,
   jsonInput=None
)
p.run()

