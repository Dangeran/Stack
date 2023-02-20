class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not bool(len(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]


def check_sequence(sequence_str):
    open_staples = ['(', '[', '{']
    close_staples = [')', ']', '}']

    if len(sequence_str) % 2 == 1:
        return False
    else:
        sequence_list = list(sequence_str)
        stack = Stack()
        for i in sequence_list:
            if i in open_staples:  # Открывающие скобки - заполняем стек
                stack.push(i)
            elif i in close_staples:  # Закрывающие скобки - освобождаем стек
                if stack.is_empty():
                    return False
                if i == close_staples[0] and stack.peek() == open_staples[0]:
                    stack.pop()
                elif i == close_staples[1] and stack.peek() == open_staples[1]:
                    stack.pop()
                elif i == close_staples[2] and stack.peek() == open_staples[2]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return stack.is_empty()


if __name__ == "__main__":
    sequence = input('Введите последовательность для оценки: ')
    if check_sequence(sequence):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
