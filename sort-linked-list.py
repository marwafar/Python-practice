class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None
#------------------------------
def traverse(head):
    if not head:
        return
    current_node=head
    result=[]
    while current_node:
        result.append(current_node.val)
        current_node=current_node.next
    return result

#-----------------------------------
def sortlist(head):
    if not head or not head.next:
        return head
    
    middle=get_middle(head)
    middle_next=middle.next
    middle.next=None

    left_list=sortlist(head)
    right_list=sortlist(middle_next)

    sorted_list=merge(left_list,right_list)

    return sorted_list
#--------------------------------------------
def merge(left,right):
    if not left and not right:
        return
    elif not left:
        return right
    elif not right:
        return left
    if left.val<=right.val:
        left.next=merge(left.next,right)
        return left
    else:
        right.next=merge(left,right.next)
    return right

#----------------------------------
def get_middle(head):
    if not head:
        return 
    
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    #print(slow.val)
    return slow
#-----------------------------------
head=LinkedList(1)
a=LinkedList(7)
b=LinkedList(10)
c=LinkedList(4)
d=LinkedList(9)
e=LinkedList(6)
f=LinkedList(8)
g=LinkedList(2)
h=LinkedList(3)
k=LinkedList(5)

head.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
#g.next=h

print(traverse(head))
#print(get_middle(head))
new_head=sortlist(head)
print(traverse(new_head))