import sys
import socket
import time
import os
import getpass

path = [] #list to hold file paths

def handshake(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
    s.bind((address,5010)) #bind socket
    s.listen(1) #wait for connection
    conn, addr = s.accept() #accept one connection
    print("accepted connection")
    data = conn.recv(512) #receive some data
    print("Received handshake data...")
    if data == '110': 
        conn.sendall('111') #if data is 110, send 111
        return conn #we know we're connected, so return and prepare to accept stuff.
    elif data != '110':
        print("invalid handshake request.")
        s.close() 
        sys.exit()

def receive_files(socket):
    fileno = socket.recv(512) #receive the number of files to be sent
    print ("Number of files expected: "), fileno
    
    for x in range(0, int(fileno)):
        print("Receiving file "), x+1 , ("of "), fileno
        dat = socket.recv(1024)
        dat = dat.replace("%%%%", getpass.getuser())

        if dat != "null":
            path.append(dat) #get path of incomming file
            time.sleep(0.5)
            size = socket.recv(1024) #get size of file
            print("Receiving "),size,("bytes")
            time.sleep(0.5)
            buff = socket.recv(int(size)) #get actual file content
            print("Writing file to "), path[x-1] 
            f = open(path[x-1], 'wb') #open new file
            f.write(buff) #write content to file.
            print ("File written")
            socket.send('1')
            time.sleep(0.5)
        else:
            print("File number '"),x+1,(" is being ignored by sender.")
            time.sleep(0.5)
                        
    return      
       
    

def receive(address):
    print ("Receive started")
    socket = handshake(address)
    receive_files(socket)
    sys.exit()
