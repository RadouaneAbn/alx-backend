#!/usr/bin/env python3
""" hypermedia_pagination """


import csv
from math import ceil
from typing import List, Dict, Union


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
        self.__dataset_len = len(self.__dataset)

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

    def get_hyper(self, page: int = 1, page_size: int = 10)\
            -> Dict[str, Union[List[List], int, None]]:
        """ This method returns a dictionary conatining the following
            key-value pairs:
                page_size
                page
                data
                next_page
                prev_page
                total_pages
        """
        data = self.get_page(page, page_size)
        current_page_size = len(data)
        next_page = None
        prev_page = None
        if (page + 1 + 1) * page_size < self.__dataset_len:
            next_page = page + 1
        if page * page_size > 0:
            prev_page = page - 1
        total_pages = ceil(self.__dataset_len / page_size)
        return {
            "page_size": current_page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
