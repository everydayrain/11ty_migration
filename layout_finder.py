#!/bin/python3
# Simple script to search recursively through md files and find the text "layout" and remove

# Import modules
from pathlib import Path

# Set the source directory and find all the files within it.
src_dir = Path("/home/directory/of/your/blog/")
files = src_dir.glob("*")

## Find the frontmatter category "layout" and delete it.
try:
    for search in files:
        with open(search, "r") as fileread:
            lines = fileread.readlines()

            with open(search, "w") as filewrite:
                for line in lines:

                    # strip() is used to remove '\n'
                    # present at the end of each line
                    if line.strip("\n") != "layout: post":
                        filewrite.write(line)
except:
    print("Oops! Something went wrong.")
