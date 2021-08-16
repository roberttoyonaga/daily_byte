from linked_list import * 

def tortoise_hare(LL):
    #floyd's cycle detection algo
    slow = LL.head
    fast = LL.head
    cycle = False

    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle = True
            break



    if cycle:
        print("cycle detected")
        slow = LL.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data

    else:
        return None

l = LinkedList()

n0 = Node(0)
l.head = n0

n1 = Node(1)
n0.next = n1

n2 = Node(2)
n1.next = n2

n3 = Node(3)
n2.next = n3

n4 = Node(4)
n3.next = n4

n4.next = n2

print(tortoise_hare(l))