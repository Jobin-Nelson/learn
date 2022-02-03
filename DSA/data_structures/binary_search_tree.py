class binary_search_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if child == self.data:
            return

        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = binary_search_tree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = binary_search_tree(child)

    def in_order_traversal(self):
        ls = []

        if self.left:
            ls += self.left.in_order_traversal()

        ls.append(self.data)

        if self.right:
            ls += self.right.in_order_traversal()

        return ls
    
    def pre_order_traversal(self):
        ls = [self.data]
        
        if self.left:
            ls += self.left.pre_order_traversal()
        if self.right:
            ls += self.right.pre_order_traversal()

        return ls

    def post_order_traversal(self):
        ls = []

        if self.left:
            ls += self.left.post_order_traversal()

        if self.right:
            ls += self.right.post_order_traversal()

        ls.append(self.data)

        return ls

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_sum(self):
        left_sum = self.left.find_sum() if self.left else 0
        right_sum = self.right.find_sum() if self.right else 0
        return left_sum + right_sum + self.data

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(arr):
    print('Building a tree with elements: ', arr)
    root = binary_search_tree(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])
    return root

if __name__ == '__main__':
    numbers = [15, 12, 27, 7, 14, 20, 88, 23]
    tree = build_tree(numbers)
    print('Is 23 in the tree: ', tree.search(23))
    print('Minimum value: ', tree.find_min())
    print('Maximum value: ', tree.find_max())
    print('Total sum: ', tree.find_sum())
    print('In order traversal: ', tree.in_order_traversal())
    print('Pre order traversal: ',tree.pre_order_traversal())
    print('Post order traversal: ',tree.post_order_traversal())
    tree.delete(20)
    print('Deleted 20, in order traversal: ', tree.in_order_traversal())
