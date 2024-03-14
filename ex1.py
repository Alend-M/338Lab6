import sys
import timeit
import random
sys.setrecursionlimit(50000)

'''
1. Implement a binary search tree with insertion and search operations as
seen in class'''

 
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
    else:
        if node.key<key:
            node.right = insert(node.right, key)
        else:
            node.left = insert(node.left, key)
    return node
 
# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None:
        return "Not found"
    elif root.key == key: 
        return root.key
 
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
 
    # Key is smaller than root's key
    return search(root.left, key)


def test_bst():
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Search for 70 in the BST
    print("Searching for key 70:", search(r, 70))

    # Search for 90 in the BST
    print("Searching for key 90:", search(r, 90))

'''
2. Measure search performance using timeit as follows: [0.3 pts]
1. Generate a 10000-element sorted vector and use it to build a tree by inserting
each element
2. Search each element. Time the search (averaged across 10 tries for each element),
and return average and total time.'''
sorted_vector = [i for i in range(10000)]

tree = None

for i in sorted_vector:
    tree = insert(tree, i)

def perform_search():
    for i in sorted_vector:
        search(tree, i)

def measure_performance():
    n = 10
    search_time = timeit.timeit(perform_search, number=n)

    avg_time = search_time / (len(sorted_vector)*n)
    total_time = search_time / n

    print(f"Average search time across all elements = {avg_time:.6f} seconds")
    print(f"Total search time for all elements = {total_time:.6f} seconds")

'''Measure search performance using timeit as follows: [0.3 pts]
1. Shuffle the vector used for question 2 (using random.shuffle)
2. Search each element. Time the search (averaged across 10 tries for each element),
and return average and total time'''
measure_performance()
random.shuffle(sorted_vector)
print("after shuffling: ")
measure_performance()\

'''Average search time across all elements = 0.002060 seconds
Total search time for all elements = 20.596152 seconds
after shuffling: 
Average search time across all elements = 0.002153 seconds
Total search time for all elements = 21.533663 seconds'''

'''The total search time before shuffling is marginally faster than the total search time
after shuffling. Idk why***
'''