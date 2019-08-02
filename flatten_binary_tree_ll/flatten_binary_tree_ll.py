        if not root: return None
        
        head = TreeNode(None)
        cur = head
        stack = [root]
        while stack:
            v = stack.pop()
            if v.right:
                stack.append(v.right)
            if v.left:
                stack.append(v.left)
            cur.left = None
            cur.right = v
            cur = cur.right
            
        return head.right