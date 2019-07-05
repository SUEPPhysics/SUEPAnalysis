import os, sys
import argparse
import logging
import pwd
import subprocess
import shutil
import time
from termcolor import colored

logging.basicConfig(level=logging.DEBUG)

script_TEMPLATE = """#!/bin/bash

export X509_USER_PROXY={proxy}
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

cd {cmssw_base}/src/
eval `scramv1 runtime -sh`
echo
echo $_CONDOR_SCRATCH_DIR
cd   $_CONDOR_SCRATCH_DIR
echo
echo "... start job at" `date "+%Y-%m-%d %H:%M:%S"`
echo "----- directory before running:"
ls -lR .
echo "----- CMSSW BASE, python path, pwd:"
echo "+ CMSSW_BASE  = $CMSSW_BASE"
echo "+ PYTHON_PATH = $PYTHON_PATH"
echo "+ PWD         = $PWD"
echo "----- Found Proxy in: $X509_USER_PROXY"
python condor_Run2_proc.py --jobNum=$1 --isMC={ismc} --era={era} --infile=$2
echo "----- transfert output to eos :"
xrdcp -s -f tree_$1.root {eosdir}
echo "----- directory after running :"
ls -lR .
echo " ------ THE END (everyone dies !) ----- "
"""


condor_TEMPLATE = """
request_disk          = 10000000
executable            = {jobdir}/script.sh
arguments             = $(ProcId) $(jobid)
transfer_input_files  = {transfer_file}
output                = $(ClusterId).$(ProcId).out
error                 = $(ClusterId).$(ProcId).err
log                   = $(ClusterId).$(ProcId).log
initialdir            = {jobdir}
transfer_output_files = ""
+JobFlavour           = "{queue}"

queue jobid from {jobdir}/inputfiles.dat
"""

def main():
    parser = argparse.ArgumentParser(description='Famous Submitter')
    parser.add_argument("-i"   , "--input" , type=str, default="data.txt" , help="input datasets", required=True)
    parser.add_argument("-t"   , "--tag"   , type=str, default="IronMan"  , help="production tag", required=True)
    parser.add_argument("-isMC", "--isMC"  , type=int, default=1          , help="")
    parser.add_argument("-q"   , "--queue" , type=str, default="testmatch", help="")
    parser.add_argument("-e"   , "--era"   , type=str, default="2017"     , help="")
    parser.add_argument("-f"   , "--force" , action="store_true"          , help="recreate files and jobs")
    parser.add_argument("-s"   , "--submit", action="store_true"          , help="submit only")
    parser.add_argument("-dry" , "--dryrun", action="store_true"          , help="running without submission")
    parser.add_argument("--redo-proxy"     , action="store_true"          , help="redo the voms proxy")

    options = parser.parse_args()

    # Making sure that the proxy is good
    proxy_base = 'x509up_u{}'.format(os.getuid())
    home_base  = os.environ['HOME']
    proxy_copy = os.path.join(home_base,proxy_base)
    cmssw_base = os.environ['CMSSW_BASE']
    eosbase = "/eos/cms/store/group/phys_exotica/monoZ/{tag}/{sample}/"

    regenerate_proxy = False
    if not os.path.isfile(proxy_copy):
        logging.warning('--- proxy file does not exist')
        regenerate_proxy = True
    else:
        lifetime = subprocess.check_output(
            ['voms-proxy-info', '--file', proxy_copy, '--timeleft']
        )
        print lifetime
        lifetime = float(lifetime)
        lifetime = lifetime / (60*60)
        logging.info("--- proxy lifetime is {} hours".format(lifetime))
        if lifetime < 10.0: # we want at least 10 hours
            logging.warning("--- proxy has expired !")
            regenerate_proxy = True

    if regenerate_proxy:
        redone_proxy = False
        while not redone_proxy:
            status = os.system('voms-proxy-init -voms cms')
            if os.WEXITSTATUS(status) == 0:
                redone_proxy = True
        shutil.copyfile('/tmp/'+proxy_base,  proxy_copy)


    with open(options.input, 'r') as stream:
        for sample in stream.read().split('\n'):
            if '#' in sample: continue
            # check if dataset in catalog
            if options.isMC:
                if options.era=="2016":
                    from PhysicsTools.MonoZ.catalog_2016 import catalog
                elif options.era=="2017":
                    from PhysicsTools.MonoZ.catalog_2017 import catalog
                elif options.era=="2017":
                    from PhysicsTools.MonoZ.catalog_2018 import catalog
                else:
                    raise "Era not reconised! only 2016, 2017 and 2018 are supported."
                if not any(sample in s for s in catalog.keys()):
                    logging.warning(colored('dataset not found: {}, skipped...'.format(sample), "red"))
                    continue
            if len(sample.split('/')) <= 1: continue
            sample_name = sample.split("/")[1] if options.isMC else '_'.join(sample.split("/")[1:3])
            jobs_dir = '_'.join(['jobs', options.tag, sample_name])
            logging.info("-- sample_name : " + sample)

            if os.path.isdir(jobs_dir):
                if not options.force:
                    logging.error(" " + jobs_dir + " already exist !")
                    continue
                else:
                    logging.warning(" " + jobs_dir + " already exists, forcing its deletion!")
                    shutil.rmtree(jobs_dir)
                    os.mkdir(jobs_dir)
            else:
                os.mkdir(jobs_dir)

            if not options.submit:
                # ---- getting the list of file for the dataset
                sample_files = subprocess.check_output(
                    ['dasgoclient','--query',"file dataset={}".format(sample)]
                )
                time.sleep(15)
                with open(os.path.join(jobs_dir, "inputfiles.dat"), 'w') as infiles:
                    infiles.write(sample_files)
                    infiles.close()
            time.sleep(10)
            eosoutdir =  eosbase.format(tag=options.tag,sample=sample_name)
            # crete a directory on eos
            if '/eos/cms' in eosoutdir:
                eosoutdir = eosoutdir.replace('/eos/cms', 'root://eoscms.cern.ch/')
                os.system("eos mkdir -p {}".format(eosoutdir.replace('root://eoscms.cern.ch/','')))
            else:
                raise NameError(eosoutdir)

            with open(os.path.join(jobs_dir, "script.sh"), "w") as scriptfile:
                script = script_TEMPLATE.format(
                    proxy=proxy_copy,
                    cmssw_base=cmssw_base,
                    ismc=options.isMC,
                    era=options.era,
                    eosdir=eosoutdir
                )
                scriptfile.write(script)
                scriptfile.close()

            with open(os.path.join(jobs_dir, "condor.sub"), "w") as condorfile:
                condor = condor_TEMPLATE.format(
                    transfer_file= ",".join([
                        "../condor_Run2_proc.py",
                        "../combineHLT_Run2.yaml",
                        "../keep_and_drop.txt",
                        "../Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
                        "../Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt",
                        "../Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
                        "../haddnano.py"
                    ]),
                    jobdir=jobs_dir,
                    queue=options.queue
                )
                condorfile.write(condor)
                condorfile.close()
            if options.dryrun:
                continue

            htc = subprocess.Popen(
                "condor_submit " + os.path.join(jobs_dir, "condor.sub"),
                shell  = True,
                stdin  = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                close_fds=True
            )
            out, err = htc.communicate()
            exit_status = htc.returncode
            logging.info("condor submission status : {}".format(exit_status))

if __name__ == "__main__":
    main()
