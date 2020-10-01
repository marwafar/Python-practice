class Node:
    def __init__(self, val=0):
        self.val=val
        self.next=None
#-------------------------
def traverse(head):
    current_node=head
    result=[]
    while current_node:
        result.append(current_node.val)
        current_node=current_node.next
    return result
#----------------------------
def reverse(head):

    back=head
    new_end=back

    cur=back.next
    next=cur.next 

    while back and cur and next:

        prev=next
        cur.next=back

        try:
            print('prev', prev.val)
        except:
            print('prev is none')
        print('cur ', cur.val)
        print('cur next ', cur.next.val)
        
        back=next.next
        prev.next=cur

        try:
            print('prev.next', prev.next.val)
        except:
            print('prev next is none')

        cur=back.next
        next=cur.next

        new_head=prev    

        if back and not cur and not next:
            back.next=prev
            new_head=back

        if back and cur and not next:
            cur.next=back
            back.next=prev
            new_head=cur

            print('cur', cur.val)
            print('cur.next', cur.next.val)
            print('back', back.val)
            print('back.next', back.next.val)

    new_end.next=None
    print(traverse(new_head))
#----------------------------
def reverse_3(head):

    previous, current, next = None, head, None

    while current is not None:
		next = current.next
		current.next = previous
		previous = current
		current = next
	
    print(traverse(previous)) 
#----------------------------
def reverse_2(head):

    back=None
    cur=head
        
    while cur is not None:
        next_n=cur.next

        cur.next=back
        back=cur
        cur=next_n
    
    print(traverse(back))

#----------------------------
## create a list
#-------------------
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f

print(traverse(a))

reverse_2(a)
