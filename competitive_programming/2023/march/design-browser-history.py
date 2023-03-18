'''
Created Date: 2023-03-18
Qn: You have a browser of one tab where you start on the homepage and you can
    visit another url, get back in the history number of steps or move forward
    in the history number of steps.

    Implement the BrowserHistory class:

        - BrowserHistory(string homepage) Initializes the object with the
          homepage of the browser. 
        - void visit(string url) Visits url from the current page. It clears up
          all the forward history. 
        - string back(int steps) Move steps back in history. If you can only
          return x steps in the history and steps > x, you will return only x
          steps. Return the current url after moving back in history at most
          steps. 
        - string forward(int steps) Move steps forward in history. If you can
          only forward x steps in the history and steps > x, you will forward
          only x steps. Return the current url after forwarding in history at
          most steps.
Link: https://leetcode.com/problems/design-browser-history/
Notes:
    - use doubly linked list
'''
from __future__ import annotations

class LinkedList:
    def __init__(self, val: str, next: LinkedList = None, prev: LinkedList = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = LinkedList(homepage)
    def visit(self, url: str) -> None:
        new_link = LinkedList(url)
        new_link.prev = self.history
        self.history.next = new_link
        self.history = self.history.next
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.prev: return self.history.val
            self.history = self.history.prev
        return self.history.val
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.next: return self.history.val
            self.history = self.history.next
        return self.history.val

if __name__ == '__main__':
    b = BrowserHistory('leetcode.com')
    b.visit("google.com");             # You are in "leetcode.com". Visit "google.com"
    b.visit("facebook.com");           # You are in "google.com". Visit "facebook.com"
    b.visit("youtube.com");            # You are in "facebook.com". Visit "youtube.com"
    print(b.back(1))                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(b.back(1))                   # You are in "facebook.com", move back to "google.com" return "google.com"
    print(b.forward(1))                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    b.visit("linkedin.com")            # You are in "facebook.com". Visit "linkedin.com"
    print(b.forward(2))                # You are in "linkedin.com", you cannot move forward any steps.
    print(b.back(2))                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    print(b.back(7))                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
