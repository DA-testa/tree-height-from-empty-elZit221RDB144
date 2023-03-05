# python3

import sys
import threading
import numpy

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def tree_build(n, parents):
    nodes = [Node(i) for i in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
    return root

def get_height(root):
    if not root.children:
        return 1
    max_depth = 0
    for child in root.children:
        max_depth = max(max_depth, get_height(child))
    return max_depth+1
        

def compute_height(n, parents):
    root = tree_build(n, parents)
    return get_height(root)


def main():
    input_type = input().strip()
    if input_type == 'I':
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
    else:
        file = input().strip()
        if 'a' in file:
            print("Error")
            return
        with open (f"test/{file}") as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()