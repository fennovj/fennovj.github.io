#!/usr/bin/env python3
import os
from pathlib import Path
from markdown import markdown

# This entire script is done somewhat verbosely to hopefully be platform-independent

# Convert 'markdown/filename.md' to 'filename'
get_basename = lambda fname: os.path.splitext(os.path.basename(fname))[0]

# Create the html output directory if it was deleted for some reason
if not os.path.exists('html'):
    os.makedirs('html')

for fname in os.listdir('markdown'):
    basename = get_basename(fname)
    output_fname = Path('html', basename).with_suffix('.html')
    # First read and render the markdown to html
    with open(Path('markdown', fname), 'r') as f:
        body = markdown(f.read())
    # Then read the template
    with open('scripts/template.html', 'r') as f:
        template = f.read()
    # Then write the result to the output
    with open(output_fname, 'w+') as f:
        f.write(template.format(markdown = body))
