# class __init__(object):
#     def __init__(self, data = None, next = None):
#         self.head = data
#         self.next = next


# class linkedList(object):
#     def __init__(self, head):
#         self.head = None
#         self.tail = none

#a -> b -> c -> D -> None 

#d -> c -> b -> a -> None 
def reverseLinkedList(head):

    curr = head
    pervious = None
    while True:
            #iterate forward
            #b | c
            nxt = curr.next

            #set pointer to orignal Node 
            #a --> None | b -> a
            curr.next = pervious
            
            #Set up for next iteration by changing prev 
            # to orignal Node , which was the Head !
            #a| b
            pervious = curr
            
            if not nxt.next:
                break
            #b | c 
            curr = nxt

            
    return curr
ll = LinkedList()
ll.append("a ")
ll.append("b")
ll.append("c ")
ll.append("d ")
ll.append("a ")

