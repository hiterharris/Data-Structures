"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque
from stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # we know we need to go left
            # how do we know when we need to recurse again
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            # we know we need to go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # we keep going right until there are no more nodes on the right side
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def iterative_get_max(self):
        current_max = self.value
        current = self

        # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            # udate our current_max variable if we see larger value
            current = current.right


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call passed in function on the value of this node
        fn(self.value)

        # pass this function to the left child
        if self.left:
            self.left.for_each(fn)

        # pass this function to the right child
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create a node_stack
        node_stack = Stack()
        # push the current node onto stack
        node_stack.push(node)
        # while we have items on the stack
        while node_stack.size > 0:
            # print the current value and pop it off
            node = node_stack.pop()
            print(node.value)
            # push the left value of current node if we can
            if node.left is not None:
                node_stack.push(node.left)
            # push the right value of the current node if we can
            if node.right is not None:
                node_stack.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
