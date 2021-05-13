import logging
import os.path
from avl import AVL

LOGGER = logging.getLogger(__name__)

def test_insert0():
    tree = AVL()
    l = [5,15,10]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        # print(tree.in_order())
        tree.insert(key, value)
        print(tree.in_order())
        print(tree.level_order())
        print("="*20)
    assert tree.root.key == 10
    assert tree.in_order() == [5,10,15]
    assert tree.level_order() == [10,5,15]

def test_insert1():
    tree = AVL()
    l = [5,10,15]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    assert tree.root.key == 10
    assert tree.in_order() == [5,10,15]
    assert tree.level_order() == [10,5,15]

def test_insert2():
    tree = AVL()
    l = [10,12,2,5,9]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    assert tree.in_order() == [2,5,9,10,12]
    assert tree.level_order() == [10,5,12,2,9]

def test_insert3():
    tree = AVL()
    l = [10,12,2,5,9,15,20]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
        print(tree.in_order())
    assert tree.in_order() == [2,5,9,10,12,15,20]
    assert tree.level_order() == [10,5,15,2,9,12,20]

def test_insert4():
    tree = AVL()
    l = [10,20,9,5,2]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
        print(tree.in_order())
    assert tree.in_order() == [2,5,9,10,20]
    assert tree.level_order() == [10,5,20,2,9]

def test_insert5():
    tree = AVL()
    l = [10,20,9,5,2,15,12]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
        print(tree.in_order())
    assert tree.in_order() == [2,5,9,10,12,15,20]
    assert tree.level_order() == [10,5,15,2,9,12,20]

def test_insert6():
    s = 1000
    l = list()
    for i in range(0, s):
        l.append(i)
    tree = AVL()
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    
    for i in range(0, s):
        l.append(i)
    while len(l) > 0:
        key = l.pop(0)
        croot = tree.find(key)
        left_height = tree.recur_height(croot.left)
        right_height = tree.recur_height(croot.right)
        assert abs(left_height-right_height) <= 1
        assert tree.recur_is_balanced(croot) == True

import random
def test_remove():
    tree = AVL()
    s = 200
    l = list()
    for i in range(0, s):
        l.append(i)
    random.shuffle(l)
    
    while len(l) > 1:
        key = l.pop(0)
        value = key
        tree.insert(key, value)
        assert tree.check_balanced(tree.root) == True
    
    l = list()
    for i in range(0, s):
        l.append(i)
    random.shuffle(l)
    while len(l) > 1:
        key = l.pop(0)
        tree.remove(key)
        assert tree.check_balanced(tree.root) == True

def test_find_smaller1():
    tree = AVL()
    for i in range(0,10):
        res = tree.find_leq(i)
        assert len(res) == 0
    tree.insert(10, 10)
    for i in range(0,10):
        res = tree.find_leq(i)
        assert len(res) == 0
    res = tree.find_leq(10)
    assert res == [10]
    
def test_find_smaller2():
    tree = AVL()
    l = [7,4,10,2,6,9,14,12,16]
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    res = tree.find_leq(10)
    res.sort()
    assert res == [2,4,6,7,9,10]
    
    res = tree.find_leq(7)
    res.sort()
    assert res == [2,4,6,7]
    
    res = tree.find_leq(4)
    res.sort()
    assert res == [2,4]
    
    res = tree.find_leq(17)
    res.sort()
    assert res == [2,4,6,7,9,10,12,14,16]
    
    res = tree.find_leq(8)
    res.sort()
    assert res == [2,4,6,7]
    
    res = tree.find_leq(11)
    res.sort()
    assert res == [2,4,6,7,9,10]