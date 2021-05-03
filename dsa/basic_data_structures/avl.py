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
            node = self.recur_is_balanced(croot)
            if isinstance(node, TreeNode):
                print(f'not balanced, lowest unbalanced root found : {node.key}')
                
                # if right subtree is higher
                if self.recur_height(node.right) > self.recur_height(node.left): 
                    if self.recur_height(node.right.right) > self.recur_height(node.right.left):
                        print('left rotation')
                        self.left_rotation(node)
                    else:
                        print('right left rotation')
                        self.right_rotation(node.right)
                        self.left_rotation(node)
                
                # if left subtree is higher
                else:
                    if self.recur_height(node.left.left) > self.recur_height(node.left.right):
                        print('right rotation')
                        self.right_rotation(node)
                    else:
                        print('left right rotation')
                        self.left_rotation(node.right)
                        self.right_rotation(node)
    
    def left_rotation(self, croot):
        subroot = croot.right
        parent = croot.parent
        croot.right = subroot.left
        subroot.left = croot
        croot.parent = subroot

        if parent is None:
            self.root = subroot
            subroot.parent = None
        else:
            parent.left = subroot
            subroot.parent = parent

    def right_rotation(self, croot):
        subroot = croot.left
        parent = croot.parent
        croot.left = subroot.right
        subroot.right = croot
        croot.parent = subroot

        if parent is None:
            self.root = subroot
            subroot.parent = None
        else:
            parent.right = subroot
            subroot.parent = parent

    def find(self, key):
        return self.recur_find(self.root, key)
    
    def recur_find(self, croot, key):
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
        
        if croot.left.key == key: return croot.left
        if croot.right.key == key: return croot.right
    
    def remove(self, key):
        croot = self.find(key)
        if croot is None:
            print('key not found')
            return
        if croot.left is not None and croot.right is not None:
            self.two_child_remove(croot)
        else:
            self.zero_one_child_remove(croot)
    
    def two_child_remove(self, croot):
        iop = self.right_most_child(croot.left)
        croot.key = iop.key
        croot.value = iop.value
        self.zero_one_child_remove(iop)
    
    def zero_one_child_remove(self, croot):
        parent = croot.parent
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
    
    def right_most_child(self, croot):
        if croot.right is None: return croot
        else: return self.right_most_child(croot.right)
        
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
        res = list()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            # print(node.key)
            res.append(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return res
    
    def height(self):
        if self.root is None: return -1
        else: return self.recur_height(self.root)
    
    def recur_height(self, croot):
        if croot is None: return -1
        else: return 1 + max(self.recur_height(croot.left), self.recur_height(croot.right))
    
    def recur_is_balanced(self, croot):
        b = self.is_balanced(croot)
        if b is True and croot.parent != None:
            return self.is_balanced(croot.parent)
        else:
            return b
        # elif isinstance(b, TreeNode)
        #     print('find lowest unbalanced tree')
        #     return croot
    
    def is_balanced(self, croot):
        h_left = self.recur_height(croot.left)
        h_right = self.recur_height(croot.right)
        if abs(h_left-h_right) <= 1:
            return True
        else:
            return croot   
    
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
        l = list()
        self.recur_print_paths(self.root, s, l)
        return l
        
    def recur_print_paths(self, croot, s, l):
        s = f'{s} {croot.key}'
        if croot.left is None and croot.right is None:
            # print(s)
            l.append(s)
        if croot.left is not None:
            self.recur_print_paths(croot.left, s, l)
        if croot.right is not None:
            self.recur_print_paths(croot.right, s, l)

tree = AVL()
# l = [5,4,3,2]
# l = [2,4,3]
l = [1,2,3]
length = len(l)
while len(l) > 0:
    key = l.pop(0)
    value = chr(key)
    tree.insert(key, value)
    print(f'level order {tree.level_order()}')