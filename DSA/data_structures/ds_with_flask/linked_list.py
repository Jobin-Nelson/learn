class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return

        self.head = Node(data, self.head)

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def print_ll(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        ll_string = ''
        while itr:
            ll_string += str(itr.data) + '-->'
            itr = itr.next_node
        ll_string += 'None'
        print(ll_string)

    def to_list(self):
        l = []
        if self.head is None:
            return l

        itr = self.head
        while itr:
            l.append(itr.data)
            itr = itr.next_node
        return l

    def get_user_by_id(self, user_id):
        itr = self.head
        while itr:
            if itr.data['id'] == int(user_id):
                return itr.data
            itr = itr.next_node
        return None

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beginning('data1')
    ll.insert_beginning('data2')
    ll.insert_beginning('data3')
    ll.insert_beginning('data4')
    ll.insert_end('data0')
    ll.print_ll()
