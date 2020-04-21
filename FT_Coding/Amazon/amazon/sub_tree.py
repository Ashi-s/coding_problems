class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def compare(tree_1, tree_2):

	if tree_1 is None and tree_2 is None:
		return True
	if tree_1 is None or tree_2 is None:
		return False
	return (tree_1.val == tree_2.val and
			compare(tree_1.left , tree_2.left) and
			compare(tree_1.right, tree_2.right)
			)


def isSubtree(root1, root2):
    if root2 is None:
        return 1
    if root1 is None:
        return -1

    if traverse(root1, root2):
        return 1
    else:
        return -1

def traverse(root1, root2):
    if root2 == None:
        return True

    if root1 == None:
        return False

    if root1.val == root2.val:
        return traverse(root1.left, root2.left) and traverse(root1.right, root2.right)

    return traverse(root1.left, root2) or traverse(root1.right, root2)
