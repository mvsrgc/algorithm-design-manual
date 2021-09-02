class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.items):
            result = self.items[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    my_queue.dequeue()

    for item in my_queue:
        print(item)
