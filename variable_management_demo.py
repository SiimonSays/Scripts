# Task 1: Assign the device ID to a variable and display it
device_id = "72e08x0"
print("Device ID:", device_id)

# Task 2: Determine and display the data type of `device_id`
device_id_type = type(device_id)
print("Data type of `device_id`:", device_id_type)

# Task 3: Create a list of approved usernames and display it
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
print("Approved usernames:", username_list)

# Task 4: Determine and display the data type of `username_list`
username_list_type = type(username_list)
print("Data type of `username_list`:", username_list_type)

# Task 5: Update the list of approved usernames to include a new user and display the difference
print("Original usernames:", username_list)
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpope"]
print("Updated usernames:", username_list)

# Task 6: Define a variable for the maximum number of login attempts and display its data type
max_logins = 3
max_logins_type = type(max_logins)
print("Data type of `max_logins`:", max_logins_type)

# Task 7: Define a variable for the current number of login attempts and display its data type
login_attempts = 2
login_attempts_type = type(login_attempts)
print("Data type of `login_attempts`:", login_attempts_type)

# Task 8: Check if the current login attempts are less than or equal to the maximum allowed
print("Login attempts <= Max logins:", login_attempts <= max_logins)

# Task 9: Reassign `login_attempts` to a new value and observe the output
login_attempts = 4
print("Login attempts <= Max logins (updated):", login_attempts <= max_logins)

# Task 10: Create a Boolean variable for login status and display its data type
login_status = False
login_status_type = type(login_status)
print("Data type of `login_status`:", login_status_type)