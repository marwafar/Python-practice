class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None

#------------------------
def iscycle_exist(head):
    if not head:
        return False
    
    fast=head
    slow=head

    while fast and slow and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            return (True, slow.val)
    
    return False
#------------------------
def detect_cycle(head):

    if not head:
        return 
    
    seen={}
    current=head
    i=0
    while current:
        #if current in seen.values():
        if current in seen:
            return current.val
        
        #seen[i]=current
        seen[current]=True
        current=current.next
        i+=1
    return 
#------------------------
def detect_cycle_II(root):
    if not root:
        return
    
    slow=head
    fast=head

    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            slow=head
            while slow!=fast:
                slow=slow.next 
                fast=fast.next
            return slow.val
    return 
#--------------------------
def traverse(head):
    if not head:
        return
    current_node=head
    result=[]
    while current_node:
        result.append(current_node.val)
        current_node=current_node.next
    return result
#------------------------
def insert_after_node(head,prev_node,new_val):
    if not prev_node:
        return
    new_node=LinkedList(new_val)
    new_node.next=prev_node.next
    prev_node.next=new_node

    result=traverse(head)
    return(result)
#------------------------
def swap_node(head,x,y):
    if not head:
        return
    if x==y:
        return
    
    prev_x=None
    cur_x=head
    while cur_x and cur_x.val!=x:
        prev_x=cur_x
        cur_x=cur_x.next

    prev_y=None
    cur_y=head
    while cur_y and cur_y.val!=y:
        prev_y=cur_y
        cur_y=cur_y.next
    
    if not cur_y or not cur_x:
        return
    print(cur_x.val,cur_y.val)
    print(prev_x.val,prev_y.val)
    print(cur_x.next.val,cur_y.next.val)

    if not prev_x:
        head=cur_y
    else:
        prev_x.next=cur_y
    if not prev_y:
        head=cur_x
    else:
        prev_y.next=cur_x

    print(cur_x.next.val,cur_y.next.val)
    cur_x.next,cur_y.next=cur_y.next,cur_x.next

    result=traverse(head)
    return result
#----------------------------

#------------------------
head=LinkedList(-1)
a=LinkedList(-7)
b=LinkedList(7)
c=LinkedList(-4)
d=LinkedList(19)
e=LinkedList(6)
f=LinkedList(-9)
g=LinkedList(-5)
h=LinkedList(-2)
k=LinkedList(-5)

head.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=h
#h.next=k
#k.next=f

#print(iscycle_exist(head))
#print(detect_cycle(head))
#print(detect_cycle_II(head))
print(traverse(head))
#print(insert_after_node(head,d,30))
#print(swap_node(head,19,30))
#new_head=(reverese(head))
#print(traverse(new_head))