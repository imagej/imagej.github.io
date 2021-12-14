#!/bin/env python

import os, traceback
from bs4 import BeautifulSoup

from index_site import *


def extract_description(content):
    pass


def parse_document(docroot, path):
    debug(f'Parsing {path}...')
    try:
        with open(path) as f:
            html = BeautifulSoup(f)
    except Exception as e:
        print(e)
        return None
    content = [line.text for line in html.contents]
    debug(f'--> Content is {len(content)} lines')
    doc = {
        'id': path[len(docroot):path.rindex('.')]
    }
    # Parse special key/value pairs out of the HTML from e.g. plugin pages.
    # This is the stuff like "Author:" etc.
    table = html.find('table')
    if table:
        rows = table.find_all('tr')
        for row in rows:
            col = row.find_all('td')
            if len(col) == 2:
                key = col[0].text
                val = col[1].text
                if key.endswith(':'):
                    doc[key[:-1]] = val
    # Set required field values.
    doc.update({
        'score': 100, # a constant value, at least for now,
        'title': html.title.text if html.title else id,
        'icon': '/media/icons/imagej.png',
        'content': ' '.join(content),
        'description': extract_description(content),
    })
    return doc

#description: try to extract key value pairs from beautiful soup results - "content"

#parse icons was here

def load_site(docroot):
    """
    Loads the content from the given docroot folder.
    """
    documents = []
    for root, dirs, files in os.walk(docroot):
        if root.find('\\developer\\api') >= 0 or \
                root.find('\\developer\\source') >= 0 or \
                root.find('\\javadoc') >= 0 or \
                root.find('\\source') >= 0:
            continue
        for name in files:
            if not name.endswith('.html'):
                continue
            path = os.path.join(root, name)
            try:
                doc = parse_document(docroot, path)
                if doc: documents.append(doc)
            except:
                error(f'Failed to parse {path}:')
                traceback.print_exc()
    return documents


docroot = 'C:/Users/Michael Nelson/imagej.nih'
info('Loading content...')
documents = load_site(docroot)
info(f'Loaded {len(documents)} documents')

for doc in documents:
    if doc['id'].find('fraclac.html') >= 0:
        print(doc)
'''
client = connect()
info('Connected to typesense')
created = create(client, collection, documents, force=True)
info('Created new collection' if created else 'Updating existing collection')
info(f'Indexing {len(documents)} documents...')
update_index(client, collection, documents)
info('Done!')
'''
