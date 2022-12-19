#!/bin/env python

import logging, os, traceback
from bs4 import BeautifulSoup

from parseutil import first_sentence


logger = logging.getLogger(__name__)


def is_imagej_website(docroot):
    notes = os.path.join(docroot, 'notes.html')
    return os.path.isfile(notes)


def extract_description(doc, body):
    desc = None
    if 'Description' in doc:
        desc = first_sentence(doc['Description'])
    if not desc:
        desc = first_sentence(body)
    return desc


def parse_document(docroot, path):
    logger.debug(f'Parsing {path}...')
    try:
        with open(path) as f:
            html = BeautifulSoup(f, features='lxml')
    except Exception as e:
        print(e)
        return None
    content = html.text.splitlines()
    logger.debug(f'--> Content is {len(content)} lines')
    doc = {}

    # Parse key/value pairs from the HTML head/meta tags.
    metas = [] if not html.head else html.head.find_all('meta')
    for meta in metas:
        if not meta.has_attr('name') or not meta.has_attr('content'):
            continue
        key = meta['name']
        val = meta['content']
        logger.debug(f'--> Found meta tag key/value pair: {key} = {val}')
        doc[key] = val

    # Parse key/value pairs e.g. "Author:" out of the HTML plugin table.
    table = html.find('table')
    if table:
        rows = table.find_all('tr')
        for row in rows:
            col = row.find_all('td')
            if len(col) == 2:
                key = col[0].text
                val = col[1].text
                if key.endswith(':'):
                    key = key[:-1]
                    logger.debug(f'--> Found key/value pair: {key} = {val}')
                    doc[key] = val

    # Set required field values.
    docid = path[len(docroot):]
    doc.update({
        'id': f'https://imagej.net/ij{docid}',
        'score': 90, # a constant value, at least for now,
        'title': html.title.text if html.title else docid,
        'icon': '/media/icons/imagej.png',
        'content': ''.join(content),
    })
    if not 'description' in doc:
        doc['description'] = extract_description(doc, html.body.text),

    return doc


def load_site(docroot):
    """
    Loads the content from the given docroot folder.
    """
    documents = []
    ignored_paths = [
        '/developer/api',
        '/developer/source',
        '/javadoc',
        '/source',
    ]
    logger.info('Loading content...')
    for root, dirs, files in os.walk(docroot):
        if any(root.find(path) >= 0 for path in ignored_paths):
            continue
        for name in files:
            if not name.endswith('.html'):
                continue
            path = os.path.join(root, name)
            try:
                doc = parse_document(docroot, path)
                if doc: documents.append(doc)
            except:
                logger.error(f'Failed to parse {path}:')
                traceback.print_exc()
    logger.info(f'Loaded {len(documents)} documents')
    return documents
