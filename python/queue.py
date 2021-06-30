class Queue:
    def __init__(self):
        self.queue_list = list()

    def push(self, item):
        self.queue_list.append(item)
        print(self.queue_list)

    def pop(self):
        if len(self.queue_list) == 0:
            print('큐가 비어있습니다.')
            return
        self.queue_list.pop(0)
        print(self.queue_list)


new_queue = Queue()
new_queue.push(10)
new_queue.push(20)
new_queue.push(30)
new_queue.pop()
new_queue.pop()