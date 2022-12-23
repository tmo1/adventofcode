#! /usr/bin/python3

# https://adventofcode.com/2021/day/18

import sys

class Node:
	def __init__(self, value = None):
		self.left  = None
		self.right = None
		self.value = value

def add(a, b):
	node = Node()
	node.left = a
	node.right = b
	return node

def dfs(node):
	stack = [[node, 0]]
	nodes = []
	while stack:
		n, depth = stack.pop()
		nodes.append([n, depth])
		if n.right is not None:
			stack.append([n.right, depth + 1])
		if n.left is not None:
			stack.append([n.left, depth + 1])
	return nodes
			
def explode(node):
	nodes = dfs(node)
	for i in range(len(nodes)):
		if nodes[i][1] > 4 and nodes[i][0].value is not None and i < len(nodes) - 1 and nodes[i + 1][0].value is not None:
			for j in range(i - 1, -1, -1):
				if nodes[j][0].value is not None:
					nodes[j][0].value += nodes[i][0].value
					break
			for j in range(i + 2, len(nodes)):
				if nodes[j][0].value is not None:
					nodes[j][0].value += nodes[i + 1][0].value
					break
			nodes[i - 1][0].value, nodes[i -1][0].left, nodes[i - 1][0].right = 0, None, None
			return True
	return False
	
def split(node):
	nodes = dfs(node)
	for i in range(len(nodes)):
		if nodes[i][0].value is not None and nodes[i][0].value >= 10:
			left = Node(nodes[i][0].value // 2)
			right = Node(nodes[i][0].value // 2 + (1 if nodes[i][0].value % 2 == 1 else 0))
			nodes[i][0].value, nodes[i][0].left, nodes[i][0].right = None, left, right
			return True
	return False

def red(node):
	unfinished = True
	while unfinished:
		unfinished = explode(node)
		if not unfinished:
			unfinished = split(node)

def magnitude(node):
	if node.value is not None:
		return node.value
	m = 0
	if node.left is not None:
		m += 3 * magnitude(node.left)
	if node.right is not None:
		m += 2 * magnitude(node.right)
	return m
	
def parse(num):
	node = Node()
	while True:
		c = num.pop()
		if c == '[':
			child = parse(num)
			if node.left is None:
				node.left = child
			else:
				node.right = child
		if c == ']':
			return node
		if c.isdigit():
			while num[-1].isdigit():
				c += num.pop()
			if node.left is None:
				node.left = Node(int(c))
			else:
				node.right = Node(int(c))

total = None
for line in sys.stdin:
	num = list(line.strip())
	num.reverse()
	num.pop()
	node = parse(num)
	total = add(total, node) if total is not None else node
	red(total)
print(magnitude(total))
