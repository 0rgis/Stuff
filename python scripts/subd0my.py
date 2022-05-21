#python 3
#subdomain scanner V1.5b

import requests
#print("   ___            _      ")
#print("  / _ \ _ __ __ _/ |___  ")
#print(" | | | | '__/ _` | / __| ")
#print(" | |_| | | | (_| | \__ \ ")
#print("  \___/|_|  \__, |_|___/ ")
#print("            |___/        ")
#print("")
#print("")
print("")
print ("subd0my (V1.5b), Sub Domain Scanner by 0rgis")
print ("")
print ("")
print ("!!!! MAKE SURE INPUT FILE IS IN WORKING DIRECTORY !!!!")
print ("")
print ("")

#the domain to scan for subdomains
domain = input ("Enter Domain Name: ")
#domain = "google.com" #use user input
print ("")
# read all subdomains (from subdomain list, place in same folder)
print ("")
list = input("Enter List Name : ")
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
        print("[+] Discovered subdomain:", url)
        # create a new text file#
        #text_file = open("results.txt", "a")
        # write to this file some text#
        #text_file.write(url)



print ("")
print ("To Do List")
print ("    - output to file")
print ("    - port scan")
print ("")
