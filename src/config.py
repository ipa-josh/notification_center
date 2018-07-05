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
		self.config['whatsapp']['qr'] = "qr.png"
		
		self.config.read(filename)
		
	def write(self, filename):
		self.config.write(filename)
		
	def filename_qr(self):
		return self.config['whatsapp']['qr']
