#!/usr/bin/env python3
""" lists all documents in a collection """

def list_all(mongo_collection):
    """ returns list of collection """
    return [document for document in mongo_collection.find()]