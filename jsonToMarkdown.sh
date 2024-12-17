#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_directory> <output_directory>"
  exit 1
fi

# Assign arguments to variables
input_dir="$1"
output_dir="$2"

# Ensure the output directory exists
mkdir -p "$output_dir"

# Loop through each JSON file in the input directory
for file in "$input_dir"/*.json; do
  # Extract the filename without extension
  filename=$(basename "$file" .json)
  
  # Run the script and redirect output to the output directory with the same filename but .md extension
  python3 jsonToMarkdown.py --file "$file" > "$output_dir/${filename}.md"
done

