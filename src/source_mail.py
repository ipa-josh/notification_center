#!/usr/bin/python3

import Source from source
import smtplib
import time
import imaplib
import email

class SourceMail(Source):

	def __init__(self, config):
		self.Source("mail", config)
		self.new_content=[]

	def read(self):
		try:
			mail = imaplib.IMAP4_SSL(self.get("server"))
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

		except Exception, e:
			print str(e)
			
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
