import os, sys
import argparse
import glob
import logging
from termcolor import colored
import commands

logging.basicConfig(level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description='Famous Submitter')
    parser.add_argument("-i"   , "--input" , type=str, default="input"  , required=True)
    parser.add_argument("-t"   , "--tag"   , type=str, default="IronMan", required=True)
    parser.add_argument("-isMC", "--isMC"  , type=int, default=1          , help="")
    options = parser.parse_args()


    with open(options.input, 'r') as stream:
        for sample in stream.read().split('\n'):
            if '#' in sample: continue
            if len(sample.split('/')) <= 1: continue
            sample_name = sample.split("/")[1] if options.isMC else '_'.join(sample.split("/")[1:3])
            jobs_dir = '_'.join(['jobs', options.tag, sample_name])
            job_status = 0
            njobs = 0
            for file in list(glob.glob(jobs_dir + '/*.log')):
                jobid = os.path.basename(file).split('.log')
                if os.path.getsize(file.replace('.log', '.out')) == 0:
                    job_status += 1
                njobs += 1
            logging.info(
                "-- {:62s}".format((sample_name[:60] + '..') if len(sample_name)>60 else sample_name) +
                (
                    colored(" --> completed", "green") if job_status==0 else colored(
                        " --> ({}/{}) running".format(job_status,njobs), 'red'
                    )
                )
            )
if __name__ == "__main__":
    main()
