class Queue:
    def __init__(self):
        self.__items = []

    def insert_item(self, item):
        self.__items.insert(0, item)
        # self.__items.append(item)

    def delete(self):
        return self.__items.pop()
        # return self.__items.pop(0)
        # zakomentovane kody jsou pro opacny chod fronty

    def peek(self):
        return self.__items[-1]
        # return self.__items[0]

    def is_empty(self) -> bool:
        return not self.__items

    def size(self) -> int:
        return len(self.__items)

    def __str__(self):
        return str(self.__items)


my_queue = Queue()

my_queue.insert_item(3)
my_queue.insert_item(4)
my_queue.insert_item(5)
print(my_queue)
print(my_queue.peek())
print(my_queue.size())
my_queue.insert_item(6)
print(my_queue.peek())
print(my_queue.size())
print(my_queue.delete())

print(my_queue)