#!/bin/bash

cd openttd-sans
bash build.sh
cd ..

cd openttd-serif
bash build.sh
cd ..

cd openttd-small
bash build.sh
cd ..

cd openttd-mono
bash build.sh
cd ..

python3 checkOpenTTDStrings.py ../openttd/src/lang
