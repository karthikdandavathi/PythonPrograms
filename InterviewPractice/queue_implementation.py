#implementation with array
class Queue(object):
	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		self.items.pop()

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)



#implementation of stack

class Stack(object):
	def __init__(self):
		self.items =[]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def get_top(self):
		return self.items[-1]


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.pop()
my_stack.push(30)
print(my_stack.get_top())