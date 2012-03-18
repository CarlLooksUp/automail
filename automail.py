#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText

def send_email(mail_settings, subject, body):
    mail_obj = MIMEText(msg)
    mail_obj['Subject'] = subject
    mail_obj['From'] = mail_settings['sender_addr']
    mail_obj['To'] = mail_settings['to_addrs'][0]
    for addr in mail_settings['to_addrs'][1:]:
      mail_obj['To'] += ", " + addr 

    sender = smtplib.SMTP('smtp.gmail.com', 587)
    sender.ehlo()
    sender.starttls()
    sender.ehlo()
    sender.login(mail_settings['sender_addr'], mail_settings['sender_pass'])
    sender.sendmail(mail_settings['sender_addr'], mail_settings['to_addrs'],
                    mail_obj.as_string())
    sender.close()

def parse_settings(file_loc):
    """helper to create dict from email settings file"""
    fp = open(file_loc, 'r')
    settings = {}
    for line in fp:
      key, value = line.split('=')
      key = key.strip()
      value = value.strip()
      if value[0] == '[':
        value = value[1:-1]
        value = value.split(',')
        print value
        for idx, val in enumerate(value):
          value[idx] = value[idx].strip()

      settings[key] = value
    return settings


