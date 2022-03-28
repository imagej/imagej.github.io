#!/bin/env python

# Parse ImageJ tutorials into documents for
# use with their own searchable collection.

import logging, os, traceback
import yaml
from parseutil import first_sentence


logger = logging.getLogger(__name__)


def is_imagej_tutorials(root):
    java = os.path.join(root, 'java')
    notebooks = os.path.join(root, 'notebooks')
    return os.path.isdir(java) and os.path.isdir(notebooks)


def parse_java_source(root, path):
    logger.debug(f'Parsing Java source file {path}...')

    with open(path) as f:
        lines = json.read(f)

    # This is dumb -- do we want to do better?
    doc = {}
    doc['content'] = ''.join(lines)

    return doc


def parse_notebook(root, path):
    logger.debug(f'Parsing notebook {path}...')

    with open(path) as f:
        data = json.read(f)

    doc = {}
    doc['content'] = ''
    for cell in data['cells']:
        # TODO: implement process_cell: extract source and output(s) if present
        doc['content'] += process_cell(cell)

    return doc


def find_resources(root, suffix):
    # TODO: use pathlib to find all .java or .ipynb (based on suffix) inside root.
    pass


def load_imagej_tutorials(root):
    """
    Loads the content from the given imagej/tutorials folder.
    See: https://github.com/imagej/tutorials
    """
    java = os.path.join(siteroot, 'java')
    notebooks = os.path.join(siteroot, 'notebooks')
    if not os.path.isdir(java) or not os.path.isdir(notebooks):
        raise ValueError(f'The path {siteroot} does not appear to be a Jekyll site.')

    logger.info('Loading content...')
    documents = []

    for javafile in find_resources(java, '.java'):
        try:
            doc = parse_java_source(root, path)
            if doc:
                documents.append(doc)
        except:
            logger.error(f'Failed to parse {path}:')
            traceback.print_exc()
    logger.info(f'Loaded {len(documents)} documents from Java source files')

    for nbfile in find_resources(notebooks, '.ipynb'):
        try:
            doc = parse_notebook(root, path)
            if doc:
                documents.append(doc)
        except:
            logger.error(f'Failed to parse {path}:')
            traceback.print_exc()
    logger.info(f'Loaded {len(documents)} documents from Jupyter notebooks')

    return documents
