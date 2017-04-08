#!/usr/bin/env python3
import yaml
# Requires: sudo apt-get install python3-pip -y && sudo pip3 install pyyaml
from subprocess import check_call, CalledProcessError
from collections import deque
import sys, os, subprocess

travisFile = os.path.join(os.path.dirname(__file__), '../.travis.yml')

def appendToQueue(cmd):
    cmd_queue.append('printf "\\n${green}Running Command: '+cmd+'${neutral}\\n"')
    cmd_queue.append(cmd)
    #cmd_queue.append('printf "\\n${yellow}The command \\"'+cmd+'\\" exited with $?.${neutral}\\n"')
def splitDistros(DictList, searchKey):
    returnList, remainderList = [], []
    for dictionary in DictList:
        for key in dictionary:
            if key == searchKey: returnList.append(dictionary)
            else: remainderList.append(dictionary)
    return returnList, remainderList


with open(travisFile, 'r') as stream:
    try:
        data = yaml.load(stream)
        envLists = splitDistros(data['env'], "distro")
        envDistroList = envLists[0]
        envVarList = envLists[1]
        #print (envDistroList)
        #print (envVarList)
        for distro in envDistroList:
            for key in distro:
                #print(distro)
                cmd_queue = deque()
                cmd_queue.append("export "+key+"="+distro[key])
                cmd_queue.append('set -e')
                cmd_queue.append("red='\033[0;31m'")
                cmd_queue.append("green='\033[0;32m'")
                cmd_queue.append("yellow='\033[0;33m'")
                cmd_queue.append("neutral='\033[0m'")

                for env in envVarList:
                    for key in env:
                        cmd_queue.append("export "+key+"="+env[key])
                try:
                    for cmd in data['script']:
                        appendToQueue(cmd)
                    for cmd in data['after_success']:
                        appendToQueue(cmd)
                    bash_script = "; ".join(cmd_queue)
                    #print('\n'+bash_script+'\n\n') #debugging
                    command = check_call(bash_script, shell=True)
                    #print ("\nTest: \033[0;32mpass\033[0m\nreturned: %s\n" % (str(command)))

                except yaml.YAMLError as exc:
                    print(exc)
                except CalledProcessError as e:
                    if e.returncode==127:
                        sys.exit("\033[0;31mprogram not found\033[0m")
                    elif e.returncode<=125:
                        sys.exit("\033[0;33m\'%s'\033[0m\nTest: \033[0;31mfailed\033[0m\nreturned code %d\n" % (cmd,e.returncode))
                    else:
                        sys.exit("\033[0;33m\'%s'\033[0m likely crashed, shell retruned code %d" % (cmd,e.returncode))
                except OSError as e:
                    sys.exit("failed to run shell: '%s'" % (str(e)))


    except yaml.YAMLError as exc:
        print(exc)
