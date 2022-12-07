"""
Moduele : Main.py
Auth : David Chaney
Version : 1.0
Date : 05/11/2022
"""
# Global Variables
dhcplog = "dhcp.log"

# Imports
# Remove brackets
import Source.brackets

# Main function
if (__name__=='__main__'):
    # Clean our initial input log into something workable and output a more 'prettier' file
    def cleanInputLog():
        # Open the logfile and read
        dhcplogopen = open(dhcplog, "r")
        # Clear the contents of dhcpcleaned.log
        with open("dhcpcleaned.log", "w") as f:
            print(' ', file=f)
        # Read each line in dhcplogopen
        for line in dhcplogopen:
            # Checking the type of line passed, check for DHCPACK & Request and remove excess information
            # Start of line @ 34 chars
            dhcp_log_cleaned = line[34:]
            dhcp_values = dhcp_log_cleaned.split(" ")
            # Create list for values of ACK/REQ
            DHCPACK = ['DHCPACK', 'DHCPREQUEST']
            # Check values against list
            if dhcp_values[0] in DHCPACK:
                # Lets look more at the MAC values and link to host
                if dhcp_values[1] == "on":
                    # Clean brackets from some MAC ids
                    mac = Source.brackets.remove_brakcets(dhcp_values[4])
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
                    # Update user on screen
                    print(f"Interesting, found a {dhcp_values[0]} and IP is {dhcp_values[2]} and MAC is {mac}, the host type is {host_type}")
                    # Update file with this information
                    with open("dhcpcleaned.log", "a") as f:
                        print(f"Interesting, IP is {dhcp_values[2]} and MAC is {mac}, the host type is {host_type}", file=f)
                elif dhcp_values[1] =="to":
                    # Similar to code above, look at MAC and clean if need, offset is different  on the 'to' lines by -1 word
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
                    # Update user on screen
                    print(f"Interesting, found a {dhcp_values[0]} and IP is {dhcp_values[2]} and MAC is {mac}. the host type is {host_type}")
                    # Update file with this information
                    with open("dhcpcleaned.log", "a") as f:
                        print(f"Interesting, IP is {dhcp_values[2]} and MAC is {mac},  the host type is {host_type}", file=f)
            # Lets handle the not so interesting lines and let the user know, which is not captured in file
            elif dhcp_values[0]:
                print(f"Not so interesting, {dhcp_log_cleaned}", end="")
# Handle situations where something has gone wrong!
else:
        print("Error - something has gone wrong! Else statement has run, review file input location, looks like its missing!")

# Execute our functions
cleanInputLog()