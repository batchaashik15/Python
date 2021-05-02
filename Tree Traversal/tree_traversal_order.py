class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def inorder(root):
    '''
    Function to simulate the preorder traversing
    '''
    if root:
        # First traverse the right child
        inorder(root.left)

        # then print the root value
        print(root.value)

        # Now traverse the right child
        inorder(root.right)


def preorder(root):
    '''
    Function to simulate the preorder traversing
    '''
    if root:
        # First print the root value
        print(root.value)

        # then traverse the left child
        preorder(root.left)

        # Now traverse the right child
        preorder(root.right)


def postorder(root):
    '''
    Function to simulate the preorder traversing
    '''
    if root:
        # First traverse the left child
        postorder(root.left)

        # then traverse the right child
        postorder(root.right)

        # Now print the root value
        print(root.value)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traversal of binary tree is ")
    inorder(root)
    print("Prerder traversal of binary tree is ")
    preorder(root)
    print("Postrder traversal of binary tree is ")
    postorder(root)
