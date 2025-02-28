import argparse
import time
import subprocess
import platform
import math
import socket
import scapy.all 

def sendPacket(host, packetSize, packetCount): 
   #packet = IP(dst=dest_ip) / ICMP() / ("X" * packet_size)

    try:
        dest_IP = socket.gethostbyname(host)
        for count in range(packetCount):
            packet = scapy.all.IP(dst=dest_IP) / scapy.all.ICMP() / ("Aayan" * packetSize)
            reply = scapy.all.sr1(packet, timeout=2, verbose=False)
            symbolic = socket.gethostbyaddr(reply.src)[0] 
            print("Original Ping Address:", host, "\nHost IP:", reply.src, "\nInternal Host Name:", symbolic)
            if (count != packetCount - 1):
                print("\n\n")
    except:
       print("Could not find host name.")
       return False
    
   
    
       

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("d")
    parser.add_argument("-c", type=int) #count
    parser.add_argument("-i", type=int) #wait
    parser.add_argument("-s", type=int) #packetSize 
    parser.add_argument("-t", type=int) #time before terminate
    args = parser.parse_args()
    
    packetSize = 56
    packetCount = 1
    sleepVal = 1
    startTime = time.time()
    while(True): 
        destination = args.d    
        if (args.s):
            packetSize = args.s
        if (args.i):
            sleepVal = args.i   
        if (args.c):
            for x in range(args.c):  
                sendPacket(destination, packetSize, packetCount)
                print("\n\n")
                time.sleep(sleepVal) 
            break
        if (args.t):
            currTime = time.time()
            if (currTime - startTime) > args.t:
                break
        
        print("\n\n")
        keepRun = sendPacket(destination, packetSize, packetCount)
        time.sleep(sleepVal)
        
        if keepRun == False:
            print("Please rerun the ping with a valid host name.")
            break
        




    



main ()