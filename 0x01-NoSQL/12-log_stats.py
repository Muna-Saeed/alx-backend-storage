#!/usr/bin/env python3
""" Nginx logs stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total number of logs
    num_logs = logs_collection.count_documents({})
    print(f"{num_logs} logs")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Specific method and path
    specific_count = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{specific_count} status check")
