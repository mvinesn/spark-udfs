#!/bin/bash

PROJECT_NAME=$(basename $(dirname $PWD))
source `which virtualenvwrapper.sh`
mkvirtualenv $PROJECT_NAME

set -euo pipefail

ln -s ~/.virtualenvs/$PROJECT_NAME pyenv
pip install wheel
pip install -r requirements.txt