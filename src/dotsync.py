#!/usr/bin/env python

#This is dotsync.
#A script allowing a user to sync their dot files between computers or to upload them to a server.
#This script is the client version of the script, it is used to send files and can be used to receive files too.

import sys
import subprocess
import socket
from receive import receive
from send import send

#address #the var to contain the address
files = [] #the list to contain all the file names

if sys.argv[1] == '-r':
    length = len(sys.argv)
    if length < 3: #if there is no files following the option, the error.
       print("Missing argument after -r")
       sys.exit()
    
    for x in range(1, (len(sys.argv) - 1)): #add all the file names following to the list.
        files.append(sys.argv[x+1])
    receive()
    sys.exit()

if sys.argv[1] == '-s':
    length = len(sys.argv)
    if length < 3:
       print("Missing argument after -s")
       sys.exit()
    address = sys.argv[2] #let address = the address entered through commanf line args.
    for x in range(1, (len(sys.argv) - 2)): #add all the file names to a list.
        files.append(sys.argv[x+2])
    send(files, sys.argv[2])
    sys.exit()

else:
    print("dotsync [options] [address] [file]")
    print("-r           Set to receive files from another computer which is activly sending")
    print("-s           Set to send files to an external computer or server which is activly looking to receive.")
    print("-g           Get files from remote server")
    print("[address]    The address either of the server to receive from, or computer or server to send too. This is not required if receiving from another computer")




