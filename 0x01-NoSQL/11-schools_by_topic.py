#!/usr/bin/env python3
""" list of docs with matching query """


def schools_by_topic(mongo_collection, topic):
    """ returns list of schools """
    return list(mongo_collection.find({"topics": topic}))
