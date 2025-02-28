Aayan Sayed 
CSCI 351
HW 02

Project: Ping and Traceroute
Description: This project is a implementation of the Ping and Traceroute using Sockets.

Although the instructions specify implementing two Python files, my_ping.py and my_traceroute.py, which I have completed, 
I have also implemented an additional version of Ping using Python’s subprocess library. This serves as a wrapper around 
the existing system ping command, providing an alternative approach to executing the functionality.

1) How to compile and run the code:
    1) Clone the github repository to access the python code and the dependencies (can make a virtual environment using python)
    2) Check if python is downloaded on the system
    3) install the requirements needed to run the code 
    4) run the code using "python my_ping.py <hostName>" or "python my_traceroute.py <hostName>" follow by filters.

Filters:

   Ping possible command line arguments:

        "-d" -> Required: hostname for the Ping.
                EX: "python my_ping.py google.com"

        "-c count" -> Optional: Allows user to specifiy the amount of Pings to send before terminating
                EX: "python my_ping.py google.com -c 5"

        "-i wait" -> Optional: Allows user to specifiy amount of time to wait before sending the next packet. Default is 1 second.
                EX: "python my_ping.py google.com -i 3"

        "-s packetSize" -> Optional: Allows user to specify amount of data to put in the payload of the ICMP echo request. My function fills it with "Aayan". 
                EX: "python my_ping.py google.com -s 5"

        "-t timeout" -> Optional: Allow user to specify a timeout in seconds beforet the project terminates. 
                EX: "python my_ping.py google.com -t 10"

   Traceroute possible command line arguments:

        "-d" -> Required: hostname for the Ping.
                EX: "python my_traceroute.py google.com"

        "-n" -> Optional: Print hop addresses numerically rather than symbolically and numerically.
                EX: "python my_traceroute.py google.com -n"

        "-q nqueries" -> Optional: Set the number of probes per TTL to nqueries. Defaut is 1.
                EX: "python my_traceroute.py google.com -q 5"

        "-S" -> Optional: Print a summary of how many probes were not answered for each hop.
                EX: "python my_traceroute.py google.com -S"
        



