#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
print("\033[1;30;40m           _         _  ___                  ")
print("\033[1;30;40m ___ _   _| |__   __| |/ _ \ _ __ ___  _   _ ")
print("\033[1;30;40m/ __| | | | '_ \ / _` | | | | '_ ` _ \| | | |")
print("\033[1;30;40m\__ \ |_| | |_) | (_| | |_| | | | | | | |_| |")
print("\033[1;30;40m|___/\__,_|_.__/ \__,_|\___/|_| |_| |_|\__, |")
print("\033[1;30;40m                                        |___/")
print("")
print("")
print("")
print("")
print("\033[1;31;40m!!!! MAKE SURE INPUT FILE IS IN WORKING DIRECTORY !!!!")
print("")
print("")

#the domain to scan for subdomains
domain = input ("\033[1;34;40mDomain Name :\033[1;37;40m ")
# read all subdomains (from subdomain list, place in same folder)
list = input("\033[1;34;40mWordList Name :\033[1;37;40m ")
print ("")
file = open(list)#file must be in same folderrere
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()

#brute forcing the sub doms

for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print("\033[1;32;40m[+] Discovered subdomain: \n", url)
        # create a new text file#
        text_file = open("results.txt", "a")
        # write to this file some text#
        text_file.write(url)

print ("")

