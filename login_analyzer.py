# Task 1: Sort a list of failed login attempts and display the result
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
print("Sorted failed login attempts:", sorted(failed_login_list))

# Task 2: Identify and display the highest number of failed login attempts
print("Highest number of failed login attempts:", max(failed_login_list))

# Task 3: Define a function to analyze logins and display the current day's total
def analyze_logins(username, current_day_logins):
    print("Current day login total for", username, "is", current_day_logins)

# Task 4: Call the analyze_logins function to test it
analyze_logins("ejones", 9)

# Task 5: Expand the function to include average logins and display the average
def analyze_logins(username, current_day_logins, average_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)

# Call the updated function
analyze_logins("ejones", 9, 3)

# Task 6: Further expand the function to calculate the login ratio
def analyze_logins(username, current_day_logins, average_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)
    login_ratio = current_day_logins / average_day_logins
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")

# Call the expanded function with login ratio
analyze_logins("ejones", 9, 3)

# Task 7: Add a return statement to the function for storing the ratio
def analyze_logins(username, current_day_logins, average_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)
    login_ratio = current_day_logins / average_day_logins
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")
    return login_ratio

# Store the returned value in a variable and display it
login_analysis = analyze_logins("ejones", 9, 3)
print("Stored login ratio:", login_analysis)

# Task 8: Use the stored value in a conditional statement
if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")