class Node(object):

	def __init__(self, value, leftNode, rightNode):
		super(Node, self).__init__()
		self.value = value
		self.leftNode = leftNode
		self.rightNode = rightNode

	def setValue(value):
		self.value = value

	def getValue(self):
		return self.value

	def setRightNode(self, rightNode):
		self.rightNode = rightNode

	def getRightNode(self):
		return self.rightNode

	def setLeftNode(self, leftNode):
		self.leftNode = leftNode

	def getLeftNode(self):
		return self.leftNode

def sumOfMaxPath(node):
	value = node.getValue()
	return max(value + sumOfPath(node.getLeftNode()), value + sumOfPath(node.getRightNode()))

def sumOfPath(node):
	rightSum = 0
	leftSum = 0
	if node.getRightNode() is not None:
		rightSum += sumOfPath(node.getRightNode())
	if node.getLeftNode() is not None:
		leftSum += sumOfPath(node.getLeftNode())
	if node.getRightNode() is None and node.getLeftNode() is None:
		return node.getValue()
	return max(node.getValue() + leftSum, node.getValue() + rightSum)

if __name__ == '__main__':
	tree = Node(3, 
		Node(7, Node(2, Node(8, None, None), Node(5, None, None)), Node(4, Node(5, None, None), Node(9, None, None))), 
		Node(4, Node(4, Node(5, None, None), Node(9, None, None)), Node(6, Node(9, None, None), Node(3, None, None))))
	print(sumOfMaxPath(tree))