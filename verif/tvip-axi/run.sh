#!/usr/bin/env bash
curdir=`pwd`
git clone https://github.com/taichi-ishitani/tvip-axi
cd ./tvip-axi
./setup_submodules.sh
cd ./sample/work
python ../../../../common/setenv/eda.py make
python ../../../../common/setenv/eda.py make SIMULATOR=xcelium
cd ${curdir}
