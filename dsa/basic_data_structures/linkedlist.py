# %%
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
    def __del__(self):
        print(f'Node with data {self.data} is destroyed')

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push_front(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        self.size += 1
    
    def push_back(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            # traverse to the last node
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            self.size += 1
    
    def insert_after(self, prev_data, new_data):
        if self.is_empty: return
        new_node = Node(new_data)
        prev = self.find_prev(prev_data)
        if prev is None:
            print(f'Node with data = {prev_data} is not found')
            return
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
    
    def remove_front(self):
        if self.is_empty(): return
        elif self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
    
    def remove_back(self):
        if self.is_empty(): return
        elif self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            data = curr.next.data
            curr.next = None
            self.size -= 1
            return data
    
    def remove(self, data):
        prev = self.find_prev(data)
        if prev is None: return
        if prev == self.head:
            self.remove_front()
            return
        curr = prev.next
        prev.next = curr.next
        self.size -= 1
    
    def peek(self):
        return self.head.data
    
    def find_prev(self, data):
        if self.is_empty(): return
        curr = self.head
        if curr.data == data: 
            print(f'first Node data {data}')
            return curr
        
        while curr.next is not None and curr.next.data != data:
            curr = curr.next
        if curr.next is None:
            print('not found')
            return None
        else:
            print(f'previous Node data {curr.data}')
            return curr
    
    def is_empty(self):
        if self.size == 0:
            print('Empty')
            return True
        else:
            return False

    def print_list(self):
        curr = self.head
        print('========== print list ==========')
        while curr is not None:
            print(curr.data)
            curr = curr.next

# llist = LinkedList()
# llist.push_front(2)
# llist.print_list()

# llist.push_front(1)
# llist.print_list()

# llist.push_back(3)
# llist.print_list()

# llist = LinkedList()
# llist.push_front(2)

## Test remove
llist = LinkedList()
for i in range(0, 10):
    llist.push_front(i)

llist.remove(2)
llist.print_list()

# ## Test remove

# llist = LinkedList()
# llist.remove(9)
# llist.print_list()
