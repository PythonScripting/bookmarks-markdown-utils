#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Evernote Clipped Bookmark to Markdown URL List element

Description: Copy links to clipboard in the input format. They'll be sent to your clipboard in the output format.

Example input:
site title | site.com

[http://example.com](http://example.com) - site description here...

Example output:
* site title | site.com - [http://example.com](http://example.com) - site description here...
"""

import re, sys
# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from pyperclip_interface import PyperInterface

def reformat_links(linklist):
    find_md_regex = re.compile(r'^\[https?.*\]\(https?.*\)')
    newformat = []
    for line in linklist:
        if line == '':
            continue
        if find_md_regex.match(line):
            newformat.append(line)
        else:
            newformat.append('\n\n* {} - '.format(line))
    return newformat

def main():    
    in_message = 'Copy your Evernote links to clipboard, press ENTER when done:'
    out_message = 'Finished!\nMarkdown links were copied to your clipboard.'
    pyper = PyperInterface(in_message, out_message)

    links = pyper.get_clipboard()
    linklist = links.split('\n')

    reformatted = reformat_links(linklist)
    pyper.send_to_clipboard(''.join(reformatted))

if __name__ == '__main__':
    main()