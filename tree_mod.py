from select import select


class Node:
    def __init__(self, data):
        self.node = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.node is None:
            self.node = data
        elif self.node > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add_node(data)
        elif self.node < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add_node(data)
        elif self.node == data:
            return

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.node)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.node)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.node)


n = int(input("enter data: "))
node = Node(n)
print("enter 1 for inserting node\nenter 2 for in order traversal\nenter 3 for pre order traversal\nenter 4 for post order traversal")
selection = 0
while True:
    selection = int(input("enter your selection: "))
    if selection == 1:
        data = int(input("enter data: "))
        node.add_node(data)
    if selection == 2:
        node.in_order()
    if selection == 3:
        node.pre_order()
    if selection == 4:
        node.post_order()
    if selection == 5:
        break
