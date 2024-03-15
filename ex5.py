# ex5.py

import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if not self.head or (data <= self.head.data):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next) and (current.next.data < data):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def dequeue(self):
        if self.head:
            element = self.head.data
            self.head = self.head.next
            return element
        else:
            return None

class HeapPriorityQueue:
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

def generate_tasks():
    tasks = []
    for i in range(1000):
        number = random.random()
        if (number < 0.7):
            tasks.append(("enqueue", random.randint(0, 500)))
        else:
            tasks.append(("dequeue", None))
    return tasks

def execute_task(queue, tasks):
    for task in tasks:
        if task[0] == "enqueue":
            queue.enqueue(task[1])
        else:
            queue.dequeue()

tasks = generate_tasks()

list_queue = ListPriorityQueue()
list_time = timeit.timeit(lambda: execute_task(list_queue, tasks), number = 1)

heap_queue = HeapPriorityQueue()
heap_time = timeit.timeit(lambda: execute_task(heap_queue, tasks), number = 1)

avg_list_time = list_time / 1000
avg_heap_time = heap_time / 1000

print(f'Total time for lists: {list_time} seconds. Average time per task: {avg_list_time}')
print(f'Time for heap: {heap_time} seconds. Average time per task: {avg_heap_time}')

# 4. The priority queue implementation using the heap was almost twice as fast as the
# implementation using the linked list. This is because the heap handles insertions/deletions
# efficiently, with a complexity of O(logn), whereas lists require list traversal for every 
# insertion and deletion operation, The complexity of which is O(n).