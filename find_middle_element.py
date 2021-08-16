from linked_list import * 

def find_middle_node(LL):
    count = 0 
    node = LL.head

    while node:
        count +=1
        node=node.next
    
    middle_node = 0

    if count%2 == 0:
        middle_node = (count+2)/2
    else:
        middle_node = (count+1)/2
    
    count = 0 
    node = LL.head

    while node:
        count += 1
        if count == middle_node:
            return node
        node=node.next

l = LinkedList()
l.insert(3)
l.insert(4)
l.insert(7)
l.insert(8)

print(find_middle_node(l).data)