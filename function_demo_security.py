# Task 1: Define a function named `alert()`
def alert():
    print("Potential security issue. Investigate further.")

# Call the `alert()` function
alert()

# Task 2: Modify `alert()` to display the message three times using a loop
def alert():
    for i in range(3):
        print("Potential security issue. Investigate further.")

# Call the updated `alert()` function
alert()

# Task 3: Define a function named `list_to_string()` to iterate through a list
def list_to_string():
    # Store the list of approved usernames in a variable
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", 
                     "gesparza", "alevitsk", "wjaffrey"]
    # Write a loop to display each username
    for username in username_list:
        print(username)

# Call the `list_to_string()` function
list_to_string()

# Task 4: Enhance `list_to_string()` to concatenate the usernames into one string
def list_to_string():
    # Store the list of approved usernames in a variable
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", 
                     "gesparza", "alevitsk", "wjaffrey"]
    # Initialize an empty string for concatenation
    sum_variable = ""
    # Concatenate the usernames
    for username in username_list:
        sum_variable += username
    # Display the concatenated string
    print(sum_variable)

# Call the enhanced `list_to_string()` function
list_to_string()

# Task 5: Improve `list_to_string()` for better readability using commas and spaces
def list_to_string():
    # Store the list of approved usernames in a variable
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", 
                     "gesparza", "alevitsk", "wjaffrey"]
    # Initialize an empty string for concatenation
    sum_variable = ""
    # Concatenate the usernames with ", " as a separator
    for username in username_list:
        sum_variable += username + ", "
    # Display the concatenated string
    print(sum_variable)

# Call the final version of the `list_to_string()` function
list_to_string()