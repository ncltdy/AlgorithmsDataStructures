
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(f"hodnota: {self.value}, levy: {self.left.value}, pravy: {self.right.value}")


class Tree:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        new_node = TreeNode(value)
        current_node = self.root
        if self.root is None:
            self.root = new_node
        while True:
            if value < current_node.value:
                if new_node.left is None:
                    current_node.left = new_node
                    return 1
                else:
                    current_node = new_node.left

            elif value > current_node.value:
                if new_node.right is None:
                    current_node.right = new_node
                    return 1
                else:
                    current_node = new_node.right
            else:
                return 0

    def find(self, value):
        current_node = self.root
        while True:
            if value == current_node.value:
                return self.root
            if value < current_node.value:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            if value > current_node.value:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right