from linked_list import * 

def reverse_linked_list(LL):
    prev = None
    curr = LL.head
    next = None

    while curr:
        print(curr.data)
        next = curr.next

        curr.next = prev

        prev = curr
        curr = next
    newLL = LinkedList()
    newLL.head = prev
    return newLL

l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
reverse_linked_list(l).printLL()