from collections import deque

type NestedDeque = int | deque['NestedDeque']

class MyStack:
    """
    A stack implemented using nested queues.
    """
    def __init__(self):
        self.q: deque[NestedDeque] = deque()

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        stack_pop = self.q.popleft()
        self.q = self.q.popleft()
        return stack_pop

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not len(self.q)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()