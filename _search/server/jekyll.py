#!/bin/env python

import logging, os, traceback
import yaml
from parseutil import first_sentence


logger = logging.getLogger(__name__)


def is_jekyll_site(siteroot):
    config = os.path.join(siteroot, '_config.yml')
    docroot = os.path.join(siteroot, '_pages')
    return os.path.isfile(config) and os.path.isdir(docroot)


def parse_jekyll_document(docroot, path, icons):
    logger.debug(f'Parsing {path}...')
    with open(path) as f:
        lines = f.readlines()

    if len(lines) == 0 or not lines[0].strip() == '---':
        # missing front matter indicator -- assume it's not a Jekyll document.
        logger.debug('Skipping non-Jekyll file {path}')
        return None

    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == '---':
            # conclusion of front matter; treat the rest as content
            break

    content = lines[i+1:]
    logger.debug(f'--> Content is {len(content)} lines')
    front_matter = lines[1:i]
    doc = yaml.safe_load(''.join(front_matter))
    logger.debug(f'--> Front matter is {len(doc)} items')

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
    if not 'title' in doc:
        doc['title'] = doc['id']
    doc['content'] = ''.join(content)

    if not 'description' in doc:
        description = first_sentence(content)
        logger.debug(f'--> Inferred description: {description}')
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


def load_jekyll_site(siteroot):
    """
    Loads the Jekyll content from the given siteroot folder.
    """
    config = os.path.join(siteroot, '_config.yml')
    docroot = os.path.join(siteroot, '_pages')
    if not os.path.isfile(config) or not os.path.isdir(docroot):
        raise ValueError(f'The path {siteroot} does not appear to be a Jekyll site.')

    logger.info('Parsing config...')
    icons = parse_icon_defaults(config)
    logger.info('Config parsed')

    logger.info('Loading content...')
    documents = []
    for root, dirs, files in os.walk(docroot):
        for name in files:
            path = os.path.join(root, name)
            try:
                doc = parse_jekyll_document(docroot, path, icons)
                if doc:
                    documents.append(doc)
            except:
                logger.error(f'Failed to parse {path}:')
                traceback.print_exc()
    logger.info(f'Loaded {len(documents)} documents')
    return documents
