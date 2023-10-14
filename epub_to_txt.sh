#!/usr/bin/bash
#
# Loop over EPUB files in the 'epub' directory
for epub_file in ./epubs/*.epub; 
do
# # Extract the base filename without extension
    base_filename=$(basename "$epub_file" .epub)
#
#     # Convert EPUB to text using pandoc
    pandoc -s "$epub_file" -o "txt/$base_filename.txt"
#
    echo "Converted $epub_file to txt/$base_filename.txt"
    # echo "Converted $epub_file "
done
