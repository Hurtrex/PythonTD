from src.TD5.DoublyLinkedList import DoublyLinkedList
from src.TD5.ArrayList import ArrayList

def test_DLL():
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
    # Show the first
    print(values.find_node(0))
    # Show None
    print(values.find_node(-4))
    # Show the last
    print(values.find_node(90))

    # Put item at the start
    values.put(150, 0)
    print(values)

    # Put None cuz negative
    values.put(155, -1)
    print(values)

    # Put the item at the end
    values.put(155, 50)
    print(values)
test_DLL()

def test_ArrayList():
    values = ArrayList(30)
    values.add_back(5)
    values.add_back(5)
    values.add_back(2)
    values.add_front(7)
    values.add_front(10)
    print(values)
    values.put_at(2,150)
    print(values)
test_ArrayList()