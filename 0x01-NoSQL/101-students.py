#!/usr/bin/env python3
"""
a Python function
"""


from pymongo import collection


def top_students(mongo_collection: collection.Collection) -> list:
    """
    Return all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    students = list(mongo_collection.aggregate(pipeline))
    return students

