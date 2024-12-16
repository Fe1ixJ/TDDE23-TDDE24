from helpfunc import *

#
def traverse(tree, inner_node_fn, leaf_fn, empty_fn):
    '''traverse tree and apply appropriate function to each node'''
    if is_empty(tree):
        return empty_fn()
    elif is_leaf(tree):
        return leaf_fn(tree)
    else:
        left = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_fn)
        right = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_fn)
        return inner_node_fn(tree_key(tree), left, right)


def contains_key(key, tree):
    '''return True if key is in tree, otherwise False'''
    def empty_tree():
        return False
    def leaf_fn(leaf):
        return key == leaf
    def inner_node_fn(tree_key, left, right):
        return key == tree_key or left or right
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree)

def tree_size(tree):
    ''' return the size of tree'''
    def empty_tree():
        return 0
    def leaf_fn(tree):
        return 1
    def inner_node_fn(tree_key, left, right):
        return 1 + left + right # komplettering
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree)

def tree_depth(tree):
    '''return the depth of tree'''
    def empty_tree():
        return 0
    def leaf_fn(tree):
        return 1
    def inner_node_fn(tree_key, left, right):
        return 1 + max(left, right) # Kompletting
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree)


# Run main tests
if __name__ == '__main__':
    print(traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn))
    print(contains_key(7, [6, 7, 8]))
    print(contains_key(2, [[],1,5]))
    print(tree_size([2,7,[]]))
    print(tree_size([]))
    print(tree_size([[1, 2, []], 4, [[], 5, 6]]))
    print(tree_depth(9))
    print(tree_depth([1,5,[10,7,14]]))