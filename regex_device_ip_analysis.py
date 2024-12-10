import re

# Task 1: Import the `re` module
# Already imported above

# Task 2: Display the contents of device IDs
devices = (
    "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk "
    "253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq "
    "g07h55q 081qc9t r159r1u"
)
print("Devices:\n", devices)

# Task 3: Define a regular expression to find device IDs starting with "r15"
target_pattern = r"r15\w+"

# Task 4: Use re.findall() to extract matching device IDs
matched_devices = re.findall(target_pattern, devices)
print("\nDevices that require updates:", matched_devices)

# Task 5: Display the contents of the log file
log_file = (
    "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \n"
    "smartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \n"
    "rjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \n"
    "asundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \n"
    "abernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \n"
    "jclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \n"
    "jrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \n"
    "daquino 2022-05-08 7:02:35 192.168.168.144"
)
print("\nLog File:\n", log_file)

# Task 6: Define a regular expression pattern to match valid IP addresses
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Task 7: Extract IP addresses using the pattern
valid_ip_addresses = re.findall(pattern, log_file)
print("\nValid IP Addresses:\n", valid_ip_addresses)

# Task 10: Display flagged IP addresses
flagged_addresses = [
    "192.168.190.178",
    "192.168.96.200",
    "192.168.174.117",
    "192.168.168.144",
]
print("\nFlagged IP Addresses:\n", flagged_addresses)

# Task 11: Check valid IPs against flagged IPs
for address in valid_ip_addresses:
    if address in flagged_addresses:
        print(f"The IP address {address} has been flagged for further analysis.")
    else:
        print(f"The IP address {address} does not require further analysis.")