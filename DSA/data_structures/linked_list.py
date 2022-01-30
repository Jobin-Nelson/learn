class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = node(data, self.head)

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = node(data, None)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node(data, None)

    def insert_values(self, data_list):
        self.head = None
        
        for l in data_list:
            self.insert_at_end(l)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, ind):
        if ind < 0 or ind >= self.get_length():
            raise  Exception('Invalid index')

        if ind == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == ind - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self, ind, data):
        if ind < 0 or ind >= self.get_length():
            raise  Exception('Invalid index')

        if ind == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == ind -1:
                itr.next = node(data, itr.next)
                return
            itr = itr.next
            count += 1

    def insert_after_value(self, val, data):
        itr = self.head
        while itr:
            if itr.data == val:
                itr.next = node(data, itr.next)
                return
            itr = itr.next

    def remove_by_value(self, val):
        itr = self.head
        while itr:
            if itr.next.data == val:
                itr.next = itr.next.next
                return
            itr = itr.next

class double_node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class double_linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = double_node(None, data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = double_node(itr, data, None)

    def prepend(self, data):
        if self.head is None:
            self.head = double_node(None, data, None)
            return
        node = double_node(None, data, self.head)
        self.head.prev = node
        self.head = node

    def print_forward(self):
        if self.head is None:
            print('Double linked list is empty')
            return

        itr = self.head
        dlstr = ''
        while itr:
            dlstr += str(itr.data) + '-->'
            itr = itr.next
        print(dlstr)

    def print_backward(self):
        if self.head is None:
            print('Double linked list is empty')
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        dlstr = ''
        while itr:
            dlstr += str(itr.data) + '-->'
            itr = itr.prev
        print(dlstr)


if __name__ == '__main__':
    ll = linked_list()
    ll.insert_values(['bannana', 'mango', 'grapes', 'orange'])
    ll.print()
    print('Length : ', ll.get_length())
    ll.remove_at(2)
    ll.insert_at(2, 'figs')
    ll.insert_at(2, 'jackfruit')
    ll.print()
    ll.insert_after_value('figs', 'apple')
    ll.print()
    ll.remove_by_value('mango')
    ll.print()

    dl = double_linked_list()
    dl.append('Jobin')
    dl.append('Jaison')
    dl.print_forward()
    dl.print_backward()
    dl.prepend('Jessy')
    dl.prepend('Nelson')
    dl.print_forward()
    dl.print_backward()

