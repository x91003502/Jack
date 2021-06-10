import logging
from priority_queue import PriorityQueue

LOGGER = logging.getLogger(__name__)

class PQItem(object):
    def __init__(self, id, index):
        self.id = id
        self.count = [1]
        self.index = [index]
    
    def addCount(self):
        self.count[0] += 1
    
    def minusCount(self):
        self.count[0] -= 1
    
    def getCount(self):
        return self.count[0]
    
    def getIndex(self):
        return self.index[0]
    
class PQVertex(object):
    def __init__(self, id, distance):
        self.id = id
        self.distance = [distance]


def test_PQItem():
    index = 0
    item = PQItem(id, index)
    assert item.count[0] == 1
    
    for k in range(1, 200):
        assert item.count[0] == k
        item.addCount()
    LOGGER.debug(f'count: {item.count[0]}')

def test_init():
    capacity = 10
    sortKey = 'count'
    pq = PriorityQueue(capacity, sortKey=sortKey)
    assert len(pq.minHeap) == 0
    assert pq.size == 0
    assert pq.capacity == capacity
    assert pq.sortKey == sortKey

import sys
capacity = sys.maxsize 
sortKey = 'count'
pq = PriorityQueue(capacity, sortKey=sortKey)
def test_insert():
    
    index = 0
    for i in range(97, 107):
        id = chr(i)
        item = PQItem(id, index)
        
        pq.insert(item)
        assert pq.size == index + 1
        index += 1

# def test_removeMin():
#     while pq.size > 0:
#         min = pq.removeMin()
#         assert min.count[0] == 1
#     assert pq.size == 0

# def test_clear():
#     pq.clear()
#     assert pq.size == 0
#     LOGGER.debug(f'Size: {pq.size}')

# def test_clear2():
#     test_insert()
#     pq.clear()
#     assert pq.size == 0
#     LOGGER.debug(f'Size: {pq.size}')