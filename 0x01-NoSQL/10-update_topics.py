#!/usr/bin/env python3
""" using Python and PyMongo """

def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the name.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
