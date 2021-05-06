import logging
import os.path
from avl import AVL

LOGGER = logging.getLogger(__name__)

def test_insert():
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
    l = list()
    for i in range(0, 200):
        l.append(i)
    tree = AVL()
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    
    l = list()
    for i in range(0, 200):
        l.append(i)
    while len(l) > 0:
        key = l.pop(0)
        croot = tree.find(key)
        left_height = tree.recur_height(croot.left)
        right_height = tree.recur_height(croot.right)
        assert abs(left_height-right_height) <= 1
        assert tree.recur_is_balanced(croot) == True

def test_remove():
    tree = AVL()
    s = 10
    for i in range(0, s):
        tree.insert(i, i)
    for i in range(0, s):
        tree.remove(i)