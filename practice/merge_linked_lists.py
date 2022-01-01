# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self, head = None):  
    self.head = head
  
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
def merge_linked_lists(l1, l2):
    #lists must be sorted in ascending order

    smaller = None
    larger = None

    #figure out which is smaller
    if l1.head.data < l2.head.data:
        smaller = l1
        larger = l2
    else:
        smaller = l2
        larger = l1

    curr = smaller.head

    #assume always adding to n1
    while curr and larger.head and curr.next:
        #print (curr.data,larger.head.data)
        if curr.data <= larger.head.data and curr.next.data >= larger.head.data:
            temp = curr.next
            temp2 = larger.head.next

            curr.next = larger.head
            larger.head.next = temp

            curr = curr.next
            larger.head = temp2
        else:
            #if we can run the while loop again
            if curr.next.next:
                curr = curr.next
            #if we cannot then point the last node in the smaller head LL 
            # that we've run out of nodes in to the remaining nodes in the larger head list
            else:
                curr.next.next = larger.head
                return smaller
           
    return smaller          

'''This is a simpler approach
We maintain three pointers to three lists
l1.head
l2.head
curr

we walk through l1 and l2 while building curr
'''
def merge_linked_lists_2(l1, l2):  
  
  curr = None #tail of list to return

  #figure out which list starts out smaller
  if l1.head.data < l2.head.data:
      curr = l1.head
      l1.head = l1.head.next
  else:
      curr = l2.head
      l2.head = l2.head.next

  ret = LinkedList(curr)

  while l1.head and l2.head:
    if l1.head.data < l2.head.data:
      temp = l1.head.next
      curr.next = l1.head
      l1.head = temp
    else:
      temp = l2.head.next
      curr.next = l2.head
      l2.head = temp
    curr= curr.next  

  if l1.head:
    curr.next = l1.head
  elif l2.head:
    curr.next = l2.head

  return ret

l = LinkedList()
l.insert(4)
l.insert(4)
l.insert(7)
l.insert(8)
l.insert(100)
l.insert(101)

l2 = LinkedList()
l2.insert(1)
l2.insert(1)
l2.insert(5)
l2.insert(6)
l2.insert(42)
l2.insert(42)
l2.insert(52)

merge_linked_lists_2(l,l2).printLL()


