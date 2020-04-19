#!/bin/bash

echo "hello, Master!"
echo " bring down wlan0"
ifconfig wlan0 down
sleep 3

echo "setting Region to Bolivia"
iw reg set BO
sleep 3

echo "setting TxPower to 30"
iwconfig wlan0 txpower 30
sleep 2

echo "starting wlan0"
ifconfig wlan0 up 
echo "putting wlan0 up"
iwconfig
sleep 5


echo "                                   "
echo "                 BY                "
echo "       =======================     "
echo "               0rg1sm              "
echo "       =======================     "
echo "                                   "
echo "                                   "
