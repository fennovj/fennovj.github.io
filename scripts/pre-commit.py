#!/usr/bin/env python3
import os
from pathlib import Path
from markdown import markdown
# This entire script is done somewhat verbosely to hopefully be platform-independent
# Render all markdowns to html, and place them in the 'html' directory.

# List of extensions. Codehilite is, as the name suggests, for code highlighting.
extensions = ['codehilite']

# Create the html output directory if it was deleted for some reason
if not os.path.exists('html'):
    os.makedirs('html')

for fname in os.listdir('markdown'):
    # Convert 'markdown/filename.md' to 'filename'
    basename = os.path.splitext(os.path.basename(fname))[0]
    # Output path like 'html/filename.html'
    output_fname = Path('html', basename).with_suffix('.html')
    # First read and render the markdown to html
    with open(Path('markdown', fname), 'r') as f:
        body = markdown(f.read(), extensions=extensions)
    # Then read the template
    with open('scripts/template.html', 'r') as f:
        template = f.read()
    # Then write the result to the output
    with open(output_fname, 'w+') as f:
        f.write(template.format(markdown=body))
