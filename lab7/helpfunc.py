#Hjälp funktioner
def empty_tree_fn():
    ''' return 0 if tree is empty'''
    return 0

def leaf_fn(key):
    '''return key squared'''
    return key**2

def inner_node_fn(key, left_value, right_value):
    '''return key + left_value'''
    return key + left_value

def left_subtree(tree):
    '''return left subtree'''
    return tree[0]

def right_subtree(tree):
    '''return right subtree'''
    return tree[2]

def tree_key(tree):
    '''return key'''
    return tree[1]
    
def create_tree(left, key, right):
    '''return a tree'''
    return [left, key, right]

def is_empty(tree):
    '''return True if tree is empty, otherwise False'''
    return isinstance(tree, list) and len(tree) == 0

def is_leaf(tree):
    '''return True if tree is a leaf, otherwise False'''
    return isinstance(tree, int)



