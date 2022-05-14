class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def print_linked_list_rec(head):
    if head == None:
        return 
    print(head.val, end='->')
    print_linked_list_rec(head.next)

if __name__ == '__main__':
    print('Printing linked list')
    print_linked_list(a)
    print('Printing linked list recursively')
    print_linked_list_rec(a)
