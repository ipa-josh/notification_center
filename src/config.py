#!/usr/bin/python3

import configparser

'''
example configuration (generate default configuration with: Config("").write("defaults.ini")

[whatsapp]
qr = /myfolder/tostore/qrcode.png

'''
class Config:
	
	def __init__(self, filename):
		self.config = configparser.ConfigParser()
		
		#setup defaults
		self.config['global']={}
		self.config['mail']={}
		self.config['dwd']={}
		self.config['whatsapp']={}
		
		self.config['global']['modules'] = "mail"
		
		self.config['whatsapp']['qr'] = "qr.png"
		
		self.config['mail']['interval'] = "600"
		self.config['mail']['server'] = ""
		self.config['mail']['email'] = ""
		self.config['mail']['password'] = ""
		
		self.config['dwd']['url'] = "https://www.dwd.de/DWD/warnungen/warnapp/json/warnings.json"
		self.config['dwd']['region_id'] = "109776000,109780000"
		
		self.config.read(filename)
		
	def write(self, filename):
		self.config.write(filename)
		
	def filename_qr(self):
		return self.config['whatsapp']['qr']
		
	def get(self, tags):
		v=self.config
		for t in tags:
			if t in v: v = v[t]
			else: return None
		return v
