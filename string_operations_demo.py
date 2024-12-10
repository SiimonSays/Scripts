# Task 1: Convert employee_id to a string
employee_id = 4186
print("Initial type of employee_id:", type(employee_id))  # Display initial type
employee_id = str(employee_id)
print("Type of employee_id after conversion:", type(employee_id))  # Display converted type

# Task 2: Check if employee_id meets the new length requirement
if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")

# Task 3: Update employee_id to meet length requirement
if len(employee_id) < 5:
    employee_id = "E" + employee_id
print("Updated employee ID:", employee_id)

# Task 4: Extract the fourth character from a device_id
device_id = "r262c36"
print("Fourth character of device_id:", device_id[3])

# Task 5: Extract the first three characters of device_id
print("First three characters of device_id:", device_id[0:3])

# Task 6: Extract the protocol from a URL
url = "https://exampleURL1.com"
print("Protocol of the URL:", url[0:8])

# Task 7: Identify the starting index of the domain extension
ind = url.index(".com")
print("Starting index of '.com':", ind)

# Task 8: Save the index of the domain extension in a variable
# Already done in Task 7 with `ind`

# Task 9: Extract the domain extension using the index
print("Domain extension:", url[ind:ind+4])

# Task 10: Extract the website name using slicing
print("Website name:", url[8:ind])