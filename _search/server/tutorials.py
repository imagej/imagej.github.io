#!/bin/env python

# Parse ImageJ tutorials into documents for
# use with their own searchable collection.

import logging, traceback
import yaml
from parseutil import first_sentence


logger = logging.getLogger(__name__)


def is_imagej_tutorials(root):
    java = Path(root) / 'java'
    notebooks = Path(root) / 'notebooks'
    return java.isdir() and notebooks.isdir()


def parse_java_source(path):
    logger.debug(f'Parsing Java source file {path}...')

    with open(path) as f:
        lines = json.read(f)

    # This is dumb -- do we want to do better?
    doc = {}
    doc['content'] = ''.join(lines)

    return doc


def parse_notebook(path):
    logger.debug(f'Parsing notebook {path}...')

    with open(path) as f:
        data = json.read(f)

    doc = {}
    doc['content'] = ''
    for cell in data['cells']:
        # TODO: implement process_cell: extract source and output(s) if present
        doc['content'] += process_cell(cell)

    return doc


def load_imagej_tutorials(root):
    """
    Loads the content from the given imagej/tutorials folder.
    See: https://github.com/imagej/tutorials
    """
    java = Path(root) / 'java'
    notebooks = Path(root) / 'notebooks'
    if not java.isdir() or not notebooks.isdir():
        raise ValueError(f'The path {siteroot} does not appear to be a Jekyll site.')

    logger.info('Loading content...')
    documents = []

    for javafile in java.rglob("**/*.java"):
        try:
            doc = parse_java_source(javafile)
            if doc:
                documents.append(doc)
        except:
            logger.error(f'Failed to parse {path}:')
            traceback.print_exc()
    logger.info(f'Loaded {len(documents)} documents from Java source files')

    for nbfile in notebooks.rglob("**/*.ipynb"):
        try:
            doc = parse_notebook(nbfile)
            if doc:
                documents.append(doc)
        except:
            logger.error(f'Failed to parse {path}:')
            traceback.print_exc()
    logger.info(f'Loaded {len(documents)} documents from Jupyter notebooks')

    return documents
