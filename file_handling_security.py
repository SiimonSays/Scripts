# Task 1: Import a security log file and prepare it for analysis
import_file = "data/login.txt"

# Open the file for reading and store the content as a string
with open(import_file, "r") as file:
    # Read the file content
    text = file.read()

# Display the contents of the imported file
print("Imported Security Log:\n", text)

# Task 2: Split the file contents into separate lines
# Split the text into a list of strings, one string per line
lines = text.split("\n")
print("\nSplit Security Log:\n", lines)

# Task 3: Append a missing entry to the file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

# Append the missing entry to the log file
with open(import_file, "a") as file:
    file.write("\n" + missing_entry)

# Re-read and display the updated file
with open(import_file, "r") as file:
    updated_text = file.read()

print("\nUpdated Security Log:\n", updated_text)

# Task 4: Create a new file for allowed IP addresses
allow_list_file = "data/allow_list.txt"
allowed_ips = (
    "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 "
    "192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 "
    "192.168.116.187 192.168.15.110 192.168.39.246"
)

# Write allowed IP addresses to a new file
with open(allow_list_file, "w") as file:
    file.write(allowed_ips)

# Task 5: Read the allowed IPs file and display its content
with open(allow_list_file, "r") as file:
    allowed_ips_content = file.read()

print("\nAllowed IPs:\n", allowed_ips_content)