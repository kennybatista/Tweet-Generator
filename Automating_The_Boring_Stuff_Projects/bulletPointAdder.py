#!/usr/bin/env python

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

#Abstract mission - take in text, output new lines that begin with a bullet point
        #Steps
# paste text from clipboard,
# do something to it,
# copy the new text to the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add starts
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
