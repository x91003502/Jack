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
        # insert and rebalance
    
    def left_rotation(self, croot):
        # TODO: remeber to update parent and take care of root case

    def right_rotation(self, croot):
        # TODO: remeber to update parent and take care of root case
    
    def rebalance(self, croot):
        # TODO: take care of 4 cases of rotation operations
    
    def find(self, key):
    
    def recur_find(self, croot, key):
    
    def remove(self, key):
    
    def two_child_remove(self, croot):
    
    def zero_one_child_remove(self, croot):
    
    def right_most_child(self, croot):
    
    def in_order(self):
    
    def recur_in_order(self, croot, res):
    
    def height(self):
    
    def recur_height(self, croot):
    
    def recur_is_balanced(self, croot):
    
    def is_balanced(self, croot):
        # TODO: abs(h_left-h_right) <= 1