class TreeNode:
    left = None
    right = None
    def __init__(self, val):
        self.val = val
        
    
def find_bst(cur, val):
    if not cur or val == cur.val:
        return cur
    if val < cur.val:
        return find_bst(cur.left, val)
    return find_bst(cur.right, val)

root = TreeNode(18)
root.left = TreeNode(7)
root.right = TreeNode(27)
root.left.left = TreeNode(4)
root.left.right = TreeNode(15)
print(find_bst(root, 4).val)