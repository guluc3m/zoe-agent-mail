# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

import smtplib
import json

from email.message import EmailMessage
from email.headerregistry import Address
from zoe import *

@Agent('Mail')
class MailAgent:

    @Intent('mail.send')
    def receive(self, intent):
        dest = intent['recipient']['email']
        # send email...
        return {
            'data': 'notification',
            'from': 'email',
            'text': 'message sent'
        }

    @Intent('mail.zoeMail')
    def sendMail(self, intent):
        """ Send a mail as Zoe

            :param intent: Intent with the format:
                { 'intent': 'mail.zoeMail',
                  'dest': ['destinationMail', ...],
                  'subject': 'text',
                  'content': 'text',
                  'adjunt': [doc1, [doc2...]] (WIP)
                }
                destinationMail it's a list of tuples with pair (name,email)
                adjunt <optional>: List of files to adjunt to the mail in base64. 

            :return None.

            Example:
            { 'intent': 'mail.zoeMail','dest': [("Nombre", "correo")]],'subject': 'Prueba','content': 'Esto es una prueba muy largo'}
        """

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()

        config = json.load(open("config.json"))

        msg = EmailMessage()
        msg['Subject'] = intent['subject']
        msg['From'] = Address("Zoe", config['email'])
        msg['To'] = [Address(mail[0], mail[1]) for mail in intent['dest']]
        msg.set_content(intent['content'])

        server.login(config['email'],config['password'])
        server.send_message(msg)
        server.quit()

        return {
            'data': 'log',
            'from': 'email',
            'text': 'Success sending mail'
        }
