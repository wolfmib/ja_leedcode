
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


# ListNode -> ListNode.next -> ListNode.next.next etc... つ付ける

if __name__ == "__main__":

    print("NODEを作成:   4->2->9 !")
    begin_node = my_node = ListNode(4)
    print("4 object at ", my_node)
    my_node.next = ListNode(2)
    my_node = my_node.next
    print("2 object at ", my_node)
    my_node.next = ListNode(9)
    my_node = my_node.next
    print("9 object at ", my_node)

    print("\n\n\n---------------------------------------------------------------------------")

    while begin_node != None:
        msg =  "ドード　            = [%d]       %s"%(begin_node.val,begin_node )
        begin_node = begin_node.next
        msg += "begin_node         = %s\n"%begin_node
        print(msg)
    
    print("Finish..")
    
   
