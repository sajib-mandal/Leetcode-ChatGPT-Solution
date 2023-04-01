class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # create a dummy node to hold the merged list
    dummy = ListNode(0)
    # create a pointer to the dummy node
    curr = dummy
    # traverse both lists until one of them is exhausted
    while list1 and list2:
        if list1.val <= list2.val:
            # if the value in list1 is smaller, add it to the merged list
            curr.next = list1
            # move the pointer in list1 forward
            list1 = list1.next
        else:
            # if the value in list2 is smaller, add it to the merged list
            curr.next = list2
            # move the pointer in list2 forward
            list2 = list2.next
        # move the pointer in the merged list forward
        curr = curr.next
    '''
    if list1:
          curr.next = list1
      if list2:
          curr.next = list2
    '''
    # add any remaining nodes from list1 or list2 to the merged list
    curr.next = list1 or list2  # 🤯
    # return the head of the merged list (i.e., the second node of the dummy node)
    return dummy.next
