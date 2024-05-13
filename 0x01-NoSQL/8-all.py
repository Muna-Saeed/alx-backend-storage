#!/usr/bin/env python3
""" using Python and PyMongo """


def list_all(mongo_collection):
    """
    List all documents in a collection.
    """
    documents = list(mongo_collection.find({}))
    return documents
