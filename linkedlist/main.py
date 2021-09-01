class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def insert_after_item(self, x, data):
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next

        if n is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_before_item(self, x, data):
        if self.head is None:
            print("Can't insert before item, list is empty.")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next

        if n is None:
            print("Item not in list.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def search_item(self, x):
        if self.head is None:
            print("List is empty.")
            return

        n = self.head

        while n is not None:
            if n.data == x:
                print("Item found.")
                return True
            n = n.next

        print("Item not found.")
        return False

    def delete_item(self, x):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == x:
            self.head = self.head.next
            return

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break

            n = n.next

        if n.next is None:
            print("Item not found.")
        else:
            n.next = n.next.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_start(5)
    llist.insert_at_start(4)
    llist.insert_at_start(3)
    llist.insert_at_start(2)
    llist.insert_at_end(8)
    llist.insert_after_item(4, 9)
    llist.insert_before_item(8, 6)
    llist.insert_before_item(2, 17)

    llist.search_item(6)

    llist.delete_item(8)

    llist.print_list()
