import argparse
import time
import subprocess
import platform
import scapy.all 
import socket

"""
     Main function that reads in arguments applies filters and constructs 
     packets before sending probes across network to implement traceroute.
     Arguments: None
     Returns:None 
    """
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("d")
    parser.add_argument("-n", action="store_true") #count
    parser.add_argument("-S", action="store_true" ) #packetSize 
    parser.add_argument("-q", type=int, default=3) #packetSize 

    args = parser.parse_args()
    dest_IP = socket.gethostbyname(args.d)
    ttlCount = 1
    while(True):
        port = 53
        nonans = 0 
        
        # Sending the packet and receive a reply
        for query in range(args.q):
            ip_packet = scapy.all.IP(dst=dest_IP, ttl=ttlCount)
            udp_packet = scapy.all.UDP(dport=port)
            #Here I tried to create a UDP packet header with the correct port
            #however UDP packets were getting blocked for some reason.
            packet = ip_packet / scapy.all.ICMP() # Had to use ICMP packets instead to get a response
            reply = scapy.all.sr1(packet, timeout=5, verbose=0)
            port += 1
            if reply is None:
               
            # No reply, print * for timeout
                nonans += 1
                print(f"{ttlCount} *")
            else:
                try:
                    symbolic = socket.gethostbyaddr(reply.src)[0]       
                except(socket.herror):
                    symbolic = "No Host Name Found"


                if reply.haslayer(scapy.all.ICMP) and reply[scapy.all.ICMP].type == 0:
                    # Destination reached, print the details
                    if args.n:
                     print(f"{ttlCount}\t{reply.src}")
                    else:
                     print(f"{ttlCount}\t{reply.src}\t{symbolic}")

                    return 
                else:
                    # Printing the IP address of the intermediate hop
                    if args.n:
                        print(f"{ttlCount}\t{reply.src}")
                    else:
                        print(f"{ttlCount}\t{reply.src}\t{symbolic}")

        if args.S:
            print("Number of unanswered packets:" , nonans)
        ttlCount += 1
        if ttlCount > 30:
            break 
          
    return 

if __name__ == "__main__":       
    main()