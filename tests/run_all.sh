#!/bin/bash

set -e
ROOT_PATH=$(cd $(dirname "$0");cd ../; pwd)
export PYTHONPATH="${ROOT_PATH}/src"
echo "${PYTHONPATH}"
python -m unittest discover
