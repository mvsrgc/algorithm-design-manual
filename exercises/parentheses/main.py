class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)


def check_parentheses(input: str) -> bool:
    stack = Stack()

    valid_paren = 0
    for letter in input:
        if letter == "(":
            stack.push("(")
        else:
            valid_paren += 1
            stack.pop()

    return stack.is_empty()


if __name__ == "__main__":
    assert not check_parentheses("((())())()(")
    assert check_parentheses("((())())()")
    assert not check_parentheses("(((())())()")
