# %%
import math
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.recur_insert(self.root, data)
    
    def recur_insert(self, croot, data):
        if data < croot.data:
            if croot.left is None:
                croot.left = TreeNode(data)
            else:
                self.recur_insert(croot.left, data)
        else:
            if croot.right is None:
                croot.right = TreeNode(data)
            else:
                self.recur_insert(croot.right, data)
    
    def in_order(self):
        self.recur_in_order(self.root)
    
    def recur_in_order(self, croot):
        if croot is not None:
            self.recur_in_order(croot.left)
            print(croot.data)
            self.recur_in_order(croot.right)
    
    def level_order(self):
        if self.root is None: return
        queue = list()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data)
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
        stack = list()
        stack.append(self.root.data)
        
    def recur_print_paths(self, croot):
        
    
    def iter_in_order(self):
        if self.root is None: return
        # TODO: create a stack to store the current stage of traversal
    
    def print_tree(self):
        # h = self.height()
        # n_space = pow(2, h) # 2^h
        # # print(n_space)
        # s = ''
        # for i in range(0, n_space):
        #     s = f'{s} '
        # s = f'{s}{self.root.data}'
        # TODO: print tree using BFSs
        
        
    

tree = Tree()
tree.insert(8)
tree.insert(3)
tree.insert(7)
tree.insert(5)
tree.insert(6)
tree.insert(10)
# print('=======')
# tree.in_order()
# print('=======')
# tree.level_order()
# print('=======')
# tree.mirror()
# tree.in_order()
# print('=======')
# tree.level_order()
# print(tree.height())