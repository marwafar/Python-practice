class ListNode:
  def __init__(self,val=0,next=None):
    self.val=val
    self.next=next


a=ListNode(2)
b=ListNode(3)
c=ListNode(4)
l1=ListNode(1)
l1.next=b
#b.next=c
#c.next=a

l2=ListNode(0)
#k=ListNode(9)
#j=ListNode(8)
#m=ListNode(7)
#l2.next=k
#k.next=j
#j.next=m

current_node=l2
while current_node:
  print(current_node.val)
  current_node=current_node.next

x=''
y=''
current_node=l1
while current_node:
  x+=str(current_node.val)
  current_node=current_node.next

current_node=l2
while current_node:
  y+=str(current_node.val)
  current_node=current_node.next

print(x,y)





