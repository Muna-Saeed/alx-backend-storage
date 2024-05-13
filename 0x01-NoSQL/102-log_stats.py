#!/usr/bin/env python3
"""
102-log_stats
"""


from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")

    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)
    for ip_info in top_ips:
        ip = ip_info.get("_id")
        count = ip_info.get("count")
        print(f"    {ip}: {count}")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)

