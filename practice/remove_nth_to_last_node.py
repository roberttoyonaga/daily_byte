# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

#----------------------------------------------------------------------------
def remove_nth_to_last_node(LL,nth):
  node = LL.head
  length = 0
  while node:
    node=node.next
    length += 1

  if length < nth or nth is 0:
    return LL

  node = LL.head

  count = 1 
  while count < (length - nth):
    node = node.next
    count += 1
  
  node.next = node.next.next
  return LL


l = LinkedList()
l.insert(3)
l.insert(4)
l.insert(7)
l.insert(8)

remove_nth_to_last_node(l,3).printLL()



