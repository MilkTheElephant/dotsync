import sys
import socket
import time

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
        dat = files[x] #send the paths for each file
        socket.send(dat) 
        time.sleep(1)
        f = open(files[x], 'rb') #open file for read
        data = f.read() #read data in
        size = len(data) #get size of data
        socket.send(str(size)) #send size of file
        time.sleep(1) 
        socket.send(data) #send data
        time.sleep(1)
        msg = socket.recv(512)
        if msg  == '1':
            print ("Sending of file "), x ,("Was succsessful")
        time.sleep(1)
           
    return

def send(files, address):
    print ("Sendint process started")
    
    socket = handshake(address) #call handshake process.    
    send_files(files, socket)



    sys.exit()


