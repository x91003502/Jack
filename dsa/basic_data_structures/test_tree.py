import logging
import os.path
from tree import Tree

LOGGER = logging.getLogger(__name__)

def test_insert():
    tree = Tree()
    s = 100
    for i in range(0, s):
        tree.insert(i, i)
    k = 0
    curr = tree.root
    while k < s:
        assert curr.key == k
        assert curr.left == None
        curr = curr.right
        k += 1

def test_in_order():
    tree = Tree()
    s = 100
    elem = list()
    for i in range(0, s):
        tree.insert(i, i)
        elem.append(i)
    res = tree.in_order()
    assert res == elem

def test_in_order2():
    tree = Tree()
    s = 100
    elem = list()
    for i in reversed(range(0, s)):
        tree.insert(i, i)
        elem.append(i)
    res = tree.pre_order()
    assert res == elem

def test_height():
    tree = Tree()
    s = 100
    assert tree.height() == -1
    for i in range(0, s):
        tree.insert(i, i)
        tree.height() == i

import random
def test_find():
    l = list()
    for i in range(97, 107):
        l.append(i)
    
    tree = Tree()
    random.shuffle(l)
    while len(l) > 0:
        key = l.pop()
        value = chr(key)
        tree.insert(key, value)
    
    for i in range(97, 107):
        key = i
        value = chr(key)
        croot = tree.find(key)
        assert croot.value == value

def test_remove():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
            key = l.pop(0)
            value = chr(key)
            tree.insert(key, value)
    # tree.remove(38)
    # assert tree.root.key == 37
    # assert tree.find(38) == None
    
    # tree.remove(89)
    # croot = tree.find(89)
    # assert croot.right.key == 95
    
    # tree.remove(13)
    # assert tree.root.left.key == 12
    
    res = tree.in_order()
    print(res)


