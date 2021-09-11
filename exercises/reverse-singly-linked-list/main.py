class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def reverse(self):
        if self.head is None:
            print("none")
            return

        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev


    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next


if __name__ == "__main__":
    the_list = LinkedList()

    the_list.insert_at_end(5)
    the_list.insert_at_end(6)
    the_list.insert_at_end(7)

    the_list.print_list()

    print("-------reverse--------")
    the_list.reverse()
    the_list.print_list()