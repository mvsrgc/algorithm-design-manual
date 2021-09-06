class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value is already present in tree.")

    def find(self, data):
        if self.root:
            return self._find(data, self.root)
        else:
            return False

    def _find(self, data, cur_node):
        if data == cur_node.data:
            return True

        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    tree = BinarySearchTree(22)
    tree.insert(12)
    tree.insert(1)
    tree.insert(45)

    print(tree.find(12))
    print(tree.find(1))
    print(tree.find(13))
