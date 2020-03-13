def is_search_tree(binary_tree):
    '''
    :param binary_tree: a Node with value, left, and right attributes,
                        where left and right are None or Node
    :return: a bool indicating whether or not it is a binary search tree;
             i.e. values of all left nodes are less than a node's value
             and values of all right nodes are greater than a node's value.

    e.g.
       _1_
      /   \ - is not a BST because 2 > 1 (left > value)
     2    3

       _2_
      /   \ - is a BST because 2 > 1 (left < value) and 2 < 3 (right < value)
     1    3

    '''

    def is_bst(binary_tree, min, max):
        if binary_tree.value <= min:
            return False
        
        if binary_tree.value >= max:
            return False

        left_bst = True
        right_bst = True
        
        if binary_tree.left is not None:
            left_bst = is_bst(binary_tree.left, min, binary_tree.value)
        
        if binary_tree.right is not None:
            right_bst = is_bst(binary_tree.right, binary_tree.value, max)

        return left_bst and right_bst

    if binary_tree is None:
        return True

    return is_bst(binary_tree, float('-inf'), float('inf'))