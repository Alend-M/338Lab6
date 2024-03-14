import timeit
import random



class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)


def build_tree(sorted_vector):
    bst = BST()
    for key in sorted_vector:
        bst.insert(key)
    return bst

def measure_performance(sorted_vector):
    bst = build_tree(sorted_vector)
    n = 10
    total_search_time = 0

    for key in sorted_vector:
        search_time = timeit.timeit(lambda: bst.search(key), number=n)
        total_search_time += search_time

    avg_time = total_search_time / (len(sorted_vector) * n)
    total_time = total_search_time / n

    print(f"Average search time across all elements = {avg_time:.6f} seconds")
    print(f"Total search time for all elements = {total_time:.6f} seconds")

# Generate a 10000-element sorted vector
sorted_vector = [i for i in range(10000)]
# Shuffle the vector
random.shuffle(sorted_vector)

# Measure performance
measure_performance(sorted_vector)


'''3. Using the same shuffled vector from question 2: [0.3 pts]
1. Sort the vector
2. Search each element using binary search. Time the search (averaged across 10
tries for each element), and return average and total time
4. Discuss: which approach is faster? Why do you think is that? [0.2 pts]
'''

#what do you mean the Same shuffled vector??? how tf????