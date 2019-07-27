#!/bin/bash
cd tools/nipe
sleep 1
perl nipe.pl start
sleep 1
perl nipe.pl status
sleep 1
echo "connected to TOR!!"
