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

def test_find_parent_croot():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    p1, c1 = tree.find_parent_croot(13)
    p2, c2 = tree.find_parent_croot(51)
    assert p1.key == p2.key
    assert c1.key == 13
    assert c2.key == 51
    
    p1, c1 = tree.find_parent_croot(38)
    assert p1.key == c1.key
    
    p1, c1 = tree.find_parent_croot(66)
    p2, c2 = tree.find_parent_croot(89)
    assert p1.key == p2.key
    
def test_right_most_child():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    parent, croot = tree.right_most_child(tree.root, tree.root.left)
    assert parent.key == 25
    assert croot.key == 37

def test_remove():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
            key = l.pop(0)
            value = chr(key)
            tree.insert(key, value)
    
    tree.remove(38)
    assert tree.root.key == 37
    assert tree.find(38) == None
    
    tree.remove(89)
    print(tree.in_order())
    p, c = tree.find_parent_croot(95)
    assert p.key == 84
    assert c.key == 95
    
    tree.remove(13)
    print(tree.in_order())
    p, c = tree.find_parent_croot(10)
    assert p.key == 12
    
    tree.remove(10)
    print(tree.in_order())
    tree.remove(12)
    print(tree.in_order())
    p, c = tree.find_parent_croot(25)
    assert p.key == 37
    
    
    


