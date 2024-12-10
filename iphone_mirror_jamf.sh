#!/bin/bash

# Create Variable for Logged-in User
LoggedInUser="$(/usr/sbin/scutil <<<"show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ { print $3 }')"

# Create Variable for the known path
known_path="/Users/$LoggedInUser/Library/Daemon Containers/"

# Create variable for mdfind search
spotlight_search="/usr/bin/mdfind"

# Search for the applications and store their paths in the variable 'app_paths'
app_paths=$($spotlight_search "kMDItemKind == 'Application'" | grep -E "/(Health|Journal|Magnifier)\.app$")

#If there are no apps found the script will exit with a failure
if [$app_paths == ""]; then
	echo "App Path Empty, exiting script"
  	exit 1

# Initialize a flag to check if application is within the known path
within_known_path=true

echo "Checking application paths..."

# Handle paths with spaces by setting IFS (Internal Field Separator) to newline
IFS=$'\n'

# Check if the app_path starts with the expected known_path
for app_path in $app_paths; do
    if [[ "$app_path" == "$known_path"* ]]; then
        echo "Application found inside known path: $app_path"

        # Remove known_path from app_path to get the relative path
        relative_path="${app_path#$known_path}"

        # Extract the first directory from the relative path (parent folder)
        parent_folder="${relative_path%%/*}"

        echo "Parent folder directly after known_path: $parent_folder"

        # Construct the full path to the parent folder
        parent_folder_path="$known_path$parent_folder"

        echo "Parent folder path: $parent_folder_path"

        # Prompt for confirmation before deletion
        #read -p "Are you sure you want to delete the directory '$parent_folder_path' and all its contents? (yes/no): " confirm

        if [[ "$confirm" == "yes" ]]; then
            # Delete the parent_folder and all its contents
            #rm -rf "$parent_folder_path"
            echo "Directory '$parent_folder_path' has been deleted."
            break
        else
            echo "Deletion cancelled."
            exit 0
        fi

    else
        echo "Warning: Application found outside the known path: $app_path"
        within_known_path=false
    fi
done

# Reset IFS to default
unset IFS

# Final report
if $within_known_path; then
    echo "All applications have been processed within the known path."
    exit 0
else
    echo "Some applications were not located within the known path."
    exit 1
fi