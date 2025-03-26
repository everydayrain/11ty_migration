#!/bin/python3
# Simple script to replace markdown image links placed in /assets/img with html code for /img/<some_name>

# Import modules
import re
from pathlib import Path

# Set target directory
src_dir = "/home/directory/of/your/blog/"

def find_images(file_variable):
  files = Path(file_variable).glob("*")
  for filename in files:
    with open(filename, "r+", encoding="utf-8") as blogpost:
      md = blogpost.read()
      md = re.sub(
        r"!\[.*?\]\(\/assets\/img\/(.*\.png|.*\.JPG|.*\.jpg)\)",
        r"<div class="grid"><div><img src="/img/g<1>" loading="lazy" title=""/></div><div></div></div>",
        md,
      )
      blogpost.seek(0)
      blogpost.write(md)
  return print("Text replaced")


find_images(src_dir)
