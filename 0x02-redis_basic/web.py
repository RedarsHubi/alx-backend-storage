#!/usr/bin/env python3
""" Return HTML Module """

from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count(method: Callable) -> Callable:
    """ Decortator """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count
def get_page(url: str) -> str:
    """ Get the HTML of a  URL """
    req = requests.get(url)
    return req.text
