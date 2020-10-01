class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#-------------------------
def traverse(l):

    current_node=l
    result=[]
    while current_node:
        result.append(current_node.val)
        current_node=current_node.next
    return result
#----------------------------------
def swap(l):
    
    prev_node=None
    current_node=l

    new_head=current_node.next
    while current_node and current_node.next:

        next_node=current_node.next

        if prev_node:
            prev_node.next=next_node
        
        current_node.next=next_node.next
        next_node.next=current_node

        prev_node=current_node
        current_node=prev_node.next

    
    print(traverse(new_head))
    
    return
#---------------------------
def swap_rec(l):

    if l is None or l.next is None:
        return l

    new_head=l.next
    #print(new_head.val)
    l.next=swap_rec(new_head.next)
    #if l.next:
    #    print(l.next.val)
    new_head.next=l
    #print(new_head.next.val)

    #print(traverse(new_head))

    return new_head

    
#--------------------------
l=Node(1)
a=Node(2)
b=Node(3)
c=Node(4)

l.next=a
a.next=b
b.next=c

print(traverse(l))
#swap(l)
head=swap_rec(l)
print(traverse(head))


