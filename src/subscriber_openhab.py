#!/usr/bin/python3

class SubscriberOpenHAB:
	
	def __init__(self, config):
		self.name = "SubscriberOpenHAB"
		self.config = config
		self.subscribers = []
		
	def name(self):
		return self.name
		
	def notify(self, source):
		self.speak(source.summary())
		
	def speak(self, text):
		print(text)
