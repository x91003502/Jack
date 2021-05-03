# %%
import math
class TreeNode(object):
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    
    # def __del__(self):
    #     print(f'TreeNode with data {self.key} is destroyed')

class AVL(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
            # self.root.parent = self.root
        else:
            croot = self.find(key)
            if key == croot.key:
                print('key already exists')
                return
            if key < croot.key:
                croot.left = TreeNode(key, value, croot)
            else:
                croot.right = TreeNode(key, value, croot)
            b = self.recur_is_balanced(croot)
            if isinstance(b, TreeNode):
                print(f'not balanced, lowest unbalanced root found : {b.key}')
                self.left_rotation(b)
    
    def left_rotation(self, croot):
        print('left_rotation')
        subroot = croot.right
        parent = croot.parent
        croot.right = subroot.left
        subroot.left = croot
        croot.parent = subroot

        # croot = subroot
        if parent is None:
            self.root = subroot
            subroot.parent = None
        else:
            parent.right = subroot
            subroot.parent = parent
        
        # subroot = croot.right
        # parent = croot.parent
        
        # croot.right = subroot.left
        
        # subroot.left = croot
        # parent.right = subroot
        # if croot == self.root:
        #     print(subroot)
        #     self.root = subroot
        # croot.parent = subroot
        # subroot.parent = parent
    
    def find(self, key):
        return self.recur_find(self.root, key)
    
    def recur_find(self, croot, key):
        if key == croot.key: return croot
        if key < croot.key and croot.left is not None:
            return self.recur_find(croot.left, key)
        elif key < croot.key and croot.left is None:
            print(f'key {key} not found, return a parent node {croot.key}')
            return croot
        
        if key > croot.key and croot.right is not None:
            return self.recur_find(croot.right, key)
        elif key > croot.key and croot.right is None:
            print(f'key {key} not found, return a parent node {croot.key}')
            return croot

# tree = AVL()
# l = [1,2,4,3,5]
# length = len(l)
# while len(l) > 0:
#     key = l.pop(0)
#     value = chr(key)
#     tree.insert(key, value)
#     print(f'in order {tree.in_order()}')

