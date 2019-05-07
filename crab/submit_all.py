import sys, os
import argparse

crab_template = """
import sys
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = '{JOBNAME}'
config.General.workArea        = '/afs/cern.ch/user/y/yhaddad/work/MonoZ/crab/'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.pluginName      = 'Analysis'
config.JobType.psetName        = 'PSet.py'
config.JobType.scriptExe       = 'crab_script.sh'

config.JobType.scriptArgs=['isMC={ISMC}','era=2017','doSyst=0','dataset={DATASETARG}','catalog=catalogue_2017.yaml']
config.JobType.inputFiles=['../scripts/keep_and_drop.txt','../scripts/drop_all.txt','../scripts/postproc.py','../scripts/haddnano.py', '../data/combineHLT_2017.yaml']
config.JobType.sendPythonFolder	       = True

config.Data.inputDataset               = '{DATASET}'
config.Data.inputDBS                   = 'global'
config.Data.splitting                  = 'FileBased'
# config.Data.lumiMask                   = '../data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
config.Data.unitsPerJob                = 1
config.Data.outLFNDirBase              = '/store/group/phys_exotica/monoZ/MonoZAnalysis_{OUTPUTTAG}/'
config.Data.publication                = False
config.Data.outputDatasetTag           = '{OUTPUTTAG}'
config.Data.allowNonValidInputDataset  = True

config.JobType.allowUndistributedCMSSW = True
config.Site.storageSite                = 'T2_CH_CERN'
# config.Site.blacklist = ['T2_US_Caltech','T1_DE_KIT','T1_RU_JINR','T2_US_Wisconsin',"T1_DE_KIT"]
# config.Site.blacklist = ["T1_DE_KIT", "T2_US_Wisconsin", "T2_US_Caltech", "T2_US_Nebraska", "T2_US_Vanderbilt"]
"""


parser = argparse.ArgumentParser()
parser.add_argument("-i"   , "--inputs", type=str, default="data.txt", help="")
parser.add_argument("-isMC", "--isMC"  , type=int, default=1         , help="")

options = parser.parse_args()
proc_args = [ "'isMC=%i'" % options.isMC, "'era=2017'", "'doSyst=0'", "'dataRun=X'"]
print(" configuration :", options.inputs )
with open(options.inputs, 'r') as stream:
    for sample in stream.read().split('\n'):
        if '#' in sample: continue
	if len(sample.split('/')) <= 1: continue

	tag = sample.split("/")[1]
	if not options.isMC:
		tag = sample.split("/")[1] + "_" + sample.split("/")[2]
	crab_config = crab_template.replace("{JOBNAME}", "Paprika_" + tag)
	if options.isMC:
		crab_config = crab_config.replace("{DATASETARG}", 'X')
	else:
		crab_config = crab_config.replace("{DATASETARG}", sample)
        crab_config = crab_config.replace("{DATASET}", sample)
        crab_config = crab_config.replace("{ISMC}", str(options.isMC) )
        crab_config = crab_config.replace("{OUTPUTTAG}", "Paprika_MonoZ_2017")
        if not options.isMC:
	 	crab_config = crab_config.replace("# config.Data.lumiMask", "config.Data.lumiMask")
	crab_file = "job_submit_%s.py" % tag
        os.system("rm -f " +  crab_file)
	with open(crab_file, 'a') as the_file:
    		the_file.write(crab_config)

        cmd = "crab submit " + crab_file
        print cmd
        os.system(cmd)
