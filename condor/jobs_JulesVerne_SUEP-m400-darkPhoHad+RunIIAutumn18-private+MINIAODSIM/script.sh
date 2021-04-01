#!/bin/bash

export X509_USER_PROXY=/home/freerc/x509up_u516
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc820

wget http://t3serv001.mit.edu/~freerc/CMSSW_10_6_4.tgz
tar -xf CMSSW_10_6_4.tgz
rm CMSSW_10_6_4.tgz
cd CMSSW_10_6_4/src/
scramv1 b ProjectRename
eval `scramv1 runtime -sh` 
export PYTHONPATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/external/slc7_amd64_gcc820/bin/python
echo 
echo $_CONDOR_SCRATCH_DIR 
cd   $_CONDOR_SCRATCH_DIR 
echo 
echo "... start job at" `date "+%Y-%m-%d %H:%M:%S"`
echo "----- directory before running:"
pwd
ls -lR .
echo "----- CMSSW BASE, python path, pwd:"
echo "+ CMSSW_BASE  = $CMSSW_BASE"
echo "+ PYTHON_PATH = $PYTHON_PATH"
echo "+ PWD         = $PWD"
echo "----- Found Proxy in: $X509_USER_PROXY"
python condor_Run2_proc.py --jobNum=$1 --isMC=1 --era=2018 --dataset=SUEP-m400-darkPhoHad+RunIIAutumn18-private+MINIAODSIM --infile=$2
echo "----- transfering output to scratch :"
mv tree_$1.root /mnt/hadoop/scratch/freerc/SUEP
echo "----- directory after running :"
ls -lR .
echo " ------ THE END (everyone dies !) ----- "
