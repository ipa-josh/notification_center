#!/usr/bin/python3

from source import Source
from threading import Thread
from time import sleep
import traceback
from urllib.request import urlopen
import json


def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data.replace("warnWetter.loadWarnings(","")[:-2])

class SourceDWD(Source):

	def __init__(self, config):
		Source.__init__(self, "dwd", config)
		self.new_content=[]
		
	def listen(self):
		self.thread = Thread(target = self.run)
		self.thread.start()
		
	def run(self):
		while True:
			self.read()
			print(self.config.get(["mail", "interval"]))
			sleep(int(self.config.get(["mail", "interval"])))

	def read(self):
		try:
			data = get_jsonparsed_data(self.get("url"))

		except Exception as e:
			print(str(e))
			traceback.print_exc()
			
		if len(self.new_content)>0:
			self.notify()
	
	def clear(self):
		self.new_content=[]
			
	def summary(self):
		return [str(len(self.new_content))+" neue Warnungen"]
		
	def text(self):
		return self.new_content
		
	def priority(self):
		return [0]

def create(config):
	return SourceDWD(config)
