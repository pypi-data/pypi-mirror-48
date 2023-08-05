# -*- coding: utf-8 -*-
import six
import codecs
from concurrent import futures
import functools
import hashlib
import collections


def wrap_result_in_future(result):
    f = futures.Future()
    f.set_result(result)
    return f


def wrap_exception_in_future(exc):
    f = futures.Future()
    f.set_exception(exc)
    return f


def future():
    return futures.Future()


# Decorator that ensures no exceptions are leaked from decorated async call
def wrap_async_call_exceptions(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return wrap_exception_in_future(e)
    return decorator


def reply_with_result(f, result):
    if not f.done():
        f.set_result(result)


def get_query_hash(yql_text):
    try:
        return hashlib.sha256(six.text_type(yql_text, 'utf-8').encode('utf-8')).hexdigest()
    except TypeError:
        return hashlib.sha256(six.text_type(yql_text).encode('utf-8')).hexdigest()


class LRUCache(object):
    def __init__(self, capacity=1000):
        self.items = collections.OrderedDict()
        self.capacity = capacity

    def put(self, key, value):
        self.items[key] = value
        while len(self.items) > self.capacity:
            self.items.popitem(last=False)

    def get(self, key, _default):
        if key not in self.items:
            return _default
        value = self.items.pop(key)
        self.items[key] = value
        return value

    def erase(self, key):
        self.items.pop(key)


def from_bytes(val):
    """
    Translates value into valid utf8 string
    :param val: A value to translate
    :return: A valid utf8 string
    """
    try:
        return codecs.decode(val, 'utf8')
    except (UnicodeEncodeError, TypeError):
        return val
