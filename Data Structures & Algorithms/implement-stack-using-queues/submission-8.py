from collections import deque

class MyStack:
    """
    A stack implemented using a queue.
    
    Time Complexity:
      push:  O(n)
      pop:   O(1)
      top:   O(1)
      empty: O(1)
    """
    def __init__(self):
        self.q: deque[int] = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

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