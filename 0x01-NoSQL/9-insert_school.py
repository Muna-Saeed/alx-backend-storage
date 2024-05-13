#!/usr/bin/env python3
""" using Python and PyMongo """

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
