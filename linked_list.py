class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_node(self):
        if self.next is None:
            print(f"NODE - hodnota je {self.value} a ukazatel je 'None'")
        else:
            print(f"NODE - hodnota je {self.value} a ukazatel ukaze ja nodes cislem {self.next.value}")


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def list_add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def list_add_to_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_on_index(self, index, value):
        new_node = Node(value)
        current_node = self.head

        for _ in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def remove_on_index(self, index):
        current_node = self.head

        for _ in range(index - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next

    def find_value(self, value):
        index_counter = 0
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return index_counter - 1

            index_counter += 1
            current_node = current_node.next

        return None


    def print_values(self):
        if self.head is None:
            print("List je prazdny - Hodnota head i tail je 'None'")

        else:
            print(f"HEAD ukazuje na Node s hodnotou {self.head.value} - {self.head}")
            print(f"TAIL ukazuje na Node s hodnotou {self.tail.value} - {self.tail}")


linked_list0 = LinkedList()
linked_list0.print_values()
print()

linked_list0.list_add_to_end(1)
linked_list0.print_values()
print()

linked_list0.list_add_to_end(2)
linked_list0.print_values()
linked_list0.head.next.print_node()
print()

linked_list0.list_add_to_end(2)
linked_list0.print_values()
linked_list0.head.next.print_node()
print()


linked_list0.list_add_to_end(3)
linked_list0.print_values()
linked_list0.head.next.print_node()
print()

linked_list0.list_add_to_front(5)
linked_list0.print_values()
linked_list0.head.next.print_node()
linked_list0.head.next.next.print_node()

current_node0 = linked_list0.head

print(linked_list0.find_value(3))