class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def traverse(root):
    if root:
        arr=[]
        node_to_visit=[root]
        arr=[[root.val]]
        while node_to_visit:
            current_node=node_to_visit.pop(0)
            if current_node.left and current_node.right:
                node_to_visit+=[current_node.left,current_node.right]
                arr.append([current_node.left.val,current_node.right.val])
            elif current_node.left and not current_node.right:
                node_to_visit+=[current_node.left]
                arr.append([current_node.left.val])
            elif current_node.right and not current_node.left:
                node_to_visit+=[current_node.right]
                arr.append([current_node.right.val])

        return arr[-1::-1]
    else:
        return 

def levels(root):
    if not root:
        return

    level_to_visit=[[root]]
    result=[[root.val]]

    while level_to_visit:
        current_level_nodes=level_to_visit.pop(0)
        temp=[]
        arr=[]
        for node in current_level_nodes:
            if node.left and node.right:
                temp+=[node.left,node.right]
                arr+=[node.left.val,node.right.val]
            elif node.left:
                temp.append(node.left)
                arr.append(node.left.val)
            elif node.right:
                temp.append(node.right)
                arr.append(node.right.val)

        if temp and arr:        
            level_to_visit.append(temp)
            result.append(arr)
        elif temp:
            level_to_visit.append(temp)
        elif arr:
            result.append(arr)

    return result[-1::-1]



root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
#root.left.left=TreeNode(4)
#root.left.right=TreeNode(5)
#root.left.right.left=TreeNode(8)
#root.right.left.left=TreeNode(10)

#print(traverse(root))
print(levels(root))