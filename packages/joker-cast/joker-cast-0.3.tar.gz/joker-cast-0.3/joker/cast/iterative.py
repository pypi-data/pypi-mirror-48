#!/usr/bin/env python3
# coding: utf-8

from __future__ import unicode_literals

import itertools
from collections import deque
from itertools import chain, combinations

from six import moves as six_moves


def flatten(tup):
    """
    >>> flatten([100])
    100
    >>> flatten([100, 200])
    [100, 200]
    :param tup: a tuple or list
    """
    if isinstance(tup, (tuple, list)):
        if len(tup) == 1:
            return tup[0]
        if len(tup) == 0:
            return None
    return tup


def unflatten(obj):
    """
    >>> unflatten(100)
    (100,)
    >>> unflatten(tuple([100]))
    (100,)
    :param obj:
    :return: a tuple or list
    """
    if isinstance(obj, (tuple, list)):
        return obj
    return obj,


def reusable(records):
    """
    >>> reusable(i for i in range(5))
    [0, 1, 2, 3, 4]
    >>> reusable([0, 1, 2, 3, 4])
    [0, 1, 2, 3, 4]
    :param records: an iterable
    :return: a list or tuple
    """
    if isinstance(records, (list, tuple)):
        return records
    return list(records)


def chunkwize(chunksize, iterable):
    """
    >>> list(chunkwize(5, range(14)))
    [[0, 1, 2, 3, 4], 
     [5, 6, 7, 8, 9], 
     [10, 11, 12, 13]]
     
    :param chunksize: integer
    :param iterable:
    """
    chunksize = int(chunksize)
    chunk = []
    for item in iterable:
        if len(chunk) >= chunksize:
            yield chunk
            chunk = []
        chunk.append(item)
    yield chunk


def chunkwize_parallel(chunksize, *sequences):
    """
    >>> s1 = '1234567890'
    >>> s2 = 'abcdefghijk'
    >>> list(chunkwize_parallel(4, s1, s2))
    [['1234', 'abcd'], ['5678', 'efgh'], ['90', 'ijk']]
    
    :param chunksize: integer
    :param sequences: tuple of strings or lists (must support slicing!)
    """
    chunksize = int(chunksize)
    for i in itertools.count(0):
        r = [s[i * chunksize:(i + 1) * chunksize] for s in sequences]
        if any(r):
            yield r
        else:
            raise StopIteration


def numseries_segment(wsize, iterable):
    """
    >>> list(numseries_segment(5, [1, 3, 5, 7]))
    [[1, 3], [5, 7]]

    :param wsize: integer
    :param iterable: must be asc ordered
    :return: a list of lists
    """
    wsize = float(wsize)
    count = 0
    chunk = list()
    for num in iterable:
        idx = int(num / wsize)
        while idx > count:
            yield chunk
            chunk = list()
            count += 1
        chunk.append(num)
    yield chunk


def all_combinations(iterable):
    """
    >>> list(all_combinations('abcd'))
    [(),
     ('a',),
     ('b',),
     ('c',),
     ('d',),
     ('a', 'b'),
     ('a', 'c'),
     ('a', 'd'),
     ('b', 'c'),
     ('b', 'd'),
     ('c', 'd'),
     ('a', 'b', 'c'),
     ('a', 'b', 'd'),
     ('a', 'c', 'd'),
     ('b', 'c', 'd'),
     ('a', 'b', 'c', 'd')]
    """
    items = list(iterable)
    return chain.from_iterable(
        combinations(items, i) for i in range(1 + len(items)))


def window_sum(wsize, numbers):
    """
    >>> numbers = [1, 10, 100, 1000, 10000, 100000]
    >>> list(window_sum(3, numbers))
    [111, 1110, 11100, 111000]
    
    :param wsize: integer, size of the moving window
    :param numbers: an iterable of numbers
    """
    queue = deque(maxlen=wsize)
    for num in numbers:
        queue.append(num)
        if len(queue) >= wsize:
            yield sum(queue)


def alternate(*iterables, **kwargs):
    """
    :param iterables:
    >>> ''.join(list(alternate('ABCD', 'abcde')))
    'AaBbCcDde'
    >>> ''.join(list(alternate('ABCD', 'abcde', fill='_')))
    'AaBbCcDd_e' 
    """
    _void = object()
    fill = kwargs.get('fill', _void)
    zip_longest = six_moves.zip_longest
    alt = itertools.chain(*zip_longest(*iterables, fillvalue=fill))
    for item in alt:
        if item is not _void:
            yield item
