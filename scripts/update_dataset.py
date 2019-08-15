import os, sys
import argparse
import logging
import pwd
import subprocess
import shutil
import time
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description='Famous Submitter')
    parser.add_argument("-i"   , "--input" , type=str, default="data.txt" , help="input datasets", required=True)

    options = parser.parse_args()

    with open(options.input, 'r') as stream:
        for sample in stream.read().split('\n'):
            if '#' in sample:
                continue
            if len(sample.split('/')) <= 1: continue

            #print colored("sample : " + sample, "red")

            sample_old = sample.split("/")[2]
            sample_tag = "RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017*"
            sample_tag = "RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017*"
            sample_files = subprocess.check_output(
                    [
                        'dasgoclient','--query',"dataset={}".format(
                            sample.replace(sample_old, sample_tag)
                        )
                    ]
            )
            #time.sleep(2)
            print colored(" - " + sample_files, "blue")


if __name__ == "__main__":
    main()

