# %%
import math
class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    # def __del__(self):
    #     print(f'TreeNode with data {self.key} is destroyed')

class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.recur_insert(self.root, key, value)
    
    def recur_insert(self, croot, key, value):
        if key < croot.key:
            if croot.left is None:
                croot.left = TreeNode(key, value)
            else:
                self.recur_insert(croot.left, key, value)
        else:
            if croot.right is None:
                croot.right = TreeNode(key, value)
            else:
                self.recur_insert(croot.right, key, value)
    
    def find(self, key):
        return self.recur_find(self.root, key)
    
    def recur_find(self, croot, key):
        if croot is None: return None
        if key == croot.key: return croot
        elif key < croot.key:
            return self.recur_find(croot.left, key)
        else:
            return self.recur_find(croot.right, key)
    
    def find_parent_croot(self, key):
        parent = self.root
        croot = self.root
        return self.recur_find_parent_croot(parent, croot, key)

    def recur_find_parent_croot(self, parent, croot, key):
        if croot is None: return None
        if key == croot.key: return parent, croot
        elif key < croot.key:
            return self.recur_find_parent_croot(croot, croot.left, key)
        else:
            return self.recur_find_parent_croot(croot, croot.right, key)
    
    def remove(self, key):
        parent, croot = self.find_parent_croot(key)
        if croot.left is not None and croot.right is not None:
            self.two_child_remove(parent, croot)
        else:
            self.zero_one_child_remove(parent, croot)
    
    def two_child_remove(self, parent, croot):
        iop_parent, iop = self.right_most_child(croot, croot.left)
        croot.key = iop.key
        croot.value = iop.value
        # iop_parent.right = None
        self.zero_one_child_remove(iop_parent, iop)
        # self.zero_one_child_remove(iop)
    
    def zero_one_child_remove(self, parent, croot):
        if parent.left is not None and parent.left.key == croot.key:
            if croot.left is None:
                parent.left = croot.right
            else:
                parent.left = croot.left
        elif parent.right is not None and parent.right.key == croot.key:
            if croot.left is None:
                parent.right = croot.right
            else:
                parent.right = croot.left
    
    def right_most_child(self, parent, croot):
        if croot.right is None: return parent, croot
        else: return self.right_most_child(croot, croot.right)
        
    def pre_order(self):
        res = list()
        return self.recur_pre_order(self.root, res)
    
    def recur_pre_order(self, croot, res):
        if croot is not None:
            res.append(croot.key)
            # print(croot.key)
            self.recur_pre_order(croot.left, res)
            self.recur_pre_order(croot.right, res)
        return res
    
    def in_order(self):
        res = list()
        return self.recur_in_order(self.root, res)
    
    def recur_in_order(self, croot, res):
        if croot is not None:
            self.recur_in_order(croot.left, res)
            res.append(croot.key)
            # print(croot.key)
            self.recur_in_order(croot.right, res)
        return res
    
    def level_order(self):
        if self.root is None: return
        queue = list()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    def height(self):
        if self.root is None: return -1
        else: return self.recur_height(self.root)
    
    def recur_height(self, croot):
        if croot is None: return -1
        else: return 1 + max(self.recur_height(croot.left), self.recur_height(croot.right))
        
    def mirror(self):
        if self.root is None: return
        self.recur_mirror(self.root)
        
    def recur_mirror(self, croot):
        if croot is None: return
        left_child = croot.left
        croot.left = croot.right
        croot.right = left_child
        self.recur_mirror(croot.left)
        self.recur_mirror(croot.right)
    
    def print_paths(self):
        if self.root is None: return
        s = ''
        self.recur_print_paths(self.root, s)
        
    def recur_print_paths(self, croot, s):
        s = f'{s} {croot.data}'
        if croot.left is None and croot.right is None:
            print(s)
        if croot.left is not None:
            self.recur_print_paths(croot.left, s)
        if croot.right is not None:
            self.recur_print_paths(croot.right, s)
        
    
    # def iter_in_order(self):
        # if self.root is None: return
        # TODO: create a stack to store the current stage of traversal
    
    # def print_tree(self):
        # h = self.height()
        # n_space = pow(2, h) # 2^h
        # # print(n_space)
        # s = ''
        # for i in range(0, n_space):
        #     s = f'{s} '
        # s = f'{s}{self.root.key}'
        # TODO: print tree using BFSs


tree = Tree()
l = [38,13,51,10,25,40,84,12,37,66,89,95]
length = len(l)
while len(l) > 0:
        key = l.pop(0)
        value = chr(key)
        tree.insert(key, value)
print(tree.in_order())
tree.remove(38)
print(tree.in_order())
tree.remove(89)
print(tree.in_order())
tree.remove(13)
print(tree.in_order())
tree.remove(10)
print(tree.in_order())
tree.remove(12)
print(tree.in_order())