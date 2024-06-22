#!/usr/bin/env python3
""" 0-simple_helper_function """


def index_range(page: int, page_size: int) -> tuple:
    """ This function returns a tuple of size two
        containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
