#!/usr/bin/python3

from source import Source
import smtplib
import time
import imaplib
import email
from threading import Thread
from time import sleep
import traceback

class SourceMail(Source):

	def __init__(self, config):
		Source.__init__(self, "mail", config)
		self.new_content=[]
		
	def listen(self):
		self.thread = Thread(target = self.run)
		self.thread.start()
		
	def run(self):
		while True:
			self.read()
			sleep(int(self.get("interval")))

	def read(self):
		try:
			mail = imaplib.IMAP4_SSL(self.get("server"))
			mail._mode_utf8() #enable('UTF8=ACCEPT')
			mail.login(self.get("email"),self.get("password"))
			mail.select('inbox')

			type, data = mail.search(None, 'ALL')
			mail_ids = data[0]

			id_list = mail_ids.split()   
			first_email_id = int(id_list[0])
			latest_email_id = int(id_list[-1])


			for i in range(latest_email_id,first_email_id, -1):
				typ, data = mail.fetch(i, '(RFC822)' )

				for response_part in data:
					if isinstance(response_part, tuple):
						msg = email.message_from_string(response_part[1])
						email_subject = msg['subject']
						email_from = msg['from']
						self.new_content.append(msg['subject']+" von "+msg['from'])

		except Exception as e:
			print(str(e))
			traceback.print_exc()
			
		if len(self.new_content)>0:
			self.notify()
	
	def clear(self):
		self.new_content=[]
			
	def summary(self):
		return [str(len(self.new_content))+" neue E-Mails"]
		
	def text(self):
		return self.new_content
		
	def priority(self):
		return [0]

def create(config):
	return SourceMail(config)
