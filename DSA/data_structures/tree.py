class tree:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_tree():
    root = tree('Electronics')

    phone = tree('Mobile phone')
    phone.add_child(tree('Iphone'))
    phone.add_child(tree('Pixel'))
    phone.add_child(tree('Vivo'))

    tv = tree('TV')
    tv.add_child(tree('Samsung'))
    tv.add_child(tree('LG'))

    laptop = tree('Laptop')
    laptop.add_child(tree('Mac'))
    laptop.add_child(tree('Surface'))
    laptop.add_child(tree('Thinkpad'))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    root.print_tree()

    return root

if __name__ == '__main__':
    build_tree()
