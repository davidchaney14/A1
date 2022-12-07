"""
Moduele : Main.py
Auth : David Chaney
Version : 1.0
Date : 05/11/2022
"""
# This file is used to perform testing on code before moving to main.py
# Global Variables
dhcplog = "dhcp.log"

# Imports
import Source.brackets
import Source.hostcheck
# Main function
if (__name__=='__main__'):
    # Clean our initial input log into something workable
    # Clean the file and output a more 'prettier' file
    def cleanInputLog():
        # Open the logfile and read
        dhcplogopen = open(dhcplog, "r")
        # Clear the contents of dhcpcleaned.log
        with open("dhcpcleaned.log", "w") as f:
            print(' ', file=f)
        # Read each line in dhcplogopen
        for line in dhcplogopen:
            # Checking the type of line passed
            # Checking for DHCPACK & Request
            # Remove unneed informtion from start of line
            dhcp_log_cleaned = line[34:]
            dhcp_values = dhcp_log_cleaned.split(" ")
            # Create list for values of ACK/REQ
            DHCPACK = ['DHCPACK', 'DHCPREQUEST']
            # Check values against list
            if dhcp_values[0] in DHCPACK:
                # Interesting matieral
                if dhcp_values[1] == "on":
                    mac = Source.brackets.remove_brakcets(dhcp_values[4])
                    Source.hostcheck()
                    print(f"Interesting, found a {dhcp_values[0]} and IP is {dhcp_values[2]} and MAC is {mac}, the host type is {host_type}")
                    # Lets push that to a file for later
                    with open("dhcpcleaned.log", "a") as f:
                        print(f"Interesting, IP is {dhcp_values[2]} and MAC is {mac}, the host type is {host_type}", file=f)
                elif dhcp_values[1] =="to":
                    mac = Source.brackets.remove_brakcets(dhcp_values[3])
                    DellValues = ['c8:4b:d6:0a:77:2d', 'c0:25:a5:66:81:fc', 'a4:4c:c8:50:c3:6b']
                    if mac == "b8:27:eb:b4:81:6d":
                        host_type = "Raspberry PI"
                    elif mac in DellValues:
                        host_type = "Dell"
                    elif mac == "18:68:cb:45:1a:ae":
                        host_type = "Hikvision"
                    elif mac == "bc:5f:f4:45:7c:1e":
                        host_type = "ASRock"
                    else:
                        host_type = "Unknown"
                    print(f"Interesting, found a {dhcp_values[0]} and IP is {dhcp_values[2]} and MAC is {mac}. the host type is {host_type}")
                    # Lets push that to a file
                    with open("dhcpcleaned.log", "a") as f:
                        print(f"Interesting, IP is {dhcp_values[2]} and MAC is {mac},  the host type is {host_type}", file=f)
            # Lets handle the not so interesting lines and let the user know
            elif dhcp_values[0]:
                print(f"Not so interesting, {dhcp_log_cleaned}", end="")
    # Think its better at this stage to work another function, getting to big
    def mactohosttype():
        # Open the new output logfile to work with
        dhcplogclean = "dhcpcleaned.log"
        mactohost = open(dhcplogclean, "r")
        with open("mactohost.log", "w") as f:
            print(' ', file=f)
else:
        print("Test -- Something has gone wrong! Else statement ran")

# Execute our functions
cleanInputLog()