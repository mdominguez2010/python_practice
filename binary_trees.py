# Page 116 of EOPI
# Binary Trees bootcamp

def tree_traversal(root: BinaryTreeNode):
    if root:
        # Preorder: Processes the root before the traversals fo left and right children
        print('PreorderL %d' % root.data)
        tree_traversal(root.left)
        # Inorder: Processes the root after the traversal of left child and before
        # traversal of right child
        print('Inorder: %d' % root.data)
        tree_traversal(root.right)
        # Postorder: Process the root after the traversals of left and right
        # children
        print('Postorder: %d' % root.data)

# 9.1, Page 116 - Test if a tree is height-balanced
import collections

def is_balanced_binary_tree(tree = BinaryTreeNode):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicated if treeis balanced, and if
    # balanced the second value of the return value is the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced 