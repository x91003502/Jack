import logging

import os.path

from src.cache.priority_queue import PriorityQueue

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

capacity = 10
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

def test_removeMin():
    while pq.size > 0:
        min = pq.removeMin()
        assert min.count[0] == 1
    assert pq.size == 0

def test_clear():
    pq.clear()
    assert pq.size == 0
    LOGGER.debug(f'Size: {pq.size}')

def test_clear2():
    test_insert()
    pq.clear()
    assert pq.size == 0
    LOGGER.debug(f'Size: {pq.size}')

def test_findInexById():
    test_insert()
    k = 0
    for i in range(97, 107):
        id = chr(i)
        index = pq.findInexById(id)
        assert index == k
        LOGGER.debug(f'Id: {id}, Index: {index}')
        k += 1
    test_clear()

def test_removeByIndex():
    test_insert()
    k = 0
    size = pq.size
    for i in range(97, 107):
        id = chr(i)
        index = pq.findInexById(id)
        remove = pq.removeByIndex(index)
        size -= 1
        assert remove.id == id
        assert size == pq.size
        LOGGER.debug(f'Should Be Removed: {id}, Removed: {remove.id} Index: {index}. PQ Size: {size}')
        k += 1
        pq.printHeap()
    test_clear()

# # Above tests are for insertion and deletion

# def test_isHeap():
#     test_insert()
#     is_heap = pq.isHeap()
#     assert is_heap == True
    
#     forth_item = pq.minHeap[3]
#     forth_item.addCount()
#     is_heap = pq.isHeap()
#     assert is_heap == False
    
#     eighth_item = pq.minHeap[7]
#     ninth_item = pq.minHeap[8]
#     eighth_item.addCount()
#     ninth_item.addCount()
#     is_heap = pq.isHeap()
#     assert is_heap == True
    
#     seventh_item = pq.minHeap[6]
#     seventh_item.addCount()
#     seventh_item.addCount()
#     is_heap = pq.isHeap()
#     assert is_heap == True
    
#     test_clear()

# from random import randint
# def test_update():
#     test_insert()
#     first_item = pq.minHeap[0]
#     first_item.addCount()
#     is_heap = pq.isHeap()
#     assert is_heap == False
    
#     pq.update(0)
#     is_heap = pq.isHeap()
#     assert is_heap == True
    
#     k = 0
#     max_index = pq.parent(pq.size)
#     for k in range(0, 200):
#         index = randint(0, max_index)
#         item = pq.minHeap[index]
#         item.addCount()
#     is_heap = pq.isHeap()
#     assert is_heap == False
    
#     for index in reversed(range(0, pq.size)):
#         item = pq.minHeap[index]
#         pq.update(index)
#     pq.printHeap()
#     is_heap = pq.isHeap()
#     assert is_heap == True
#     test_clear()

# def test_swap():
#     firstItem = PQItem('a', index=0)
#     secondItem = PQItem('b', index=1)
#     pq.insert(firstItem)
#     pq.insert(secondItem)
#     firstItem.addCount()

#     assert firstItem.getIndex() == 0
#     assert firstItem.id == 'a'
#     assert firstItem.getCount() == 2
#     assert secondItem.getIndex() == 1
#     assert secondItem.id == 'b'
#     assert secondItem.getCount() == 1
    
#     pq.swap(0, 1)
    
#     firstItem = pq.minHeap[0]
#     secondItem = pq.minHeap[1]

#     assert firstItem.getIndex() == 0
#     assert firstItem.id == 'b'
#     assert firstItem.getCount() == 1
#     assert secondItem.getIndex() == 1
#     assert secondItem.id == 'a'
#     assert secondItem.getCount() == 2
