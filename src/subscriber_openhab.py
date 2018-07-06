#!/usr/bin/python3
from openhab2 import openHAB

class SubscriberOpenHAB:
	
	def __init__(self, config):
		self.name_ = "SubscriberOpenHAB"
		self.config = config
		self.subscribers = []
		
		self.openhab = openHAB(self.get("url"))
		
	def get(self, tag):
		return self.config.get(["openhab",tag])
		
	def name(self):
		return self.name_
		
	def notify(self, source):
		self.speak(source.summary())
		
	def speak(self, text):
		print(text)
		
		try:
			for alexa in self.get("alexas").split(","):
				item = openhab.get_item(alexa)
				item.state = text
		except:
			print("failed to pass text to alexa")
