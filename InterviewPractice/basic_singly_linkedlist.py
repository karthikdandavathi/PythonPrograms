import sys
import os

class Node(Object):

	def __init__(self,data=None,next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self,new_next):
		self.data = data

class LinkedList(Object):
		