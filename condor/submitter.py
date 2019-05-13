import os,sys

from Queue import Queue
from multiprocessing import cpu_count
from threading import Thread, Semaphore
import threading
import subprocess

condor_template = """
universe              = {queue}
requirements          = (Arch == "X86_64") && (OpSys == "LINUX")
# request_disk          = 10000000
executable            = {exename}
# transfer_input_files  = {files_to_transfer}
output                = {jobdir}/$(jobid).out
error                 = {jobdir}/$(jobid).err
log                   = {jobdir}/$(jobid).log
Should_Transfer_Files = YES
initialdir            = {outputdir}
WhenToTransferOutput  = ON_EXIT
want_graceful_removal = true
max_retries = 1

queue jobid from {jobids_file}
"""

script_template = """
#!/bin/bash
echo
export X509_USER_PROXY={PROXY}
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
"""

class Submitter(object):
    def __init__(self, queue=None, name="job", jobdriver=None, maxthreads=500):
        self.returned = Queue()
        self.jobdriver = jobdriver
        self.njobs = 0
        self.jobs = Queue()
        self.queue = queue
        self.name = name
        self.sem = Semaphore()
        self.maxthreads = maxthreads
        if self.queue:
            self.running = Queue()
        else:
            self.running = Queue(cpu_count())

        if not self.jobdriver:
            self.jobdriver = CondorJob

    def run(self, cmd, args, name=None):
        myargs = [cmd, args]
        if name:
            myargs.append(name)

        wrap = Wrap(self, myargs, self.returned, self.running)
        while threading.activeCount() > self.maxthreads:
            sleep(0.05)

        ret = (None,(None,None))
        if not self.queue:
            thread = Thread(None, wrap)
            thread.start()
        else:
            ret = wrap(interactive=True)

        self.sem.acquire()
        self.njobs += 1
        self.sem.release()

        return ret

    def jobid(self):
        self.sem.acquire()
        ret = self.jobId
        self.jobId += 1
        self.sem.release()
        return ret

    def __call__(self,cmd, args, interactive, name=None):

        if type(cmd) == str or type(cmd) == unicode:
            ## print cmd
            cmd = "%s %s" % (cmd, " ".join(args) )
            args = (cmd,)
            if self.queue and not interactive:
                if not name:
                    jobname = "%s%d" % (self.name, self.jobid())
                cmd = self.jobdriver(self.queue,name)
            else:
                cmd = commands.getstatusoutput

        ret = cmd( *args )
        if self.queue and not interactive:
            self.jobs.put(cmd)
        return cmd,args,ret




class CondorJob(object):
    def __init__(self, queue, name, outputdir="."):
        self.queue = queue
        self.name = name
        self.cfgname = name + '.sub'
        self.exename = name + '.sh'
        self.transfile = None

    def __call__(self, command):
        script  = ""
        script += "#!/bin/bash\n"
        script += command + "\n"
        return self.run(script)

    def run(self, script):
        logdir = os.path.dirname(self.name)
        if not os.path.exists(self.name):
            os.mkdir(self.name)

        self.outputdir =  "./" + self.name
        print "--- script-----"
        print script
        print "---------------"
        with open(self.exename, "w+") as fout:
            fout.write(script)
            fout.close()

        with open(self.cfgname, "w+") as fout:
            condor_sub = condor_template.format(
                queue       = self.queue,
                exename     = os.path.abspath(self.exename),
                jobdir      = self.name,
                outputdir   = self.outputdir,
                jobids_file = 0,
                files_to_transfer = self.transfile if self.transfile else ''
            )
            fout.write(condor_sub)
            fout.close()

        htc = subprocess.Popen(
            "cat " + self.cfgname,
            shell  = True,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            close_fds=True
        )

        out, err = htc.communicate()
        self.exit_status = htc.returncode

        if self.exit_status != 0:
            print out
            print err
        else:
            self.jobid = None
            for line in out.split('\n'):
                if 'cluster' in line:
                    self.jobid = int(line.replace('.','').split()[-1])
                    break
        return self.exit_status
