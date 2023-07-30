#!/bin/bash

# Create directories for each file type
mkdir -p imgs audio pdf videos other

# Move files to corresponding directories based on their extensions
for file in *; do
    if [ -f "$file" ]; then
        extension="${file##*.}"
        case "$extension" in
            jpg|jpeg|png|gif|bmp)
                mv "$file" imgs/
                ;;
            mp3|wav|flac|aac)
                mv "$file" audio/
                ;;
            pdf|pages)
                mv "$file" pdf/
                ;;
            mp4|mkv|avi|mov)
                mv "$file" videos/
                ;;
            *)
                mv "$file" other/
                ;;
        esac
    fi
done

echo "Files have been arranged into respective directories."

