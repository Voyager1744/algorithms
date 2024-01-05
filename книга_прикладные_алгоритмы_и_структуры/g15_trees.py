class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

    def __str__(self):
        return f"узел с значением {self.value}"


node1 = TreeNode(25)
node2 = TreeNode(72)
root = TreeNode(50, node1, node2)


def search(search_value, node):
    if node is None or node.value == search_value:
        return node
    elif search_value < node.value:
        return search(search_value, node.leftChild)
    else:
        return search(search_value, node.rightChild)


def insert(value, node):
    if node is None:
        return TreeNode(value)
    if value < node.value:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)
    return node


def delete(value_to_delete, node):
    if node is None:
        return None
    elif value_to_delete < node.value:
        node.leftChild = delete(value_to_delete, node.leftChild)
    elif value_to_delete > node.value:
        node.rightChild = delete(value_to_delete, node.rightChild)
    elif value_to_delete == node.value:
        if node.leftChild is None:
            return node.rightChild
        elif node.rightChild is None:
            return node.leftChild
        else:
            node.value = lift(node.rightChild, node)
            return node


def lift(node, node_to_delete):
    if node.leftChild:
        node.leftChild = lift(node.leftChild, node)
        return node
    else:
        node_to_delete.value = node.value
        return node.rightChild


def max_in_tree(node):
    """
    Recursively finds the maximum value in a binary tree.

    Args:
        node: The root node of the binary tree.

    Returns:
        The maximum value in the binary tree.
    """
    if node.rightChild:
        # If there is a right child, recursively call the function on the right child.
        return max_in_tree(node.rightChild)
    else:
        # If there is no right child, return the value of the current node.
        return node.value

