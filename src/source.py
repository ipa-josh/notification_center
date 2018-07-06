#!/usr/bin/python3

class Source:
	
	def __init__(self, name, config):
		self.name = name
		self.config = config
		self.subscribers = []
		
	def subscribe(self, s):
		self.subscribers.append(s)
		
	def notify(self):
		for s in self.subscribers:
			s.notify(self)
		self.clear()
		
	def clear(self):
		pass
		
	def listen(self):
		pass
			
	def get(self, tag):
		return self.config.get([self.name(), tag])
			
	def name(self):
		return self.name
		
	def name_nice(self):
		return self.name()
		
	def summary(self):
		return []
		
	def text(self):
		return []
		
	def priority(self):
		return []
