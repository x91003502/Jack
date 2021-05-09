########################################
#           Author: Jack Lin           #
########################################

import logging
import logging.config

# create logger
logging.config.fileConfig('src/logging.conf')
logger = logging.getLogger('priority_queue.py')

# zero-based priority queue
class PriorityQueue(object):
    
    def __init__(self, capacity: int, sortKey: str):
        '''
        Construct a new PriorityQueue object.
        
        :param capacity: The capacity of the priority queue
        :param sortKey: The key used to build a heap
        :return: returns nothing
        '''
        self.minHeap = list()
        self.size = 0
        self.capacity = capacity
        self.sortKey = sortKey
    
    def insert(self, obj):
        '''
        Inset an object in the PQ.
        If the PQ is full, remove the front element before 
        inserting the new element at the tail and REBUILD the heap.
        
        get method which will mess up the priority is used much more frequently 
        than insert, thus it would be more efficient the update the heap during the insertion.
        
        Time Complexity: 
            NOT FULL: O(log n)
            FULL: 2*O(log n)
        '''
        if (self.size < self.capacity):
            self.size += 1
            self.minHeap.append(obj)
            self.heapifyUp(self.size - 1)
            return None
        else:
            min = self.removeMin()
            self.size += 1
            self.minHeap.append(obj)
            self.heapifyUp(self.size - 1)
            return min
    
    def removeMin(self):
        '''
        Remove the element at the front.
        Time Complexity: O(log n)
        '''
        if (self.size == 0):
            print('Heap is empty.')
        else:
            logger.debug('\n==================== Remove from PQ ====================\n')
            min = self.minHeap[0]
            # self.minHeap[0] = self.minHeap[self.size - 1]
            self.swap(0, self.size - 1)
            del self.minHeap[-1]
            self.size -= 1
            self.heapifyDown(0)
            logger.debug(f'Object : {min} Has Been Removed.')
            return min
    
    def clear(self):
        self.minHeap.clear()
        self.size = 0
    
    def removeByIndex(self, index):
        '''
        Remove the element based on its index.
        Time Complexity: O(n) + O(log n)
        '''
        if (self.size == 0):
            print('Heap is empty.')
        else:
            logger.debug('\n==================== Remove from PQ ====================\n')
            remove = self.minHeap[index]
            self.minHeap[index] = self.minHeap[self.size - 1]
            
            for i in range(index, self.size):
                self.minHeap[i].index[0] -= 1
                print(self.minHeap[i].index)
            
            del self.minHeap[-1]
            self.size -= 1
            self.heapifyDown(index)
            logger.debug(f'Object : {remove.id} Has Been Removed.')
            return remove
    
    # def removeById(self, id):
    #     '''
    #     Remove the element based on its id.
    #     Time Complexity: O(n) + O(log n)
    #     '''
    #     if (self.size == 0):
    #         print('Heap is empty.')
    #     else:
    #         currIndex = self.findInexById(id)
    #         if (currIndex == -1):
    #             logger.debug(f'Object {0} Not Found.')
    #         else:
    #             logger.debug('\n==================== Remove from PQ ====================\n')
    #             self.minHeap[currIndex] = self.minHeap[self.size - 1]
    #             del self.minHeap[-1]
    #             self.size -= 1
    #             self.heapifyDown(currIndex)
    #             logger.debug(f'Object : {0} Has Been Removed.')
    
    def update(self, index):
        '''
        A simple way to update the PQ.
        Time Complexity: O(log n)
        '''
        logger.debug('\n==================== Update PQ ====================\n')
        self.heapifyDown(index)
    
    def buildHeap(self):
        '''
        Build Heap.
        Time Complexity: O(n)
        '''
        # python range(start, end) not include end
        for i in reversed(range(self.parent(self.size) + 1)):
            self.heapifyDown(i)
    
    def heapifyUp(self, currIndex):
        '''
        heapifyUp based on the sortKey which is specified when PQ is initialized.
        Time Complexity: O(log n)
        '''
        if (self.size > 1):
            parentIndex = self.parent(currIndex)
            if (self.getSortKeyValue(currIndex) < self.getSortKeyValue(parentIndex)):
                self.swap(currIndex, parentIndex)
    
    def heapifyDown(self, currIndex):
        '''
        heapifyDown based on the sortKey which is specified when PQ is initialized.
        Time Complexity: O(log n)
        '''
        if (self.hasAChild(currIndex)):
            minChildIndex = self.minChildIndex(currIndex)
            if (self.getSortKeyValue(currIndex) > self.getSortKeyValue(minChildIndex)):
                self.swap(currIndex, minChildIndex)
                self.heapifyDown(minChildIndex)
    
    def parent(self, currIndex):
        return int((currIndex - 1)/ 2)
    
    def hasAChild(self, currIndex):
        leftChildIndex = 2 * currIndex + 1
        if (leftChildIndex <= self.size - 1):
            return True
    
    def minChildIndex(self, currIndex):
        minChildIndex = 2 * currIndex + 1
        # If has two children
        if (minChildIndex < self.size - 1):
            if (self.getSortKeyValue(minChildIndex) > self.getSortKeyValue(minChildIndex + 1)):
                minChildIndex += 1
        return minChildIndex
    
    def swap(self, i, j):
        '''
        Swap two objects by their indices.
        Time Complexity: O(1)
        '''
        firstIndex = self.minHeap[i].index[0]
        secondIndex = self.minHeap[j].index[0]
    
        temp = self.minHeap[i]
        self.minHeap[i] = self.minHeap[j]
        self.minHeap[j] = temp
    
        self.minHeap[i].index[0] = firstIndex
        self.minHeap[j].index[0] = secondIndex
    
    def findInexById(self, id):
        '''
        Return the index of the object based on its id.
        If no object matches the given id, return -1.
        Time Complexity: O(n) (Linear Search)
        '''
        index = 0
        for elem in self.minHeap:
            if (elem.id == id):
                break
            else:
                index += 1
        if (index >= self.size):
            return -1
        else:
            return index
    
    def getSortKeyValue(self, index):
        return getattr(self.minHeap[index], self.sortKey)[0]
    
    def getPQ(self):
        res = dict()
        if (self.size == 0):
            print('Heap is empty.')
        else:
            for elem in self.minHeap:
                print(elem.count[0])
                data = {'count': elem.count[0], 'model_name': str(elem.id)}
                res.update(data)
        return res
    
    def isHeap(self):
        is_heap = True
        for i in reversed(range(self.parent(self.size) + 1)):
            if (self.hasAChild(i)):
                minChildIndex = self.minChildIndex(i)
                if(self.getSortKeyValue(i) > self.getSortKeyValue(minChildIndex)):
                    is_heap = False
                    logger.critical('PQ Bug')
                    # return is_heap
        return is_heap
    
    def printHeap(self):
        if (self.size == 0):
            logger.debug('Heap is empty.')
        else:
            logger.debug('\n==================== Heap Info ====================\n')
            for elem in self.minHeap:
                logger.debug(f'id : {elem.id}  index : {elem.index}  count : {elem.count}')
            logger.debug('\n===================================================\n')