from traceback import print_tb


class Node:
    def __init__(self, data) -> None:
        self.root = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.root is None:
            self.root = data
        elif self.root > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif self.root < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif self.root == data:
            return

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.root)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.root)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.root)


node = Node(9)
node.insert(3)
node.insert(11)
node.insert(5)
node.insert(4)
node.insert(15)
node.insert(6)
print("in order")
node.in_order()
print("pre order")
node.pre_order()
print("post order")
node.post_order()
