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
            return None

    def _find(self, data, cur_node):
        if data == cur_node.data:
            return cur_node

        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

    def find_minimum(self):
        if self.root:
            tree_min = self.root
            while tree_min.left:
                tree_min = tree_min.left
            return tree_min.data
        else:
            return None

    def delete(self, data):
        parent = None
        node = self.root

        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right

        # node not found
        if node is None or node.data != data:
            return None

        # node has no children
        elif node.left is None and node.right is None:
            if node.data < parent.data:
                parent.left = None
            elif node.data > parent.data:
                parent.right = None

        # node has left child
        elif node.left and node.right is None:
            if node.data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.right

        # node has right child
        elif node.right and node.left is None:
            if node.data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right

        # node has left and right child

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    tree = BinarySearchTree(22)
    tree.insert(12)
    tree.insert(35)
    tree.insert(21)
    tree.insert(4)
    tree.insert(45)

    print(tree.find(12).data)
    print(tree.find(1))
    print(tree.find(13))

    tree.delete(21)

    print(tree.find_minimum())
