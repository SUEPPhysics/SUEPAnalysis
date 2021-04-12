#!/bin/bash

export X509_USER_PROXY=/home/freerc/x509up_u516
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc820
export HOME=.

wget http://t3serv001.mit.edu/~freerc/CMSSW_10_6_4.tgz
tar -xf CMSSW_10_6_4.tgz
rm CMSSW_10_6_4.tgz
cd CMSSW_10_6_4/src/
scramv1 b ProjectRename
eval `scramv1 runtime -sh` 
cd -

echo $_CONDOR_SCRATCH_DIR 
cd   $_CONDOR_SCRATCH_DIR 

echo "----- Found Proxy in: $X509_USER_PROXY"
echo "python condor_Run2_proc.py --jobNum=$1 --isMC=1 --era=2018 --dataset=SUEP-m400-darkPhoHad+RunIIAutumn18-private+MINIAODSIM --infile=$2"
python condor_Run2_proc.py --jobNum=$1 --isMC=1 --era=2018 --dataset=SUEP-m400-darkPhoHad+RunIIAutumn18-private+MINIAODSIM --infile=$2
rm tmp.root

echo "----- transferring output to scratch :"
mv tree_$1.root /mnt/hadoop/scratch/freerc/SUEP/LeaguesUnderTheSea/SUEP-m400-darkPhoHad+RunIIAutumn18-private+MINIAODSIM/
echo "----- directory after running :"
echo " ------ THE END (everyone dies !) ----- "
