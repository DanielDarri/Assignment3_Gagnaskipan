from binary_search_tree import Pair, BinarySearchTree
from my_dict import MyDict
from word_freq import word_frequency_alphabetical_pydict, word_frequency_alphabetical_mydict

def test0():
    tree = BinarySearchTree()
    tree.insert_key(20)
    tree.insert_key(30)
    tree.insert_key(40)
    tree.insert_key(10)
    print(tree)
    print(tree.is_in(10))
    print(tree.is_in(50))
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
    print(tree.delete(10))      # False
    tree.insert_key(10)
    print(tree.delete(99))      # False
    print(tree.delete(10))      # True
    print(tree.is_empty())      # True
    tree.insert_key(10)
    tree.insert_key(20)
    tree.delete(10)
    print(tree.keys())          # [20]
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
    keys = list(range(1, 21))
    for key in keys:
        tree.insert_key(key)
    print(tree.keys())          # [1, 2, ..., 20]
    print(tree.is_in(15))       # True
    print(tree.is_in(99))       # False

def test_mydict_basic():
    print("--- test_mydict_basic ---")
    d = MyDict()
    d[10] = 'cat'
    d[20] = 'dog'
    d[5] = 'bird'
    print(d[10])        # cat
    print(d[20])        # dog
    print(d[5])         # bird
    print(d)            # {5: bird, 10: cat, 20: dog}

def test_mydict_len():
    print("--- test_mydict_len ---")
    d = MyDict()
    print(len(d))       # 0
    d[1] = 'a'
    d[2] = 'b'
    d[3] = 'c'
    print(len(d))       # 3
    d[2] = 'z'
    print(len(d))       # 3
    del d[1]
    print(len(d))       # 2

def test_mydict_get():
    print("--- test_mydict_get ---")
    d = MyDict()
    d[1] = 'hello'
    print(d.get(1))             # hello
    print(d.get(99))            # None
    print(d.get(99, 'default')) # default

def test_mydict_update():
    print("--- test_mydict_update ---")
    d = MyDict()
    d[10] = 'cat'
    print(d[10])        # cat
    d[10] = 'lion'
    print(d[10])        # lion
    print(len(d))       # 1

def test_mydict_delete():
    print("--- test_mydict_delete ---")
    d = MyDict()
    d[1] = 'a'
    d[2] = 'b'
    d[3] = 'c'
    del d[2]
    print(len(d))       # 2
    print(list(d))      # [1, 3]
    try:
        del d[99]
        print("ERROR: should have raised KeyError")
    except KeyError:
        print("KeyError raised correctly")

def test_mydict_getitem_keyerror():
    print("--- test_mydict_getitem_keyerror ---")
    d = MyDict()
    d[1] = 'a'
    try:
        _ = d[99]
        print("ERROR: should have raised KeyError")
    except KeyError:
        print("KeyError raised correctly")

def test_mydict_iter():
    print("--- test_mydict_iter ---")
    d = MyDict()
    d[30] = 'c'
    d[10] = 'a'
    d[20] = 'b'
    for key in d:
        print(key, end=' ')     # 10 20 30
    print()

def test_mydict_empty():
    print("--- test_mydict_empty ---")
    d = MyDict()
    print(len(d))       # 0
    print(list(d))      # []
    print(str(d))       # {}
    try:
        del d[1]
        print("ERROR: should have raised KeyError")
    except KeyError:
        print("KeyError raised correctly")

def test_word_frequency_basic():
    print("--- test_word_frequency_basic ---")
    text = "I am so so happy happy Happy"
    expected = [('am', 1), ('happy', 3), ('i', 1), ('so', 2)]
    result_py = word_frequency_alphabetical_pydict(text)
    result_my = word_frequency_alphabetical_mydict(text)
    print(result_py)            # [('am', 1), ('happy', 3), ('i', 1), ('so', 2)]
    print(result_my)            # [('am', 1), ('happy', 3), ('i', 1), ('so', 2)]
    print(result_py == expected)    # True
    print(result_my == expected)    # True
    print(result_py == result_my)   # True

def test_word_frequency_punctuation():
    print("--- test_word_frequency_punctuation ---")
    text = "hello, hello. world! world world?"
    expected = [('hello', 2), ('world', 3)]
    result_py = word_frequency_alphabetical_pydict(text)
    result_my = word_frequency_alphabetical_mydict(text)
    print(result_py)            # [('hello', 2), ('world', 3)]
    print(result_py == expected)    # True
    print(result_py == result_my)   # True

def test_word_frequency_single_word():
    print("--- test_word_frequency_single_word ---")
    text = "python"
    expected = [('python', 1)]
    result_py = word_frequency_alphabetical_pydict(text)
    result_my = word_frequency_alphabetical_mydict(text)
    print(result_py == expected)    # True
    print(result_py == result_my)   # True

def test_word_frequency_empty():
    print("--- test_word_frequency_empty ---")
    text = ""
    expected = []
    result_py = word_frequency_alphabetical_pydict(text)
    result_my = word_frequency_alphabetical_mydict(text)
    print(result_py == expected)    # True
    print(result_py == result_my)   # True

def test_word_frequency_alphabetical_order():
    print("--- test_word_frequency_alphabetical_order ---")
    text = "zebra apple mango apple zebra zebra"
    expected = [('apple', 2), ('mango', 1), ('zebra', 3)]
    result_py = word_frequency_alphabetical_pydict(text)
    result_my = word_frequency_alphabetical_mydict(text)
    print(result_py)            # [('apple', 2), ('mango', 1), ('zebra', 3)]
    print(result_py == expected)    # True
    print(result_py == result_my)   # True

def test_word_frequency_match():
    print("--- test_word_frequency_match ---")
    # Both implementations should always produce identical results
    text = "the quick brown fox jumps over the lazy dog the fox"
    result_py = word_frequency_alphabetical_pydict(text)
    result_my = word_frequency_alphabetical_mydict(text)
    print(result_py)
    print(result_py == result_my)   # True


# BST tests
test0()
test1()
test_is_empty()
test_clear()
test_insert_duplicate()
test_get()
test_delete_edge_cases()
test_single_node()
test_large_insert()

# MyDict tests
test_mydict_basic()
test_mydict_len()
test_mydict_get()
test_mydict_update()
test_mydict_delete()
test_mydict_getitem_keyerror()
test_mydict_iter()
test_mydict_empty()

# Word frequency tests
test_word_frequency_basic()
test_word_frequency_punctuation()
test_word_frequency_single_word()
test_word_frequency_empty()
test_word_frequency_alphabetical_order()
test_word_frequency_match()
