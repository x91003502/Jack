import math
class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.recur_insert(self.root, key, value)
    
    def recur_insert(self, croot, key, value):
        # TODO: Use recursive helper function to insert tree node
        # if key is less than the key of current node, than go left
        # otherwise (equal or greater), go right
    
    def find(self, key):
        # TODO: return a tree node
    
    def recur_find(self, croot, key):
        # TODO: recursive helper function for find operation
    
    def find_parent_croot(self, key):
        parent = self.root
        croot = self.root
        return self.recur_find_parent_croot(parent, croot, key)
        # TODO: this function returns both the tree node with the given key
        # and also its parent node. This would be helpful for remove the node

    def recur_find_parent_croot(self, parent, croot, key):
        # TODO: helper function for finding nodes.
    
    def remove(self, key):
        # TODO: Implement the remove function
        # if ...: two_child_remove(self, parent, croot)
        # else: zero_one_child_remove(self, parent, croot)
    
    def two_child_remove(self, parent, croot):
        # We can devide the remove cases in two case.
        # In this case, it's more complicated, we need to find
        # the in order predecessor before remove operation
        iop_parent, iop = self.right_most_child(croot, croot.left)
        croot.key = iop.key
        croot.value = iop.value
        self.zero_one_child_remove(iop_parent, iop)
    
    def zero_one_child_remove(self, parent, croot):
        # Easier case for remove operation,
        # we can pass parent node and croot(current node, which is the node we want to delete)
        # if parent.left and the current node is the same node, 
        # we can connect parent of current node to children of current node. (similar to linkedlist)
        if parent.left is not None and parent.left.key == croot.key:
            # TODO
        elif parent.right is not None and parent.right.key == croot.key:
            # TODO
            
    
    def right_most_child(self, parent, croot):
        # Find the right most child with respect to croot node.
        # Example:
        #         38
        #      13
        #  10    25
        #    12     37
        #
        # when parent = 38, croot = 13, 
        # then you should return the most right child which is 37 and its paretn 25
        # TODO: return parent, croot
        
    def pre_order(self):
        res = list()
        return self.recur_pre_order(self.root, res)
    
    def recur_pre_order(self, croot, res):
        # TODO: Store the pre-order traversal to list

    
    def in_order(self):
        res = list()
        return self.recur_in_order(self.root, res)
    
    def recur_in_order(self, croot, res):
        # TODO: Store the in-order traversal to list

    
    def level_order(self):
        # TODO: Store the level-order traversal to list
        # Hint: you need to use queue.

    
    def height(self):
    

    def recur_height(self, croot):

        
    def mirror(self):
        if self.root is None: return
        self.recur_mirror(self.root)
        
    def recur_mirror(self, croot):
        # Before mirror
        #       1
        #    2     3
        #  6  7   8  9
        
        # After mirror
        #       1
        #    3     2
        #  7  6   9  8
        
    
    def print_paths(self):
        if self.root is None: return
        s = ''
        self.recur_print_paths(self.root, s)
        
    def recur_print_paths(self, croot, s):
        #     tree
        #       1
        #    3     2
        #  7  6   9  8
        
        # all paths: 
        # 137
        # 136
        # 129
        # 128
        