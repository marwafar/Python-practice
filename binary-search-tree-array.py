class TreeNode:

    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def bst_recursive(sorted_array):

    if not sorted_array:
        return None
    
    mid_idx=len(sorted_array)//2
    mid_val=sorted_array[mid_idx]

    root=TreeNode(mid_val)
    root.left=bst_recursive(sorted_array[:mid_idx])
    root.right=bst_recursive(sorted_array[mid_idx+1:])

    return root
#--------------------------
def traverse(root):

    if not root:
        return None

    node_to_visit=[root]
    result=[[root.val]]

    while node_to_visit:
        current_node=node_to_visit.pop(0)

        if current_node.left and current_node.right:
            node_to_visit+=[current_node.left,current_node.right]
            result.append([current_node.left.val,current_node.right.val])
        elif current_node.left:
            node_to_visit+=[current_node.left]
            result.append([current_node.left.val])
        elif current_node.right:
            node_to_visit+=[current_node.right]
            result.append([current_node.right])
    
    if result:
        return result
#------------------
def traverse_level(root):

    node_to_visit=[[root]]
    result=[[root.val]]

    depth=0
    while node_to_visit:
        current_level=node_to_visit.pop(0)

        temp_node=[]
        temp_result=[]
        for node in current_level:
            if node.left and node.right:
                temp_node+=[node.left,node.right]
                temp_result+=[node.left.val,node.right.val]
            elif node.left:
               temp_node+=[node.left]
               temp_result+=[node.left.val]
            elif node.right:
                temp_node+=[node.right]
                temp_result+=[node.right.val]
        
        if temp_node and temp_result:
            node_to_visit.append(temp_node)
            result.append(temp_result)
        depth+=1

    return result,depth
#----------------------
def traverse_level_2(root):

    depth=0
    result=[[root.val]]
    queue=[root]

    while queue:

        level=len(queue)
        temp_result=[]
        for i in range(level):
            node=queue.pop(0)
            if node.left and node.right:
                temp_result+=[node.left.val,node.right.val]
                queue+=[node.left,node.right]
            elif node.left:
                temp_result+=[node.left.val]
                queue+=[node.left]
            elif node.right:
                temp_result+=[node.right.val]
                queue+=[node.right]
        depth+=1
        if temp_result:
            result.append(temp_result)

    return (result,depth)
#-------------------------------------
def in_order(root):

    result=[]
    stack=[root]
    node=root

    while stack:
        if node.left:
            stack.append(node.left)
            node=node.left

        if not node.left or not node:
            current_node=stack.pop()            
            result.append(current_node.val)  

            if current_node.right:         
                node=current_node.right
                stack.append(node)

    return result
#-------------------------------------
def pre_order(root):

    stack=[root]
    result=[]
    while stack:
        node=stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
#------------------------------------
def post_order(root):

    stack=[root]
    result=[]

    while stack:
        node=stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[-1::-1]

#-------------------------------------
def deep_traverse(root,result=[]):

    if not root:
        return None
    
    #result.append(root.val)
    deep_traverse(root.left,result)
    #result.append(root.val)
    deep_traverse(root.right,result)
    result.append(root.val)
    
    return result
#-------------------------------------
def depth_2(root):
    if not root:
        return 0
    
    #result=[]
    left=1+symmetry(root.left)
    #result.append(left)
    right=1+symmetry(root.right)
    #result.append(right)
    #print(left,right)

     
    if left and right:
        return max(left,right)
    elif left:
        return left
    elif right:
        return right
    else:
        return 1
    #return left==right
#--------------------------------------
def max_depth(root):
    if not root:
        return 0
    
    ldepth=max_depth(root.left)
    rdepth=max_depth(root.right)

    #if ldepth>rdepth:
    #    return ldepth+1
    #else:
    #    return rdepth+1
    #return max(ldepth,rdepth)+1
    if ldepth>rdepth:
        return ldepth+1
    else:
        return rdepth+1
    #return max(ldepth,rdepth)+1
#-------------------------------------
def symmetry_iter(root):

    if not root:
        return True
    if not root.left and not root.right:
        return True

    if root.left and root.right:        
        subtree_left=[root.left]
        subtree_right=[root.right]        
    else:
        return False

    while subtree_left and subtree_right:

        nodes_left=subtree_left.pop(0)
        nodes_right=subtree_right.pop(0)

        if nodes_left.val!=nodes_right.val:
            return False

        if nodes_left.left and nodes_right.right:            
            subtree_left.append(nodes_left.left)
            subtree_right.append(nodes_right.right)
                    
        elif nodes_left.left or nodes_right.right:
            return False
        
        
        if nodes_left.right and nodes_right.left:
            subtree_left.append(nodes_left.right)
            subtree_right.append(nodes_right.left)
            
        elif nodes_left.right or nodes_right.left:
            return False

    return True
#-------------------------------------
def symmetry_recursive(root1,root2):

    if not root1 and not root2:
        return True
    print(root1.val,root2.val)
    if root1 and root2:
        if root1.val==root2.val:
            return symmetry_recursive(root1.left,root2.right) and \
                symmetry_recursive(root1.right,root2.left)
    
    return False
#-------------------------------------
def haspathsum(root,target):
    if not root:
        return False
    
    s=root.val
    if not root.left and not root.right:
        if s==target:
            return True
    stack=[root,s]
    node=root
    while stack:
        if node.left:
            s+=node.left.val
            stack.append(node.left)
            stack.append(s)
            node=node.left
            if not node.left and not node.right:
                if s==target:
                    return True
        else:
            s=stack.pop()
            current_node=stack.pop()
            if current_node.right:
                s+=current_node.right.val
                stack.append(current_node.right)
                stack.append(s)
                node=current_node.right
                if not node.left and not node.right:
                    if s==sum:
                        return True
    return False

#--------------------------------------
def diamater(root):
    if not root:
        return 0
    
    ans=[0]
    h=tree_h(root,ans)
    return ans[0]
#----------------------------
def tree_h(root,ans):
    if not root:
        return 0

    l=tree_h(root.left,ans)
    r=tree_h(root.right,ans)
    ans[0]=max(ans[0],1+l+r)
    
    return max(l,r)+1
#--------------------------------------
def kdistance(root,k,depth=0,result=[]):
    
    if not root:
        return

    if depth==k:
        result.append(root.val)
        #print(result)

    ldepth=kdistance(root.left,k,depth+1,result)
    rdepth=kdistance(root.right,k,depth+1,result)

    return result
#-------------------------------------
def kdistance_iter(root,k):

    if not root:
        return

    queue=[root]
    depth=0
    if depth==k:
        print(root.val)
        return
    while queue:
        l=len(queue)
        for i in range(l):
            node=queue.pop(0)
            if node.left:
                if depth+1==k:
                    print(node.left.val, end=' ')
                queue.append(node.left)
            if node.right:
                if depth+1==k:
                    print(node.right.val, end=' ')
                queue.append(node.right)
        depth+=1
        if depth==k:
            print("\n")
            return
    return
        

#--------------------------------------
def ancestor(root,target):
    if not root:
        return False
    
    if root.val==target:
        return True
    
    if (ancestor(root.left,target) or ancestor(root.right,target)):
        print(root.val)
        return True
    return False
#---------------------------------------

#--------------------------------------
sorted_array=[0,1,2,3,4,5,6,7,8]
tree=bst_recursive(sorted_array)
print("Traverse tree by level")
#print(traverse(tree))
print(traverse_level(tree))
#print(traverse_level_2(tree))

#print("Traverse deep")
#print(deep_traverse(tree))
#print(in_order(tree))
#print(pre_order(tree))
#print(post_order(tree))
#print("Get the depth")
#print(max_depth(tree))
#print(symmetry_iter(tree))
#print(symmetry_recursive(tree,tree))
#print(haspathsum(tree,22))
#print(diamater(tree))
#print(kdistance(tree,9))
#kdistance_iter(tree,9)
print(ancestor(tree,5))
#----------------------------
tree_2=TreeNode(1)
tree_2.left=TreeNode(2)
tree_2.right=TreeNode(2)
tree_2.left.left=TreeNode(3)
tree_2.right.right=TreeNode(3)
tree_2.left.left.left=TreeNode(4)
tree_2.left.left.right=TreeNode(5)
tree_2.right.right.left=TreeNode(5)
tree_2.right.right.right=TreeNode(4)
#print(symmetry_iter(tree_2))

#print(symmetry_recursive(tree_2,tree_2))
#------------------------------------------
#inorder=[0, 1, 2, 3, 4, 5, 6, 7, 8]
#postorder=[0, 1, 3, 2, 5, 6, 8, 7, 4]
inorder=[3,2,1]
postorder=[3,2,1]
#buildtree(inorder,postorder)