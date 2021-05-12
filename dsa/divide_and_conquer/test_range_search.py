import logging
import os.path
from binary_search2 import range_search

def test_range1():
    arr = [1,6,11]
    rg = [2, 3]
    index1, index2 = range_search(arr, rg)
    assert index1 > index2
    
    rg = [0, 5]
    index1, index2 = range_search(arr, rg)
    assert index1 <= index2
    
    rg = [7, 10]
    index1, index2 = range_search(arr, rg)
    assert index1 > index2

def test_range2():
    arr = [-100,10,100]
    rg = [1, 3]
    index1, index2 = range_search(arr, rg)
    assert index1 > index2
    
    rg = [-10, 10]
    index1, index2 = range_search(arr, rg)
    assert index1 <= index2