from collections import deque

class MyStack:
    """
    A stack implemented using two queue, which is apparently only useful in 
    the fact that it is an unconventional and convoluted way of doing so.

    In order to get a LIFO behavior, we need to alter push and pop operations.
    
    For pop, to start, all stack items are initially held in queue 1.  When pop 
    is called, to get the most recently pushed or "last" stack item, we deque 
    all items except that "last" one and enque them to queue 2.  The "last" stack
    item is them dequed and returned.  We can then swap the references to queue 1
    and queue 2 to avoid dequeuing and enqueuing all remaining items in the stack.

    For push, in order to complement the behavior of pop and maintain the LIFO behavior,
    we only then need to enque any new item pushed onto the stack to queue 1.
    """
    def __init__(self):
        self.q1: deque[int] = deque()
        self.q2: deque[int] = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # Move all items, but last from q1 to q2
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        
        # Dequeue the stack pop from q1
        stack_pop = self.q1.popleft()

        # Swap references
        self.q1, self.q2 = self.q2, self.q1
        
        return stack_pop

    def top(self) -> int:
        # Move all items, but last from q1 to q2
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        
        # Dequeue the stack top from q1
        stack_top = self.q1.popleft()

        # Re-enqueue the stack top
        self.q2.append(stack_top)

        # Swap references
        self.q1, self.q2 = self.q2, self.q1

        return stack_top

    def empty(self) -> bool:
        return not len(self.q1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()