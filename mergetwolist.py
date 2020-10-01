class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
#-----------------------------
def traverse(l):
    current_node=l
    arr=[]
    while current_node:
        arr.append(current_node.val)
        current_node=current_node.next
    return arr
#-------------------------------
def merge_sort(l1,l2):

    head_node=None
    if l1 and not l2:
        return l1
    elif l2 and not l1:
        return l2
    
    while l1 and l2:
        if l1.val<=l2.val:
            if head_node is None:
                head_node=ListNode(l1.val)
                current_node=head_node
                l1=l1.next
            else:
                current_node.next=ListNode(l1.val)
                current_node=current_node.next
                l1=l1.next
        else:
            if head_node is None:
                head_node=ListNode(l2.val)
                current_node=head_node
                l2=l2.next
            else:
                current_node.next=ListNode(l2.val)
                current_node=current_node.next
                l2=l2.next 
    if l1:
        current_node.next=l1
    if l2:
        current_node.next=l2
    
    print(traverse(head_node))

#-----------------------------
l1=ListNode(1)
a=ListNode(2)
b=ListNode(3)
c=ListNode(4)
l1.next=a
a.next=b
b.next=c
l2=ListNode(1)
l2.next=a
a.next=b
b.next=c
#------------------
#print(traverse(l2))

merge_sort(l1,l2)