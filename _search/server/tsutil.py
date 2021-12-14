#!/bin/env python

import logging
import typesense


logger = logging.getLogger(__name__)


def connect():
    """
    Open a connection to the typesense server.
    """
    try:
        with open('/etc/typesense/typesense-server.ini') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None

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
    logger.info('Deleted existing collection')


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
    # a union of all the observed keys, plus the three required fields.
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


def update_index(client, collection, documents):
    """
    Update the collection with the given name to match the given documents.
    """
    client.collections[collection].documents.import_(documents, {'action': 'upsert'})
