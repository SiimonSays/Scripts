# Task 1: Display a message using a for loop
for i in range(3):
    print("Connection could not be established.")

# Task 2: Use a variable to control the number of iterations
connection_attempts = 3
for i in range(connection_attempts):
    print("Connection could not be established.")

# Task 3: Display a message using a while loop
connection_attempts = 0
while connection_attempts < 3:
    print("Connection could not be established.")
    connection_attempts += 1

# Task 4: Display each IP address in a list
ip_addresses = [
    "192.168.142.245", "192.168.109.50", "192.168.86.232", 
    "192.168.131.147", "192.168.205.12", "192.168.200.48"
]

for ip in ip_addresses:
    print(ip)

# Task 5: Check if IP addresses are allowed
allow_list = [
    "192.168.243.140", "192.168.205.12", "192.168.151.162", 
    "192.168.178.71", "192.168.86.232", "192.168.3.24", 
    "192.168.170.243", "192.168.119.173"
]

for ip in ip_addresses:
    if ip in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")

# Task 6: Break the loop if an unauthorized IP is found
for ip in ip_addresses:
    if ip in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed. Further investigation of login activity required.")
        break

# Task 7: Generate unique employee IDs divisible by 5 between 5000 and 5150
i = 5000
while i <= 5150:
    print(i)
    i += 5

# Task 8: Add a notification when 10 IDs remain
i = 5000
while i <= 5150:
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i += 5