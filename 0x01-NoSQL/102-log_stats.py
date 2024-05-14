#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')


def get_stats():
    """ returns stats """
    database = client["logs"]
    collection = database["nginx"]
    get_logs = collection.count_documents({"method": "GET"})
    post_logs = collection.count_documents({"method": "POST"})
    put_logs = collection.count_documents({"method": "PUT"})
    patch_logs = collection.count_documents({"method": "PATCH"})
    delete_logs = collection.count_documents({"method": "DELETE"})
    st_logs = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    print(f'\tmethod GET: {get_logs}')
    print(f'\tmethod POST: {post_logs}')
    print(f'\tmethod PUT: {put_logs}')
    print(f'\tmethod PATCH: {patch_logs}')
    print(f'\tmethod DELETE: {delete_logs}')
    print(f"{st_logs} status check")


def print_top_ips():
    '''Prints statistics about the top 10 HTTP IPs in a collection.
    '''
    print('IPs:')
    database = client["logs"]
    collection = database["nginx"]
    request_logs = collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


if __name__ == "__main__":
    get_stats()
    print_top_ips()
