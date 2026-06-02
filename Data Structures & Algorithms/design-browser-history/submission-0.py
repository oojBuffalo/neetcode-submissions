class HistoryNode:
    """Doubly-linked-list node for BrowserHistory"""
    def __init__(self, url: str, prev: HistoryNode = None, next: HistoryNode = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.page: HistoryNode = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        newPage = HistoryNode(url, self.page, None)
        self.page.next = newPage
        self.page = newPage

    def back(self, steps: int) -> str:
        while steps > 0:
            if not self.page.prev:
                return self.page.url
            self.page = self.page.prev
            steps -= 1
        return self.page.url

    def forward(self, steps: int) -> str:
        while steps > 0:
            if not self.page.next:
                return self.page.url
            self.page = self.page.next
            steps -= 1
        return self.page.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)