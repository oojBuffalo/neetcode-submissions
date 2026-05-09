class MinStack:
    """
    A stack that keeps track of its current minimum value.
    """

    def __init__(self):
        """
        Encodes values on stack as the differences between the values
        and the minimum value at the time the value is pushed.
        """ 
        self._stack: list[int] = list()
        self._min: int | float = float('inf')

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append(0)
            self._min = val
        else:
            enc = val - self._min
            self._stack.append(enc)
            if enc < 0:
                self._min = val

    def pop(self) -> None:
        p = self._stack.pop()
        if (p < 0):
            self._min = self._min - p

    def top(self) -> int:
        t = self._stack[-1]
        if t < 0:
            return self._min
        return t + self._min

    def getMin(self) -> int:
        return self._min