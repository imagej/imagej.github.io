#!/bin/env python

import logging, os, sys
import jekyll, ijsite, tsutil
import tutorials


logger = logging.getLogger('indexer')


def load_site(siteroot):
    if jekyll.is_jekyll_site(siteroot):
        return jekyll.load_jekyll_site(siteroot)
    if ijsite.is_imagej_website(siteroot):
        return ijsite.load_site(siteroot)
    if tutorials.is_imagej_tutorials(siteroot):
        return tutorials.load_imagej_tutorials(siteroot)
    return None


def load_sites(sites):
    logger.info('Loading documents...')
    documents = []
    for siteid, siteroot in sites.items():
        docs = load_site(siteroot)
        if docs:
            for doc in docs:
                doc['siteid'] = siteid
            documents.extend(docs)
    logger.info(f'{len(documents)} documents loaded.')
    return documents


def index_documents(collection, documents):
    client = tsutil.connect()
    if client is None:
        logger.info('No typesense credentials available.')
        return
    logger.info('Connected to typesense.')
    created = tsutil.create(client, collection, documents, force=True)
    logger.info('Created new collection.' if created else 'Updating existing collection.')
    logger.info(f'Indexing {len(documents)} documents...')
    tsutil.update_index(client, collection, documents)
    logger.info('Done!')


def main(args):
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    logging.root.setLevel(logging.INFO)

    if len(args) == 1:
        collection = 'imagej-wiki'
        sites = {
            'imagej.net': os.path.join(os.path.dirname(args[0]), '..', '..'),
            'imagej.nih.gov/ij': '/var/www/mirror.imagej.net',
        }
    elif len(args) >= 3:
        collection = args[1]
        siteroot = args[2]
    else:
        print('Usage: index-sites.py [<collection-name> <site-id:site-root> [<another-site-id:another-site-root>...]]')
        sys.exit(1)

    documents = load_sites(sites)
    index_documents(collection, documents)


if __name__ == '__main__':
    main(sys.argv)
