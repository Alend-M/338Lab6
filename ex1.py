# Note: code is working, just takes a long time

import random
import timeit
import sys

sys.setrecursionlimit(50000)

class Node:
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, root=None):
        if root is None:
            if self.root is None:
                self.root = Node(key)
                return self.root
            else:
                return self.insert(key, self.root)
        elif key <= root.data:
            if root.left is None:
                root.left = Node(key, root)
                return root.left
            else:
                return self.insert(key, root.left)
        else:
            if root.right is None:
                root.right = Node(key, root)
                return root.right
            else:
                return self.insert(key, root.right)

    def search(self, key):
        return self.recursive_search(self.root, key)

    def recursive_search(self, root, key):
        current = root
        while (current != None):
            if (key == current.data):
                return current
            elif (key > current.data):
                current = current.right
            else:
                current = current.left

def sorted_tree(array):
    tree = BinarySearchTree()
    for i in array:
        tree.insert(i)
    return tree

def measure_performance(tree, array):
    total_time = 0
    for i in array:
        time = timeit.timeit(lambda: tree.search(i), number = 10) / 10
        total_time += time
    return total_time / len(array), total_time

array = list(range(10000))
sorted_array = sorted_tree(array)
sorted_avg, sorted_time = measure_performance(sorted_array, array)

random.shuffle(array)
shuffled_array = sorted_tree(array)

shuffled_avg, shuffled_time = measure_performance(shuffled_array, array)

print(f'Total time for sorted array: {sorted_time}. Average time per task: {sorted_avg}')
print(f'Total time for shuffled array: {shuffled_time}. Average time per task: {shuffled_avg}')

# The shuffled vector is significantly faster than the sorted vector.
# This is because of the way a binary search tree is structured. When creating 
# a binary search tree with a sorted vector, the nodes will insert one at a time
# in a line, resembling the structure of a linked list. This would cause the insert
# and search operations to take longer as the entire tree would need to be traversed,
# leading to O(n) complexity. On the other hand, a shuffled vector turned into a BST 
# would be much quicker to search through as the item being searched for would be 
# found quicker in a more balanced tree. (complexity = O(logn))
