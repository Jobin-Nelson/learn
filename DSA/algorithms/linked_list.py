class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        llstr = ""
        itr = self.head

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr) 

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data):
        self.head = None
        for d in data:
            self.insert_at_end(d)

    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count==(index-1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_beginning(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return 

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__=="__main__":
    ll = Linked_list()
    ll.insert_values(['Banana','Apples','Mango','Grapes'])
    ll.print()
    ll.insert_after_value('Mango', "Figs")
    ll.print()
    ll.remove_by_value("Figs")
    ll.remove_by_value("Banana")
    ll.remove_by_value("Mango")
    ll.remove_by_value("Apples")
    ll.remove_by_value("Grapes")
    ll.print()