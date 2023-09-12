from socket import *
from datetime import datetime
import sys
import time


#Reads in and Stores sommand line arguments and sets up varibles
message= sys.argv[1]
message= sys.argv[1]
serverName = sys.argv[2]
serverPort = int(sys.argv[3])
timePassed= time.time()
count = 0


#Coonect to the server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


#loop for repeated connection attempts and for id resets
while True:
    try:
        #clientSocket.timeout(15)

        #sends and recives message
        clientSocket.send(message.encode())
        recived = clientSocket.recv(1024)
        messsageList = recived.decode().split()

        #Handles resets and message receival
        if(count==3):
            print(count)
            print('Connection Failure on ' + str(datetime.now()))
        if(messsageList[0]=="OK"):
            print("Connection established " + str(messsageList[1]) + " " + str(serverName) + " " +  str(serverPort))
            break
        if(messsageList[0]=="Reset"):
            num = input("ConnectionID already in use. Select new ID: ")
            message = "HELLO " + num 
            count+=1

    #handles connection failures        
    except:
        print('Connection Failure on ' + str(datetime.now()))
        break
clientSocket.close()