from collections import deque

class MyStack:
    """
    A stack implemented using two queues.

    Logic for enforcing stack-order invariant moved from pop/top to push.
    """
    def __init__(self):
        self.q1: deque[int] = deque()
        self.q2: deque[int] = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        for _ in range(len(self.q1)):
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not len(self.q1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()