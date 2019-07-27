#!/bin/bash
ifconfig wlan1 down
sleep 1
ifconfig wlan0 down
sleep 1
iwconfig wlan1 mode monitor
sleep 1
airodump-ng wlan1