from socket import *
from datetime import datetime
import sys
import time

#Reads in and Stores sommand line arguments and sets up varibles
serverPort = int(sys.argv[2])
serverIP = sys.argv[1]
connectionId = []
connectionIdTime = []

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
timeSinceRequest= time.time()
serverSocket.listen(1)
closed = False

print("The TCP server is ready to receive")

#listens for first connection
connectionSocket, addr = serverSocket.accept()

#loop used to keep server listening
while True:

     #used to connect to new connection
     if(closed):
          closed = False
          connectionSocket, addr = serverSocket.accept()

     try:
        #sends and recives messages
        serverSocket.settimeout(120)
        sentence = connectionSocket.recv(1024).decode() # if the buf size value is smaller than the datagram size, it will drop the rest.
        modifiedMessage = sentence.split()


        #handles connectionId
        if(len(modifiedMessage)!=0):
          count=0
          for id in connectionId:
               if time.time() - connectionIdTime[count] > 30:
                    del connectionId[count]
                    del connectionIdTime[count]
               count+=1
          if modifiedMessage[1] in connectionId:
               returnMessage = 'Reset Connection'
               connectionSocket.send(returnMessage.encode())
          else:
               timeSinceRequest= time.time()
               connectionId.append(modifiedMessage[1])
               connectionIdTime.append(time.time())
               returnMessage= "OK " + modifiedMessage[1]
               connectionSocket.send(returnMessage.encode())
               connectionSocket.close()
               closed = True
               
     except:
        print('Server Closed')
        serverSocket.close()
        break