from collections import deque

class DynamicQueue:
    def __init__(self, lst: list):
        self.queue = deque(lst)

    def dequeue_all(self) -> list:
        dequeued = []
        while self.queue:
            item = self.queue.popleft()
            print(f"Dequeued: {item}")
            dequeued.append(item)
        return dequeued


class StaticQueue:
    def __init__(self, lst: list):
        self.queue = [None] * len(lst)
        self.front = 0
        self.back = 0

        for item in lst:
            if self.back < len(self.queue):
                self.queue[self.back] = item
                self.back += 1
            else:
                print("Full queue!")

    def dequeue_all(self) -> list:
        dequeued = []
        while self.front < self.back:
            item = self.queue[self.front]
            print(f"Dequeued: {item}")
            dequeued.append(item)
            self.front += 1
        return dequeued