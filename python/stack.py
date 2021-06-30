class Stack:
    def __init__(self):
        self.stack_list = list()

    def push(self, item):
        self.stack_list.append(item)
        print(self.stack_list)

    def pop(self):
        if len(self.stack_list) == 0:
            print('스택에 아무 것도 존재하지 않습니다.')
            return
        self.stack_list.pop()
        print(self.stack_list)


new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.pop()
new_stack.pop()