class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Node not in DLL.")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def insert_before(self, head, next_node, new_data):
        if next_node is None:
            print("The next node cannot be null.")
            return

        new_node = Node(new_data)

        new_node.prev = next_node.prev

        next_node.prev = new_node

        new_node.next = next_node

        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            head = new_node

        return head

    def print_list(self, node):
        print("\n Traversal in forward direction")
        while node:
            print(f" {node.data} ")
            last = node
            node = node.next

        print("\n Traversal in backward direction")
        while last:
            print(f" {last.data} ")
            last = last.prev


if __name__ == "__main__":
    llist = DoublyLinkedList()

    llist.insert_at_start(5)
    llist.insert_at_start(6)
    llist.insert_at_start(17)
    llist.insert_at_start(20)

    llist.print_list(llist.head)
