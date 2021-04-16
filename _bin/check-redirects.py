#!/bin/env python

import os, sys

def pagepath(page):
    p1 = os.path.join('_site', page) + '.html'
    if os.path.isfile(p1): return p1
    p2 = os.path.join('_site', page, 'index.html')
    if os.path.isfile(p2): return p2

def valid(slug):
    hashsign = slug.find('#')
    page = slug[:hashsign] if hashsign >= 0 else slug
    anchor = slug[hashsign+1:] if hashsign >= 0 else None

    path = pagepath(page)
    if not path: return False
    if not anchor: return True
    fragment1 = f' id="{anchor}"'
    fragment2 = f' name="{anchor}"'

    with open(path, 'r') as f:
        for line in f.readlines():
            if fragment1 in line or fragment2 in line:
                return True # found the anchor
    return False # anchor not found

def resolve(working, broken, slug):
    if valid(slug):
        return slug
    if slug in working:
        return working[slug]
    for frm, to in broken:
        if frm == slug:
            try:
                resolved = resolve(working, broken, to)
                if resolved: return resolved
            except RecursionError:
                print(f'[INFINITE LOOP] {frm} -> {to}')
    return None

with open('redirects.txt') as f:
    lines = f.readlines()

working = {}
broken = []
for line in lines:
    before, after = line.strip().split(' :: ')
    if valid(after):
        if before in working:
            print(f'[ERROR] {before} -> {working[before]} AND {after}!')
            sys.exit(1)
        working[before] = after
    else:
        broken.append((before, after))

for before, after in broken:
    resolved = resolve(working, broken, after)
    if resolved:
        print(f'{before} -> {after} -> {resolved}')
    else:
        print(f'[DEAD END] {before} -> {after}')
