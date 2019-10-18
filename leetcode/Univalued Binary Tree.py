# 965. Univalued Binary Tree

```
class Solution:    
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: #如果沒有左右腳直接回傳True
            return True
        
        if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
            return False  #先從左腳開始，如果左腳質與root不一樣則回傳False，右腳同理
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
```
