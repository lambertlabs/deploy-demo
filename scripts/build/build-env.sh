#!/usr/bin/env bash

set -xe

apt-get update

echo Updating conda...
conda update conda

echo Building environment...
conda env update --name root -f environment.yml

# Install packages
apt-get install shellcheck
