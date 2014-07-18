import sys
import socket
import time
import os
import getpass


def handshake(address):
    print ("Attempting handshake...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    port = 5010 #specify port
    s.connect((address,port)) #connect
    s.sendall('110') #send data
    reply = s.recv(512) #save reply.
    if reply == '111':
        print("Connection made")
        return s
    elif reply != '111':
        print("Invalid handshake reply.")
        s.close() #close socket
        sys.exit()

def send_files(files, socket, repname):
    socket.sendall(str(len(files))) #send number of files
    print ("files to send: "),str(files)

    for x in range(0, len(files)):
        
        if os.path.exists(files[x]): #make sure the file actually exists
            
            if repname == 1:
                dat = os.path.abspath(files[x]) #send the paths for each file
                print ("Sending '"),dat,("'...")
                dat = dat.replace(getpass.getuser(), "%%%%") #if replace name set then replace username with %
            else:
                dat = os.path.abspath(files[x]) #send the paths for each file
                print ("Sending "),dat

            socket.send(dat) 
            time.sleep(0.5)
            f = open(files[x], 'rb') #open file for read
            data = f.read() #read data in
            size = len(data) #get size of data
            print("Sending "),size,(" bytes...")
            socket.send(str(size)) #send size of file
            time.sleep(0.5) 
            socket.send(data) #send data
            time.sleep(0.5)
            msg = socket.recv(512)
            if msg  == '1':
                print ("Sending of file "),x+1 ,("Was succsessful")
            time.sleep(0.5)
            dat = ""
        else:
            socket.send("null") #If file doesnt exist, tell the server.
            time.sleep(0.5)
            print("File '"), files[x], ("' does not exist. Ignoring it.")
           
    return

def send(files, address):
  
    repname = 1

    socket = handshake(address) #call handshake process.    
    send_files(files, socket, repname)



    sys.exit()


