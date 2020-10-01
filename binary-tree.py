class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def traverse(root):
    if not root:
        return

    #print(root.val)
    traverse(root.left)
    print(root.val)
    traverse(root.right)
    #print(root.val)

#---------------------------
root=TreeNode(3)
l_level1=TreeNode(9)
r_level1=TreeNode(20)
ll_level2=TreeNode(12)
lr_level2=TreeNode(13)
l_level1.left=ll_level2
r_level1.right=lr_level2

root.right=r_level1
root.left=l_level1

print(root.right.val)

traverse(root)
