from src.TD5.DoublyLinkedList import DoublyLinkedList

values = DoublyLinkedList()
values.add_back(5)
values.add_back(2)
values.add_back(5)
values.add_back(6)
values.add_back(6)
values.add_front(9)
values.add_front(2)
print(values)

print(values.find_node(4))
print(values.find_node(0))
print(values.find_node(-4))
print(values.find_node(90))