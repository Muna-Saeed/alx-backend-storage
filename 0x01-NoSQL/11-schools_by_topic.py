#!/usr/bin/env python3
""" using Python and PyMongo """

def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return schools
