import logging
import os.path
from tree2 import Tree

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

def test_insert2():
    tree = Tree()
    s = 100
    for i in range(0, s):
        tree.insert(i, i)
    
    # try to insert again
    for i in range(0, 10):
        tree.insert(i, i+1)
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

def test_in_order_pre_order_level_order():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    in_order = tree.in_order()
    pre_order = tree.pre_order()
    level_order = tree.level_order()
    assert in_order ==  [10,12,13,25,37,38,40,51,66,84,89,95]
    assert pre_order == [38,13,10,12,25,37,51,40,84,66,89,95]
    assert level_order == [38,13,51,10,25,40,84,12,37,66,89,95]

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

def test_find2():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    assert tree.find(100).key == 95
    assert tree.find(50).key == 40
    assert tree.find(39).key == 40
    assert tree.find(15).key == 25
    
def test_right_most_child():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    croot = tree.right_most_child(tree.root.left)
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
    assert tree.find(13).parent.key == 37
    assert tree.find(51).parent.key == 37
    assert tree.find(38).key == 40
    
    tree.remove(89)
    assert tree.find(95).key == 95
    assert tree.find(95).parent.key == 84
    
    
    tree.remove(13)
    assert tree.find(13).key == 25
    assert tree.find(12).parent.key == 37
    assert tree.find(10).parent.key == 12
    assert tree.find(25).parent.key == 12


def test_remove2():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
            key = l.pop(0)
            value = chr(key)
            tree.insert(key, value)
    tree.remove(100)
    tree.remove(50)
    tree.remove(14)
    tree.remove(39)
    assert len(tree.in_order()) == length


def test_remove3():
    tree = Tree()
    s = 100
    for i in range(0, s):
        tree.insert(i, i)
    
    for i in range(0, s):
        tree.remove(i)

def test_remove4():
    tree = Tree()
    s = 100
    for i in reversed(range(0, s)):
        tree.insert(i, i)
    
    for i in reversed(range(0, s)):
        tree.remove(i)

import random
def test_remove5():
    
    tree = Tree()
    l = list()
    s = 100
    for i in range(0, s):
        tree.insert(i, i)

    for i in range(0, s):
        l.append(i)
    random.shuffle(l)
    
    size = 100
    while len(l) > 1:
        key = l.pop()
        tree.remove(key)
        size -= 1
        assert len(tree.in_order()) == size
        croot = tree.find(key)
        assert croot.key != key


def test_mirror():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
            key = l.pop(0)
            value = chr(key)
            tree.insert(key, value)
    level_order = tree.level_order()
    assert level_order == [38,13,51,10,25,40,84,12,37,66,89,95]
    tree.mirror()
    level_order = tree.level_order()
    pre_order = tree.pre_order()
    assert level_order == [38,51,13,84,40,25,10,89,66,37,12,95]
    assert pre_order == [38,51,84,89,95,66,40,13,25,37,10,12]


def test_print_paths():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
            key = l.pop(0)
            value = chr(key)
            tree.insert(key, value)
    l =tree.print_paths()
    assert l[0] == ' 38 13 10 12'
    assert l[1] == ' 38 13 25 37'
    assert l[2] == ' 38 51 40'
    assert l[3] == ' 38 51 84 66'
    assert l[4] == ' 38 51 84 89 95'