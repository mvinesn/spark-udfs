#!/bin/bash

python3 -m venv ./pyenv

source ./pyenv/bin/activate

pip install wheel
pip install -r requirements.txt