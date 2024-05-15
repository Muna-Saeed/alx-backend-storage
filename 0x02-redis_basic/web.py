#!/usr/bin/env python3
"""
Web cache and tracker module.
"""

import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """
    Decorator to count how many times a particular URL was accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to count and cache the URL requests.
        """
        cache_key = f"count:{url}"
        r.incr(cache_key)
        return method(url)
    return wrapper

@count_requests
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a particular URL and cache the result
    with an expiration time of 10 seconds.

    :param url: The URL to fetch.
    :return: The HTML content of the URL.
    """
    cache_key = f"cached:{url}"
    cached_content = r.get(cache_key)

    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    html_content = response.text

    r.setex(cache_key, 10, html_content)
    return html_content

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    html_content = get_page(url)
    print(html_content)
    access_count = r.get(f"count:{url}").decode('utf-8')
    print(f"Access count for {url}: {access_count}")

