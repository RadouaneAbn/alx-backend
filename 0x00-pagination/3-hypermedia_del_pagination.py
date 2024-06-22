#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) \
            -> Dict[str, Union[List[List], int, None]]:
        """ This method returns a dictionary containing some data of a page
        """
        if not self.__indexed_dataset:
            return []
        index_dataset_len = len(self.__indexed_dataset)
        index_dataset_keys = sorted(self.__indexed_dataset.keys())
        assert all([index >= 0, index < index_dataset_len])
        cursor = index
        while cursor not in index_dataset_keys:
            cursor += 1
        next_index = index_dataset_keys[
            index_dataset_keys.index(cursor) + page_size
            ]
        end = next_index
        data = [self.__indexed_dataset[idx] for idx in range(index, end)
                if self.__indexed_dataset.get(idx, None) is not None]
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }

    def gett(self, n):
        for i in range(n):
            dd = self.__indexed_dataset.get(i, None)
            if dd is not None:
                print(f"{i}: {dd}")
