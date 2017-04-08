#!/bin/bash
wget -O ${PWD}/tests/test_local.py https://gist.githubusercontent.com/joshuacherry/d76b03d159f104eac986870e26722f74/raw
chmod +x ${PWD}/tests/test_local.py
${PWD}/tests/test_local.py
