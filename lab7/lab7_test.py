import unittest
from lab7 import *

class TestLab7(unittest.TestCase):
    def test_traverse(self):
        self.assertEqual(traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn), 43)
        self.assertEqual(traverse([1,5,[10,7,14]], inner_node_fn, leaf_fn, empty_tree_fn), 6)
        self.assertEqual(traverse([[],7,[]], inner_node_fn, leaf_fn, empty_tree_fn), 7)
        self.assertEqual(traverse([[[1, 2, []], 4, [[], 5, 6]], 7, [[], 8, 9]], inner_node_fn, leaf_fn, empty_tree_fn), 14)
        self.assertEqual(traverse([[2, 3, []], 5, [6, 7, 8]], inner_node_fn, leaf_fn, empty_tree_fn),12)
        self.assertEqual(traverse([], inner_node_fn, leaf_fn, empty_tree_fn),0)
        self.assertEqual(traverse([[10, 4, [2, 3, [4, 5, 7]]], 5, [1, 2, [2, 3, 4]]],inner_node_fn, leaf_fn, empty_tree_fn),109)
        self.assertEqual(traverse([[4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, 2]]]]]], 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [2, 3, 4]]]]]]]], inner_node_fn, leaf_fn, empty_tree_fn),24)


    def test_contains_key(self):
        # Contains key test cases
        self.assertTrue(contains_key(7, [6, 7, 8]))
        self.assertFalse(contains_key(2, [[], 1, 5]))
        self.assertTrue(contains_key(5, [[1, 5, []], 4, [[], 5, 6]]))
        self.assertTrue(contains_key(4, [[[5, 3, 2], 4, []], 7, [[], 5, 6]]))
        self.assertFalse(contains_key(42, [[[5, 3, 2], 4, []], 7, [[], 5, 6]]))
        self.assertFalse(contains_key(0, []))  # Empty tree

    def test_tree_size(self):
        # Size test cases with various nested structures
        self.assertEqual(tree_size([2, 7, []]), 2)
        self.assertEqual(tree_size([]), 0)  # Empty tree
        self.assertEqual(tree_size([[[3, 1, 4], 8, [9, 10, 11]], 12, [[13, 14, 15], 16, [17, 18, 19]]]), 15)
        self.assertEqual(tree_size([[1, [2, [3, []]], 4], 5, [6, 7, []]]), 6)  # Deeply nested tree

    def test_tree_depth(self):
        # Depth test cases with varying depths
        self.assertEqual(tree_depth(9), 1)  # Single leaf
        self.assertEqual(tree_depth([[5, 6, 7], 8, [9, 10, 11]]), 3)  # Balanced tree
        self.assertEqual(tree_depth([[1, [2, [3, []]], 4], 5, [6, 7, []]]), 3)  # Unbalanced tree
        self.assertEqual(tree_depth([]), 0)  # Empty tree



if __name__ == '__main__':
    unittest.main()


    