#!/usr/bin/env python3
""" function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ updates based on name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
