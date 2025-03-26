#!/bin/python3

# Import modules
import re
from pathlib import Path

# Set target directory
src_dir = "/home/sociodicy/imagined_realities/content/blog/"


def find_images(file_variable):
    files = Path(file_variable).glob("*")
    for filename in files:
        with open(filename, "r+", encoding="utf-8") as blogpost:
            link = blogpost.read()
            link = re.sub(
                r"https\:\/\/christopherbauer\.org\/(\d{4})\/(\d{2})\/(\d{2})\/(\w.*)\.html",
                r"https://christopherbauer.org/blog/\1-\2-\3-\4",
                link,
            )
            blogpost.seek(0)
            blogpost.write(link)

    return print("Text replaced")


find_images(src_dir)
