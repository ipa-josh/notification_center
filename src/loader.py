#!/usr/bin/python3

import importlib

class Loader:
	
	def __init__(self, config, sub):
		self.config = config
		self.sources=[]
		
		modules = self.config.get(["global", "modules"])
		
		for m in modules.split(","):
			self.sources.append(importlib.import_module("source_"+m).create(config))
			
		for s in self.sources:
			s.subscribe(sub)
			s.listen()
