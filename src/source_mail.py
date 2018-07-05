#!/usr/bin/python3

import Source from source
import smtplib
import time
import imaplib
import email

class SourceMail(Source):

	def __init__(self, config):
		self.Source("mail", config)

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
						print 'From : ' + email_from + '\n'
						print 'Subject : ' + email_subject + '\n'

		except Exception, e:
			print str(e)
