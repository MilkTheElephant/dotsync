import sys
import socket
import time
import os


def handshake(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    port = 5010 #specify port
    s.connect((address,port)) #connect
    s.sendall('110') #send data
    print("sent") 
    reply = s.recv(512) #save reply.
    print("Got reply") 
    if reply == '111':
        print("Connection made")
        return s
    elif reply != '111':
        print("Invalid handshake reply.")
        s.close() #close socket
        sys.exit()

def send_files(files, socket):
    print len(files)
    socket.sendall(str(len(files))) #send number of files
    print (files)

    for x in range(0, len(files)):
        
        print x

        if os.path.exists(files[x]): #make sure the file actually exists
            dat = os.path.abspath(files[x]) #send the paths for each file
            print dat
            socket.send(dat) 
            time.sleep(0.5)
            f = open(files[x], 'rb') #open file for read
            print ("opened: "), files[x]
            data = f.read() #read data in
            size = len(data) #get size of data
            print("sending size: "), size
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
    print ("Sendint process started")
    
    socket = handshake(address) #call handshake process.    
    send_files(files, socket)



    sys.exit()


