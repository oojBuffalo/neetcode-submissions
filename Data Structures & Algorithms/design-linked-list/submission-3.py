class MyNode:
    def __init__(self, val: int, prev: Optional[MyNode] = None, next: Optional[MyNode] = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head: Optional[MyNode] = None
        self.tail: Optional[MyNode] = None
        self.length: int = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        if 2 * index < self.length - 1:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - index - 1):
                node = node.prev
        return node.val

    def addAtHead(self, val: int) -> None:
        if not self.length:
            self.head = self.tail = MyNode(val, None, None)
        else:
            self.head.prev = MyNode(val, None, self.head)
            self.head = self.head.prev
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.length:
            self.head = self.tail = MyNode(val, None, None)
        else:
            self.tail.next = MyNode(val, self.tail, None)
            self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        
        if index == 0:
            return self.addAtHead(val)

        if index == self.length:
            return self.addAtTail(val)
            
        if 2 * index < self.length - 1:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - index - 1):
                node = node.prev
        
        new_node = MyNode(val, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        if self.length == 1:
            self.head = self.tail = None

        elif self.length == 2:
            if index == 0:
                self.head = self.tail
                self.tail.prev = None
            else:
                self.tail = self.head
                self.head.next = None

        else:
            if 2 * index < self.length - 1:
                node = self.head
                for _ in range(index):
                    node = node.next
            else:
                node = self.tail
                for _ in range(self.length - index - 1):
                    node = node.prev
            
            if index == 0:
                self.head = self.head.next
            else:
                node.prev.next = node.next
            
            if index == self.length - 1:
                self.tail = self.tail.prev
            else:
                node.next.prev = node.prev
    
        self.length -= 1 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)