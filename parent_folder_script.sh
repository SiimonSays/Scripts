#!/bin/bash

# Create Variable for Logged-in User
LoggedInUser=$(whoami)

# Create Variable for the known path
known_path="/Users/$LoggedInUser/Library/Daemon Containers/"

# Search for the applications and store their paths in the variable 'app_paths'
app_paths=$(mdfind "kMDItemKind == 'Application'" | grep -E "/(Health|Journal|Magnifier)\.app$")

# Initialize a flag to check if all applications are within the known path
all_within_known_path=true

echo "Checking application paths..."

# Handle paths with spaces by setting IFS (Internal Field Separator) to newline
IFS=$'\n'

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

        # Navigate to the parent folder if needed
        # cd "$parent_folder_path"

        # You can perform actions within this directory now
        # For example, list contents:
        # ls "$parent_folder_path"

    else
        echo "Warning: Application found outside the known path: $app_path"
        all_within_known_path=false
    fi
done

# Reset IFS to default
unset IFS

# Final report
if $all_within_known_path; then
    echo "All applications are correctly located within the known path."
else
    echo "Some applications are not located within the known path."
fi
