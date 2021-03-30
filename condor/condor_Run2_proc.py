import os, sys, re
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import yaml

#Import the NanoAOD-tools that we will need
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme import jetRecalib
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.JetSysColl import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *

#Import the SUEP analysis tools
from PhysicsTools.SUEP.SUEPProducer import *
from PhysicsTools.SUEP.GenWeightProducer import *
from PhysicsTools.SUEP.PhiXYCorrection import *
import argparse

parser = argparse.ArgumentParser("")
parser.add_argument('-isMC'   , '--isMC'   , type=int, default=1     , help="")
parser.add_argument('-jobNum' , '--jobNum' , type=int, default=1     , help="")
parser.add_argument('-era'    , '--era'    , type=str, default="2018", help="")
parser.add_argument('-doSyst' , '--doSyst' , type=int, default=1     , help="")
parser.add_argument('-infile' , '--infile' , type=str, default=None  , help="")
parser.add_argument('-dataset', '--dataset', type=str, default="X"   , help="")
parser.add_argument('-nevt'   , '--nevt'   , type=str, default=-1    , help="")
parser.add_argument('-json'   , '--json'   , type=str, default=None  , help="")

options  = parser.parse_args()

def inputfile(nanofile):
   tested   = False
   forceaaa = False
   pfn=os.popen("edmFileUtil -d %s"%(nanofile)).read()
   pfn=re.sub("\n","",pfn)
   print (nanofile," -> ",pfn)
   if (os.getenv("GLIDECLIENT_Group","") != "overflow" and
       os.getenv("GLIDECLIENT_Group","") != "overflow_conservative" and not
       forceaaa ):
      if not tested:
         print ("Testing file open")
         testfile=ROOT.TFile.Open(pfn)
         if testfile and testfile.IsOpen() :
            print ("Test OK")
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

print ("---------------------------")
print (" -- options  = ", options)
print (" -- is MC    = ", options.isMC)
print (" -- jobNum   = ", options.jobNum)
print (" -- era      = ", options.era)
print (" -- in file  = ", options.infile)
print (" -- dataset  = ", options.dataset)
print ("---------------------------")

xsection = 1.0
dataset = "QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8+RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1+MINIAODSIM"
condtag_ = "SUEP_QCD"

if options.isMC:
   with open(os.path.dirname(__file__) +'../data/xsections_{}.yaml'.format(options.era)) as file:
       MC_xsecs = yaml.full_load(file)
   try:
       xsection *= MC_xsecs[dataset]["xsec"]
       xsection *= MC_xsecs[dataset]["kr"]
       xsection *= MC_xsecs[dataset]["br"]
       print("The dataset name: ", dataset)
       print("The xsection: ", xsection)
   except:
       print("WARNING: I did not find the xsection for that MC sample. Check the dataset name and the relevant yaml file")


pre_selection = "(Sum$(Jet_pt>500) >= 1) && (HLT_PFHT1050 || HLT_PFJet500)"
if float(options.nevt) > 0:
   print (" passing this cut and : ", options.nevt)
   pre_selection += ' && (Entry$ < {})'.format(options.nevt)

modules_era = [ GenWeightProducer( isMC = options.isMC, xsec = xsection, dopdf =  True) ]

pro_syst = []
ext_syst = []


if options.isMC:
   if options.era=="2016":
      modules_era.append(puAutoWeight_2016())
      modules_era.append(PrefCorr())
      modules_era.append(jetmetUncertainties2016All())
      modules_era.append(btagSFProducer("Legacy2016", "deepcsv"))
      modules_era.append(muonScaleRes2016())
      modules_era.append(lepSF_2016())
      ext_syst.append("PrefireWeight")
   if options.era=="2017":
      modules_era.append(puAutoWeight_2017())
      modules_era.append(PrefCorr())
      modules_era.append(jetmetUncertainties2017All())
      modules_era.append(btagSFProducer("2017", "deepcsv"))
      modules_era.append(muonScaleRes2017())
      modules_era.append(lepSF_2017())
      ext_syst.append("PrefireWeight")
   if options.era=="2018":
      modules_era.append(puAutoWeight_2018())
      modules_era.append(jetmetUncertainties2018All())
      modules_era.append(btagSFProducer("2018", "deepcsv"))
      modules_era.append(muonScaleRes2018())
      modules_era.append(lepSF_2018())

   modules_era.append(PhiXYCorrection(era=options.era,isMC=options.isMC,sys=''))
   modules_era.append(SUEPProducer(isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))

   # for shift-based systematics
   for sys in pro_syst:
      for var in ["Up", "Down"]:
          if "jesTotal" in sys and options.doSyst==1: modules_era.append(PhiXYCorrection(era=options.era,isMC=options.isMC,sys=sys+var))
          if "jer" in sys and options.doSyst==1: modules_era.append(PhiXYCorrection(era=options.era,isMC=options.isMC,sys=sys+var))
          modules_era.append(SUEPProducer(isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=sys+var))

else:
   print ("sample : ", options.dataset, " candtag : ", condtag_)

   print (" -- era : ",)
   if options.era=="2016":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2016%s' % condtag_.split(options.era)[1][:1])() )
   if options.era=="2017":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2017%s' % condtag_.split(options.era)[1][:1])() )
   if options.era=="2018":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2018%s' % condtag_.split(options.era)[1][:1])() )

   modules_era.append(PhiXYCorrection(era=options.era,isMC=options.isMC,sys=''))
   modules_era.append(SUEPProducer  (isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))

   if options.era=="2016":
       options.json = "Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt"
   if options.era=="2017":
       options.json = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
   if options.era=="2018":
       options.json = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
   print ("---- JSON used is : ", options.json)


for i in modules_era:
   print ("modules : ", i)

print ("Selection : ", pre_selection)

p = PostProcessor(
   ".", [options.infile],
   cut=pre_selection,
   branchsel="keep_and_drop.txt",
   outputbranchsel="keep_and_drop_post.txt",
   haddFileName="tree_%s.root" % str(options.jobNum),
   modules=modules_era,
   provenance=True,
   noOut=False,
   fwkJobReport=True,
   jsonInput=options.json
)
p.run()
