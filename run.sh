#!/bin/bash

# Ativar virtualenV
# NÃO ALTERE SE NÃO SOUBER O QUE ESTÁ FAZENDO
source .brasilio/venv/bin/activate

# Ativar debug
set -x

cd src
python capture.py