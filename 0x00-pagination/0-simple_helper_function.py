#!/usr/bin/env python3
"""Defining the function index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """This function returns the starting and ending index of a page"""
    end = page * page_size
    start = end - page_size
    return(start, end)
