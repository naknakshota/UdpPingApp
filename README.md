# UdpPingApp (Expermenting with UDP)

Author: Shota Nakamura

A simple udp ping application that drops some packets on purpose.

How to run the app (In terminal)
1.) Run python3 udp_server.py (This opens up the server)
2.) Run python3 udp_client.py

Files include in this program:

File: udp_client.py
Details: This is the ping client file. This client file will send 10 messages (encoded to utf-8) to udp_server.py. It will either receive a packet back within the timeout interval or the packet will timeout, in which chances are the server's function determined that the packet will be dropped. Note that packet timeout is set to 10 seconds. Once it receives the echo, it will out put its PING # and its RTT or round trip time.

File: udp_server.py
Details: This is the ping server file. It will create a UDP socket, bind it to port 50007, and then wait for client messages. When it receives a message, a function will determine whether an ACK will be sent back or if the packet will be dropped. The ACK will just echo back the message to the client.

