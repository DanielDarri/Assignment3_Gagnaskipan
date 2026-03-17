#
# BST - Trees (Binary Search Trees)
# Your name:
#  - <Daníel Darri Ragnarsson>
#
from interface.binary_search_tree_abc import Pair, IBinarySearchTree


class BinarySearchTree(IBinarySearchTree):
    """
    A class for a binary search tree, storing (key, value) pairs.
    Only unique key values are allowed.
    IMPORTANT:
        - You are not allowed to change the interface of the existing class methods (public/private),
          nor the _Note class. Doing so will result in non-graded submission.
          However, feel free to add other helper methods as you see fit.
    """

    # --------------------------------------------------------------------------------------
    # Private helper methods and classes (hint: once implemented try to reuse them as
    # much as possible in your public methods).
    # --------------------------------------------------------------------------------------

    class _Node:
        """
        The node class for creating the nodes in the tree (Do not change!).
        """
        def __init__(self, parent, left, right, pair: Pair):
            self.parent = parent
            self.left = left
            self.right = right
            self.pair = pair

    def _representation(self, node: _Node) -> str:
        if node is None:
            return "-"
        l = self._representation(node.left)
        r = self._representation(node.right)
        return '(' + str(node.pair) + ' ' + l + ' ' + r + ')'

    # The __iter__ and __reversed__ will be used to test the _first/_last/_before/_after methods.
    def __iter__(self):
        node = self._first()
        while node is not None:
            yield node.pair
            node = self._after(node)

    def __reversed__(self):
        node = self._last()
        while node is not None:
            yield node.pair
            node = self._before(node)

    def _first(self) -> _Node | None:
        """
        In a non-empty tree, returns the minimum key node (first in an inorder traversal), otherwise None.
        """
        if self._root is None:
            return None
        node = self._root
        while node.left is not None:
            node = node.left
        return node
        

    def _last(self) -> _Node | None:
        """
        In a non-empty tree, returns the maximum key node (last in an inorder traversal), otherwise None.
        """
        if self._root is None:
            return None
        node = self._root
        while node.right is not None:
            node = node.right
        return node

    def _before(self, node: _Node) -> _Node | None:
        """
        Returns the in-order predecessor of node, or None if it does not exist.
        """
        if node.left is not None:
            curr = node.left
            while curr.right is not None:
                curr = curr.right
            return curr
        
        curr = node
        while curr.parent is not None:
            if curr is curr.parent.right:
                return curr.parent
            curr = curr.parent
        return None

    def _after(self, node: _Node) -> _Node | None:
        """
        Returns the in-order successor of node, or None if it does not exist.
        """
        if node.right is not None:
            curr = node.right
            while curr.left is not None:
                curr = curr.left
            return curr
        
        curr = node
        while curr.parent is not None:
            if curr is curr.parent.left:
                return curr.parent
            curr = curr.parent
        return None

    # --------------------------------------------------------------------------------------
    # Public methods, implementing the abstract-base-class interface.
    # --------------------------------------------------------------------------------------

    def __init__(self):
        # This is the only member variable you need. Do not change the constructor.
        self._root = None

    def __str__(self) -> str:
        """
        Returns a string representation of the tree.
        """
        return self._representation(self._root)

    def insert_key(self, key: object) -> bool:  # Method is non-essential, but added for testing convenience.
        """
        Insert (key, None) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, None) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        return self.insert(Pair(key, None))

    def keys(self) -> list[object]: # Method is non-essential, but added for testing convenience.
        """
        Returns a list of all the keys in the tree, in an increasing order.
        """
        return [pair.key for pair in self.pairs()]

    def insert(self, pair: Pair) -> bool:
        """
        Insert (key, value) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, value) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        # TO DO
        if self._root is None:
            self._root = self._Node(None, None, None, pair)
            return True
        
        curr = self._root
        while curr is not None:
            if pair.key == curr.pair.key:
                curr.pair = pair
                return False
            elif pair.key < curr.pair.key:
                if curr.left is None:
                    curr.left = self._Node(curr, None, None, pair)
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = self._Node(curr, None, None, pair)
                    return True
                curr = curr.right

    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty, False otherwise.
        """
        if self._root is None:
            return True
        else:
            return False

    def is_in(self, key: object) -> bool:
        """
        Returns True if an element with key is in the tree, otherwise False.
        """
        curr = self._root
        while curr is not None:
            if key == curr.pair.key:
                return True
            elif key < curr.pair.key:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def get(self, key: object) -> object:
        """
        Returns the value of the element with the given key, or None if the key does not exist.
        """
        curr = self._root
        while curr is not None:
            if key == curr.pair.key:
                return curr.pair.value
            elif key < curr.pair.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def pairs(self) -> list[Pair]:
        """
        Returns a list of all the (key, value) pairs in the tree, in an increasing order.
        """
        return list(self)

    def clear(self):
        """
        Removes all elements from the tree (tree becomes empty).
        """
        self._root = None

    def delete(self, key: object) -> bool:
        """
        Deletes the element with key, if exists.
        Returns True if the element was deleted (existed), otherwise False (does not exist).
        """
        curr = self._root
        while curr is not None:
            if key == curr.pair.key:
                break
            elif key < curr.pair.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return False
        
        #Case 1 node has two children
        if curr.left is not None and curr.right is not None:
            successor = self._after(curr)
            curr.pair = successor.pair
            curr = successor
        
        #case 2 & 3 node has zero or one child
        child = curr.left if curr.left is not None else curr.right

        if child is not None:
            child.parent = curr.parent
        
        if curr.parent is None:
            self._root = child
        elif curr is curr.parent.left:
            curr.parent.left = child
        else:
            curr.parent.right = child
        
        return True
