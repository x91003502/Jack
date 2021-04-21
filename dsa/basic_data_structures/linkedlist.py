
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

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
    
    def remove_front(self):
        if self.size == 0:
            print('Empty')
            return
        elif self.size == 1:
            curr = self.head
            self.head = None
            self.size -= 1
            return curr.data
        else:
            curr = self.head
            self.head = curr.next
            self.size -= 1
            return curr.data
    
    # def remove_back(self):
    #     if self.size == 0:
    #         print('Empty')
    #         return
    #     elif self.size == 1:
    #         curr = self.head
    #         self.head = None
    #         self.size -= 1
    #         return curr.data
    #     else:
    #         curr = self.head
    #         while curr.next.next is not None:
    #             curr = curr.next
    
    def peek(self):
        return self.head.data
    
    def print_list(self):
        curr = self.head
        print('========== print list ==========')
        while curr is not None:
            print(curr.data)
            curr = curr.next

llist = LinkedList()
llist.push_front(2)
llist.print_list()

llist.push_front(1)
llist.print_list()

llist.push_back(3)
llist.print_list()
