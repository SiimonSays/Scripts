# Task 1: Display elements from approved lists based on indices
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Display specific elements
print("User:", approved_users[0])
print("Device:", approved_devices[0])

# Task 2: Add a new user and device
new_user = "gesparza"
new_device = "3rcv4w6"
approved_users.append(new_user)
approved_devices.append(new_device)

print("Updated users:", approved_users)
print("Updated devices:", approved_devices)

# Task 3: Remove a user and device
removed_user = "tshah"
removed_device = "2ye3lzg"
approved_users.remove(removed_user)
approved_devices.remove(removed_device)

print("Users after removal:", approved_users)
print("Devices after removal:", approved_devices)

# Task 4: Verify if a user is approved
username = "sgilmore"
if username in approved_users:
    print(f"The user {username} is approved to access the system.")
else:
    print(f"The user {username} is not approved to access the system.")

# Task 5: Find the index of a username
ind = approved_users.index(username)
print(f"Index of {username}: {ind}")

# Task 6: Display the corresponding device for a user
print(f"Device assigned to {username}: {approved_devices[ind]}")

# Task 7: Verify user and device pairing
device_id = "4n482ts"
if username in approved_users and device_id == approved_devices[ind]:
    print(f"The user {username} is approved to access the system.")
    print(f"{device_id} is the assigned device for {username}.")
elif username in approved_users and device_id != approved_devices[ind]:
    print(f"The user {username} is approved to access the system, but {device_id} is not their assigned device.")
else:
    print(f"The user {username} is not approved to access the system.")

# Task 9: Function to automate user and device verification
def login(username, device_id):
    if username in approved_users:
        print(f"The user {username} is approved to access the system.")
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
            print(f"{device_id} is the assigned device for {username}.")
        else:
            print(f"{device_id} is not their assigned device.")
    else:
        print(f"The user {username} is not approved to access the system.")

# Call the login function with different credentials
login("bmoreno", "hl0s5o1")
login("elarson", "r2s5r9g")
login("abernard", "4n482ts")