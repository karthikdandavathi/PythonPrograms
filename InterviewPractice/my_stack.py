
class Stack(object):

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def size(self):
		return len(self.items)


s = Stack()

s.push(1)
s.push(2)
s.push(3)

while s.size()>0:
	s.pop()


print(s.is_empty())
print(s.size())
