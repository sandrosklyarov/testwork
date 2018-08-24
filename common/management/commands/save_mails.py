#coding=utf-8
import quopri
import base64

from dateutil.parser import parse
from django.core.management.base import BaseCommand
import imaplib
import email
import email.header
import urllib.parse
from emails.models import EMailPost, Tag
from testwork.settings import EMAIL_PASS, EMAIL_LOGIN

def extract_body(payload):
    if isinstance(payload, str):
        return payload
    else:
        return ''.join([extract_body(part.get_payload()) for part in payload])

def normal_code(text):
    decoder = email.header.decode_header(text)
    decode_array = decoder[0]
    if decode_array[1]:
        return decode_array[0].decode(decode_array[1])
    return base64.b64decode(text).decode('utf-8')

class Command(BaseCommand):

    def handle(self, *args, **options):
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login(EMAIL_LOGIN, EMAIL_PASS)
        mail.list()
        mail.select("inbox")
        result, data = mail.uid('search', None, 'UNSEEN')
        tags = [x.text.lower() for x in Tag.objects.filter(moderated=True)]
        for num in data[0].split():
            typ, msg_data = mail.uid('fetch', num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode("utf-8") )
                    subject_decode = msg['subject']

                    #ОПИСАНИЕ
                    subject = normal_code(subject_decode)
                    is_filter = False
                    for tag in tags:
                        if subject.lower().__contains__(tag):
                            is_filter = True
                            break
                    if not is_filter:
                        continue

                    # ТЕКСТ
                    payload = msg.get_payload()
                    body = extract_body(payload)
                    body = normal_code(body)

                    # ОТПРАВИТЕЛЬ
                    sender = msg['sender']
                    if not sender:
                        sender = msg['from'].split('<')[-1].replace('>', '')

                    # ДАТА
                    date = msg['date']
                    if date:
                        date = parse(date)
                    else:
                        date = str(msg).split('\n')[0].split(' ')[3:]
                        date = parse(' '.join(date))
                    obj = EMailPost.objects.create(sender=sender, created=date, description=subject, text=body)



        mail.logout()
