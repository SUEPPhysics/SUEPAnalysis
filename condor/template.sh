#!/bin/bash
echo
export X509_USER_PROXY=/afs/cern.ch/user/y/yhaddad/x509up_u17147
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

cd /afs/cern.ch/user/y/yhaddad/work/CMSSW_9_4_9/src/
eval `scramv1 runtime -sh`
echo
echo ${_CONDOR_SCRATCH_DIR}
cd   ${_CONDOR_SCRATCH_DIR}
echo
echo "... start job at" `date "+%Y-%m-%d %H:%M:%S"`
echo "----- directory before running:"
ls -lR .
echo "----- CMSSW BASE, python path, pwd:"
echo "+ CMSSW_BASE  = $CMSSW_BASE"
echo "+ PYTHON_PATH = $PYTHON_PATH"
echo "+ PWD         = $PWD"
echo "----- Found Proxy in: $X509_USER_PROXY"
python condor_proc.py --jobNum=$1 --isMC=0 --era=2017 --infile=$2
echo "----- transfert output to eos :"
xrdcp -s tree_$1.root root://eoscms.cern.ch//store/group/phys_exotica/monoZ/condortest/
echo "----- directory after running :"
ls -lR .
echo "----- checking if eos is mounted : "
ls -lR  /eos/cms/store/group/phys_exotica/monoZ/condortest/
echo " ------ THE END (everyone dies !) ----- "
