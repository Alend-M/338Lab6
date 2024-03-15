# ex4.py

import timeit
import random

class Heap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, array):
        self.heap = array
        for i in range(len(array) // 2 - 1, -1, -1):
            self.heapifyDown(i)
    
    def enqueue(self, item):
        self.heap.append(item)
        self.heapifyUp(len(self.heap) - 1)
    
    def dequeue(self):
        if len(self.heap) > 0:
            self.swap(0, len(self.heap) - 1)
            element = self.heap.pop()
            self.heapifyDown(0)
            return element
        else:
            return None
        
    def heapifyUp(self, index):
        parent = (index - 1) // 2
        while (index > 0) and (self.heap[index] < self.heap[parent]):
            self.swap(index, parent)
            index, parent = parent, (parent - 1) // 2
    
    def heapifyDown(self, index):
        size = len(self.heap)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        min = index
        if left_child < size and self.heap[left_child] < self.heap[min]:
            min = left_child
        if right_child < size and self.heap[right_child] < self.heap[min]:
            min = right_child
        if min != index:
            self.swap(index, min)
            self.heapifyDown(min)
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def testSortedHeap():
    heap = Heap()
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heap.heapify(array)
    expectedValue = array
    assert heap.heap == expectedValue, "Sorted heap test failed."

def testEmptyHeap():
    heap = Heap()
    array = []
    heap.heapify(array)
    expectedValue = []
    assert heap.heap == expectedValue, "Empty heap test failed."

def testLargeRandomHeap():
    heap = Heap()
    array = [random.sample(range(200), 50)]
    expectedValue = sorted(array)
    heap.heapify(array)
    assert heap.heap == expectedValue, "Randomized array test failed."

testSortedHeap()
testEmptyHeap()
testLargeRandomHeap()

print("All tests ran, no failures.")