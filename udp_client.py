#-----------------------------------------
# Shota Nakamura
# Homework 6
#**************************************

from socket import *
import sys
import time
import datetime

# Open UDP Socket

#Loop this 10 times
    #Send Short Message & Start Timer

    #Receiver Echo & End timer
class UdpClient:

    def __init__(self, udp_host, udp_port):
        self.udp_host = udp_host
        self.udp_port = udp_port
        self.start()

    def start(self):
        # Open connection to udp python
        clientSock = socket(AF_INET, SOCK_DGRAM)
        clientSock.settimeout(10)
        #Binds address given
        address = (self.udp_host,self.udp_port)
        #Creates Message
        msg = "Hello!"
        #Encodes Message
        encodeMsg = msg.encode('utf-8')
        
        #PING 10 times
        for i in range(0,10):
            #send encoded message to the socket
            clientSock.sendto(encodeMsg,address) #Send to send the message, and the address for convenient use
            #Set a start time
            startTimer = time.time()
  
            try:
                #take message and server address
                msg, addr = clientSock.recvfrom(1024)
                #Takes end time to calculate RTT

                endTimer = time.time()
                #Calcuates RTT
                RTT = endTimer - startTimer
                t = time.localtime()
                print("Reply from " + addr[0] + ": PING " + str(i) + " " + time.asctime(t)+ " RTT: " + str(RTT))

            except:
                self.timeout()
                continue
    
    def timeout(self):
        print("Request timed out.")

def main():

    print (sys.argv, len(sys.argv))

    udp_host = 'localhost'
    udp_port = 50007

    if len(sys.argv) > 1:
        udp_host = sys.argv[1]
        udp_port = int(sys.argv[2])

    udp_client = UdpClient(udp_host, udp_port)

if __name__ == '__main__':
    main() 