#*******************************************************************
#                         UDP Ping Application
#                        Author: Shota Nakamura
# Objective: simulate a udp ping server that will take messages from
#            clients and determine whether packets get dropped.
#*******************************************************************

import socketserver
from socket import *
import random
import sys

class Udp_Server:

    def __init__(self, udp_port):
        self.udp_port = udp_port
        self.start()

    def start(self):
        #Create UDP Socket 
        serverSock = socket(AF_INET, SOCK_DGRAM)
        serverSock.bind(('',self.udp_port))
        
        #Wait (Listen for connection from Udp_Client)
        while True:
            #Receive a message 
            msg,address = serverSock.recvfrom(1024) #Must be recvfrom since this is unconnected
            #Here generate a random number, If it is divisible by 3 dont send an echo) 
            num = random.randint(0,30)
            
            #Drop packets 1 out of 3 times, else send back message ack
            if num % 3 == 0:
                continue
            else:
                serverSock.sendto(msg,address)


def main():

    print (sys.argv, len(sys.argv))
    udp_port = 50007

    if len(sys.argv) > 1:
        udp_port = int(sys.argv[1])

    udpserver = Udp_Server(udp_port)

if __name__ == '__main__':
    main()