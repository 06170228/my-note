#def for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return Solution().insert(root.left, val)
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return Solution().insert(root.right, val)

    def FindMintarget(self, curr):
        while curr.left != None:
            curr = curr.left

        return curr

    def delete(self, root, target):
        #store parent node of current node
        parent = None
        #start with root node
        current = root
        #search target in BST and set its parent 
        while current != None and current.val != target:
            #update parent node as current node
            parent = current

            #if given target is less than the current node, 
            #go to left subtree
            if target < current.val:
                current = current.left
            # else go to right subtree
            else:
                current = current.right
        #return if target is not found in the tree
        if current == None:
            return root
        
        #Case 1: node to be deleted has no children i.e. it is a leaf node
        if current.left == None and current.right == None:
            #if node to be deleted is not a root node, then set its
            #parent left/right child to null
            if current != root:
                if parent.left == current:
                    parent.left == None
                else:
                    parent.right == None
            
            #if tree has only root node, delete it and set root to null
            else:
                root = None
        
        #Case 2: node to be deleted has two children
        elif current.left != None and current.right != None:
            #find its in-order successor node
            minimumkey = Solution().FindMintarget(current.right)
            #store successor value
            key = minimumkey.val

            #recursively delete the successor. Note that the successor
            #will have at-most one child (right child)
            Solution().delete(root, minimumkey.val)

            #Copy the value of successor to current node
            current.val = key

        #Case 3: node to be deleted has only one child
        else:
            #find child node
            if current.left != None:
                child = current.left
            else:
                child = current.right

            #if node to be deleted is not a root node, then set its parent
            #to its child
            if current != root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child

            #if node to be deleted is root node, then set the root to child
            else:
                root = child
        if Solution().search(root, target) != None:
            Solution().delete(root, target)
        return root

    def search(self, root, target):
        #root is noll or target is present
        if root is None or root.val == target:
            return root
        #target is smaller than root's
        if root.val > target:
            return Solution().search(root.left, target)
        #target is greater than root's
        else:
            return Solution().search(root.right, target)

    def REmodify(self, root, target, new_val):
        if root is None or root.val == target:
            if root.right != None and new_val >= root.right.val:
                root.val = new_val
                return root
            elif root.left != None and new_val >= root.left.val:
                root.val = new_val
                return root
        elif root.val > target:
                #smaller than root greater than target.left
            if new_val <= root.val:
                return Solution().REmodify(root.left, target, new_val)
        elif root.val <= target:
            return Solution().REmodify(root.right, target, new_val)
        return root

    def modify(self, root, target, new_val):
        Solution().REmodify(root, target, new_val)
        if (Solution().search(root, target) != None):
            Solution().delete(root, target)
            Solution().insert(root, new_val)
        return root
