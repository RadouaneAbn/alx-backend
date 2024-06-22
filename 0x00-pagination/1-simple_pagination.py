#!/usr/bin/env python3
""" 1-simple_pagination """

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ This function returns a tuple of size two
        containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.dataset()

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ This method returns that return the content of a page
        """
        assert (type(page) is int and type(page_size) is int)\
            and (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        return self.__dataset[start: end]
