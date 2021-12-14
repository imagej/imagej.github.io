#!/bin/env python

import os, re, sys, traceback
import typesense
import yaml


def debug(s):
    pass

def info(s):
    print(f'[INFO] {s}')

def error(s):
    sys.stderr.write(f'[ERROR] {s}\n')


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


def connect():
    """
    Open a connection to the typesense server.
    """
    with open('/etc/typesense/typesense-server.ini') as f:
        lines = f.readlines()

    api_key = [line[10:] for line in lines if line.startswith('api-key = ')][0].rstrip()

    return typesense.Client({
      'nodes': [{
        'host': 'search.imagej.net',
        'port': '8108',
        'protocol': 'https'
      }],
      'api_key': api_key,
      'connection_timeout_seconds': 2,
    })


def summary(client, collection):
    summary = client.collections.retrieve()
    for item in summary:
        if item['name'] == collection:
            return item


def drop(client, collection):
    """
    Delete the collection with the given name.
    """
    client.collections[collection].delete()
    info('Deleted existing collection')


def create(client, collection, documents, force=False):
    """
    Create the collection with the given name, if it doesn't already exist.

    :return: True if newly created; False if collection already exists.
    """
    if summary(client, collection):
        # already exists
        if force: drop(client, collection)
        else: return False

    # Typesense allows you to index the following types of fields:
    #   string, int32 int64, float, bool
    #   string[], int32[], int64[], float[], bool[]

    # Make a schema out of all the fields present across all the documents:
    # a union of all the observed YAML keys, plus the three required fields.
    fieldset = set()
    for doc in documents:
        fieldset.update(doc)
    fieldset -= {'id', 'score', 'title', 'content'}
    fields = [
        {'name': 'score',   'type': 'int32'}, # for tie-breaking
        {'name': 'title',   'type': 'string'}, # required field
        {'name': 'content', 'type': 'string'}, # required field
    ]
    fields.extend({'name': key, 'type': 'string', 'optional': True} for key in fieldset)

    schema = {
        'name': collection,
        'fields': fields,
        'default_sorting_field': 'score',
    }
    client.collections.create(schema)
    return True


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


def update_index(client, collection, documents):
    """
    Update the collection with the given name to match the given documents.
    """
    client.collections[collection].documents.import_(documents, {'action': 'upsert'})

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
    error(f'The path {pathname} does not appear to be a Jekyll site.')
    sys.exit(1)
else:
    print(f'Found _pages at {docroot}')

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
