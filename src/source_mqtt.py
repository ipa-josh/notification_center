#!/usr/bin/python3
# -*- coding: utf-8 -*-

from source import Source
import paho.mqtt.client as mqtt
from threading import Thread
from time import sleep

class SourceMQTT(Source):

	def __init__(self, config):
		Source.__init__(self, "mqtt", config)
		self.new_content=[]
		self.mqttc = mqtt.Client()
		
		self.mqttc.on_connect = self.on_connect
		self.mqttc.on_message = self.on_message

		self.mqttc.connect(self.get("server"), int(self.get("port")), 60)
		
	def listen(self):
		self.thread = Thread(target = self.run)
		self.thread.start()
		
	def run(self):
		self.mqttc.loop_forever()

	def on_connect(self, client, userdata, flags, rc):
		client.subscribe("online/#")
		client.subscribe("offline/#")

	def on_message(self, client, userdata, msg):
		print(msg.topic+" "+str(msg.payload))
	
	def clear(self):
		self.new_content=[]
			
	def summary(self):
		return [str(len(self.new_content))+" neue E-Mails"]
		
	def text(self):
		return self.new_content
		
	def priority(self):
		return [0]

def create(config):
	return SourceMQTT(config)
