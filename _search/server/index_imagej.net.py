#!/bin/env python

import os, sys, traceback
import yaml
from index_site import *


def parse_document(docroot, path, icons):
    debug(f'Parsing {path}...')
    with open(path) as f:
        lines = f.readlines()

    if path.endswith('_config.yml'):
        info("Found config")

    if len(lines) == 0 or not lines[0].strip() == '---':
        # missing front matter indicator -- assume it's not a Jekyll document.
        return None

    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == '---':
            # conclusion of front matter; treat the rest as content
            break

    content = lines[i+1:]
    debug(f'--> Content is {len(content)} lines')
    front_matter = lines[1:i]
    doc = yaml.safe_load(''.join(front_matter))
    debug(f'--> Front matter is {len(doc)} items')

    # Coerce YAML content to strings only. Sad but necessary.
    for key in doc:
        doc[key] = str(doc[key])

    if 'icon' not in doc:
        depth = -1
        for key in icons.keys():
            if key in path:
                count = key.count('/')

                if count > depth:
                    depth = count
                    doc['icon'] = icons[key]

    # Set required field values.
    doc['id'] = path[len(docroot):path.rindex('.')]
    doc['score'] = 100 # a constant value, at least for now
    if not 'title' in doc: doc['title'] = doc['id']
    doc['content'] = ''.join(content)

    if not 'description' in doc:
        description = first_sentence(content)
        debug(f'--> Inferred description: {description}')
        doc['description'] = description

    return doc

def parse_icon_defaults(config):
    icons = {}
    with open(config) as f:
        lines = f.readlines()

    doc = yaml.safe_load(''.join(lines))

    defaults = {}
    if 'defaults' in doc:
        defaults = doc['defaults']

    for rule in defaults:
        scope = rule['scope']
        values = rule['values']
        if scope['type'] == 'pages' and 'path' in scope and 'icon' in values:
            icons[scope['path']] = values['icon']

    return icons


def load_jekyll_site(docroot, defaults):
    """
    Loads the Jekyll content from the given docroot folder.
    """
    documents = []
    for root, dirs, files in os.walk(docroot):
        for name in files:
            path = os.path.join(root, name)
            try:
                doc = parse_document(docroot, path, defaults)
                if doc: documents.append(doc)
            except:
                error(f'Failed to parse {path}:')
                traceback.print_exc()
    return documents


if len(sys.argv) == 1:
    collection = 'imagej-wiki'
    pathname = os.path.join(os.path.dirname(sys.argv[0]), '..', '..')
elif len(sys.argv) == 3:
    collection = sys.argv[1]
    pathname = sys.argv[2]
else:
    print('Usage: index-site.py [<collection-name> <jekyll-site-docroot>]')
    sys.exit(1)

config = os.path.join(pathname, '_config.yml')
docroot = os.path.join(pathname, '_pages')
if not os.path.isfile(config) or not os.path.isdir(docroot):
    error(f'The path ${pathname} does not appear to be a Jekyll site.')
    sys.exit(1)
else:
    print(f'Found _pages at ${docroot}')

info('Parsing config...')
icons = parse_icon_defaults(config)
info('Config parsed')

info('Loading content...')
documents = load_jekyll_site(docroot, icons)
info(f'Loaded {len(documents)} documents')

client = connect()
info('Connected to typesense')
created = create(client, collection, documents, force=True)
info('Created new collection' if created else 'Updating existing collection')
info(f'Indexing {len(documents)} documents...')
update_index(client, collection, documents)
info('Done!')
