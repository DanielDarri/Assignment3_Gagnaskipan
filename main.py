from binary_search_tree import Pair, BinarySearchTree

def test0():
    tree = BinarySearchTree()
    tree.insert_key(20)
    tree.insert_key(30)
    tree.insert_key(40)
    tree.insert_key(10)
    print(tree)
    print(tree.is_in(10))
    print(tree.is_in(50))
    # For testing _before/_after_/_first/_last
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()
    print('==>', tree.pairs())
    print('=>', tree.keys())

def test1():
    tree = BinarySearchTree()
    keys = [50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55]
    for key in keys:
        tree.insert_key(key)
    print(tree)
    tree.delete(55)
    print(tree)
    tree.delete(20)
    print(tree)
    tree.delete(70)
    print(tree)
    tree.delete(50)
    print(tree)
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()

def test_is_empty():
    print("--- test_is_empty ---")
    tree = BinarySearchTree()
    print(tree.is_empty())          # True
    tree.insert_key(5)
    print(tree.is_empty())          # False

def test_clear():
    print("--- test_clear ---")
    tree = BinarySearchTree()
    tree.insert_key(1)
    tree.insert_key(2)
    tree.insert_key(3)
    tree.clear()
    print(tree.is_empty())          # True
    print(tree.keys())              # []

def test_insert_duplicate():
    print("--- test_insert_duplicate ---")
    tree = BinarySearchTree()
    print(tree.insert(Pair(10, 'a')))   # True (new insert)
    print(tree.insert(Pair(10, 'b')))   # False (update)
    print(tree.get(10))                 # 'b' (value was updated)

def test_get():
    print("--- test_get ---")
    tree = BinarySearchTree()
    tree.insert(Pair(10, 'cat'))
    tree.insert(Pair(20, 'dog'))
    tree.insert(Pair(5, 'bird'))
    print(tree.get(10))     # cat
    print(tree.get(20))     # dog
    print(tree.get(5))      # bird
    print(tree.get(99))     # None (does not exist)

def test_delete_edge_cases():
    print("--- test_delete_edge_cases ---")
    tree = BinarySearchTree()

    # Delete from empty tree
    print(tree.delete(10))      # False

    # Delete non-existent key
    tree.insert_key(10)
    print(tree.delete(99))      # False

    # Delete root with no children
    print(tree.delete(10))      # True
    print(tree.is_empty())      # True

    # Delete root with one child
    tree.insert_key(10)
    tree.insert_key(20)
    tree.delete(10)
    print(tree.keys())          # [20]

    # Delete root with two children
    tree.clear()
    tree.insert_key(10)
    tree.insert_key(5)
    tree.insert_key(20)
    tree.delete(10)
    print(tree.keys())          # [5, 20]

def test_single_node():
    print("--- test_single_node ---")
    tree = BinarySearchTree()
    tree.insert_key(42)
    print(tree.is_in(42))       # True
    print(tree.keys())          # [42]
    for pair in tree:
        print(pair.key)         # 42
    for pair in reversed(tree):
        print(pair.key)         # 42

def test_large_insert():
    print("--- test_large_insert ---")
    tree = BinarySearchTree()
    keys = list(range(1, 21))   # 1 to 20
    for key in keys:
        tree.insert_key(key)
    print(tree.keys())          # [1, 2, ..., 20]
    print(tree.is_in(15))       # True
    print(tree.is_in(99))       # False


# Some basic BST tests, add more tests as needed!
test0()
test1()
test_is_empty()
test_clear()
test_insert_duplicate()
test_get()
test_delete_edge_cases()
test_single_node()
test_large_insert()