#!/usr/bin/env python3
import yaml
# Requires: sudo apt-get install python3-pip -y && sudo pip3 install pyyaml
from subprocess import check_call, CalledProcessError
import sys, os

travisFile = os.path.join(os.path.dirname(__file__), '../.travis.yml')

with open(travisFile, 'r') as stream:
    try:
        data = yaml.load(stream)
        for cmd in data['script']:
            command = check_call(cmd, shell=True)
            print ("\033[0;33m\'%s'\033[0m\nTest: \033[0;32mpass\033[0m\nreturned: %s\n" % (cmd,str(command)))
        for cmd in data['after_success']:
            command = check_call(cmd, shell=True)
            print ("\033[0;33m\'%s'\033[0m\nTest: \033[0;32mpass\033[0m\nreturned: %s\n" % (cmd,str(command)))


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
