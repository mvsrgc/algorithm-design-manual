class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        max_index = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max_index]:
                max_index = i

        return self.queue.pop(max_index)

if __name__ == "__main__":
    priority_queue = PriorityQueue()

    priority_queue.insert(12)
    priority_queue.insert(1)
    priority_queue.insert(14)
    priority_queue.insert(7)

    while not priority_queue.is_empty():
        print(priority_queue.delete())
