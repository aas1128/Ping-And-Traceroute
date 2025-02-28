import argparse
import time
import subprocess
import platform
import math

def sendPacket(host, packetSize, packetCount): 
    os_name = platform.system()
    command = " "
    print
    if (os_name == "Darwin"):
        command = ["ping", "-c", str(packetCount), "-s", str(packetSize), host]
    else:
        command = ["ping" , "-n", str(packetCount), "-l", str(packetSize), host]
        

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("result: " , result.stdout)
    return result.stdout

def ping():
    parser = argparse.ArgumentParser()
    parser.add_argument("d")
    parser.add_argument("-c", type=int) #count
    parser.add_argument("-i", type=int) #wait
    parser.add_argument("-s", type=int) #packetSize 
    parser.add_argument("-t", type=int) #time before terminate
    args = parser.parse_args()
    counter = 0
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
                time.sleep(sleepVal)

            break
        if (args.t):
            currTime = time.time()
            if (currTime - startTime) > args.t:
                break
        sendPacket(destination, packetSize, packetCount)
        time.sleep(sleepVal)
        
         




def main(): 
    ping()

    



main ()