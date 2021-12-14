#!/bin/env python

import re


def first_sentence(lines):
    def good(line):
        if line.startswith('#'): return False      # ignore headers
        if re.match('^[=-]+$', line): return False # ignore section dividers
        return True

    s = ''.join(line for line in lines if good(line))
    s = re.sub('<[^>]*>', '', s)                   # strip HTML
    s = re.sub('{%[^%]*%}', '', s)                 # strip Liquid tags
    s = re.sub('\[([^]]*)\]\([^\)]*\)', '\\1', s)  # strip Markdown links
    s = re.sub('\*+\\s*([^\*]*)\\s*\*+', '\\1', s) # strip emphasis
    s = re.sub('\\s\\s*', ' ', s)                  # unify whitespace
    dot = s.find('. ')
    if dot >= 0: s = s[:dot+1]                     # cut down to first sentence
    return s.strip()
