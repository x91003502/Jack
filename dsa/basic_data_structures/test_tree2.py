import logging
import os.path
from tree2 import Tree

LOGGER = logging.getLogger(__name__)

def test_insert():
    tree = Tree()
    s = 10
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
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    
    assert tree.find(100) == None
    assert tree.find(50) == None
    assert tree.find(15) == None
    assert tree.find(39) == None
    
    # check parent except root node (38)
    assert tree.find(13).parent.key == tree.find(51).parent.key == 38
    assert tree.find(10).parent.key == tree.find(25).parent.key == 13
    assert tree.find(40).parent.key == tree.find(84).parent.key == 51
    assert tree.find(66).parent.key == tree.find(89).parent.key == 84
    
def test_right_most_child():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
    croot = tree.right_most_child(tree.root.left)
    assert croot.parent.key == 25
    assert croot.key == 37
    node = tree.find(13)
    croot = tree.right_most_child(node.left)
    assert croot.parent.key == 10
    assert croot.key == 12

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
    tree.remove(15)
    print(tree.in_order())
    p, c = tree.find_parent_croot(25)
    assert p.key == 37

def test_remove():
    tree = Tree()
    l = [38,13,51,10,25,40,84,12,37,66,89,95]
    length = len(l)
    while len(l) > 0:
            key = l.pop(0)
            value = chr(key)
            tree.insert(key, value)
    tree.remove(100)
    tree.remove(50)
    tree.remove(13)
    tree.remove(39)

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



