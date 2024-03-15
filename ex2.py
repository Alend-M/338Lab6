import timeit
import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def time_search_bst():
    data = [i for i in range(10000)]
    random.shuffle(data)
    root = None
    for item in data:
        root = insert(root, item)

    total_time = 0
    for _ in range(10):
        avg_time = timeit.timeit(lambda: search(root, random.choice(data)), number=1)
        total_time += avg_time

    avg_search_time = total_time / 10
    return avg_search_time, total_time

def time_binary_search():
    data = [i for i in range(10000)]
    random.shuffle(data)
    data.sort()

    total_time = 0
    for _ in range(10):
        avg_time = timeit.timeit(lambda: binary_search(data, random.choice(data)), number=1)
        total_time += avg_time

    avg_search_time = total_time / 10
    return avg_search_time, total_time

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

bst_avg_time, bst_total_time = time_search_bst()
binary_avg_time, binary_total_time = time_binary_search()

print(f"BST average search time:{bst_avg_time:0.3}")
print(f"BST total search time: {bst_total_time:0.3}")
print(f"Binary search average time: {binary_avg_time:0.3}")
print(f"Binary search total time: {binary_total_time:0.3}")

#Both search have average time complexity of O(log n) but if the tree isnt balanced it can degrade into a 
# complexity of o(n). Thus on the most part Binary Search will be faster because its consistantly a O(log n) algorithm.
