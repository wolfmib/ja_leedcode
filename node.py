"""
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

--------

Approach 1: Two pass algorithm
Intuition

We notice that the problem could be simply reduced to another one : Remove the (L - n + 1)(L−n+1) th node from the beginning in the list , 
where LL is the list length. This problem is easy to solve once we found list length LL.

Algorithm

First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some 
corner cases such as a list with only one node, or removing the head of the list. On the first pass, we find the list length LL. 
Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L - n)(L−n) th node. We relink 
next pointer of the (L - n)(L−n) th node to the (L - n + 2)(L−n+2) th node and we are done.

"""


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(head)

    dummy = ListNode(0)
    dummy.next = head

    length = 0
    n = 2

    first = head
    while first != None:
        length += 1
        first = first.next
    print("head's length (L)   =  ",length)

    length -= n
    print("For [1,2,3,4 ] n = 2,    The skip poision index  is  = ",length)

    first = dummy
    while length > 0 :
        length -=1
        print(length,"first = ", first.val, "first.next = ",first.next.val)
        first = first.next  #    [] <- 1 
        print(length, "first = ", first.val, "first.next = ", first.next.val)
    
    # 這邊進行跨接
    #   2  -> 4   
    first.next = first.next.next


