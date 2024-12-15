#!/bin/bash
# Loop through each JSON file in the json/ directory
for file in json/*.json; do
  # Extract the filename without extension
  filename=$(basename "$file" .json)
  
  # Run the script and redirect output to the md/ directory with the same filename but .md extension
  python3 jsonToMarkdown.py --file "$file" > "md/${filename}.md"
done
