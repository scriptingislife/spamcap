#!/usr/bin/python3
import sys
import json
import email
import hashlib
from datetime import datetime
import boto3

OUTPUT_DIR = '/tmp/'
BUCKET_NAME = 'spamcap'

def create_filename(mime):
    if mime['Message-ID'] is None:
        return str(datetime.now()) + '.json'
        #m = hashlib.md5()
        #return m.update(mime.get_payload()).hexdigest()
    return str(mime['Message-ID']).replace('<', '').replace('>', '') + '.json'

def on_error(stdin):
    with open(OUTPUT_DIR + 'spamcap.err', 'a') as f:
        f.write('\n')
        f.write(stdin)
        f.write('\n')

def main(stdin):
    msg = email.message_from_string(stdin)
    # out = {}
    # out['date'] = msg['Date']
    # out['id'] = msg['Message-Id']
    # out['from'] = msg['from']
    # out['body'] = msg.get_payload()
    # out['raw'] = str(msg)    

    filename = create_filename(msg)
    newlines = str(msg).replace('\\n', '\n')

    s3 = boto3.resource('s3')
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=newlines.encode('utf-8'), ContentType='text/plain', ACL='public-read')

    #with open(OUTPUT_DIR + filename, 'w') as f:
    #    f.write(str(msg).replace('\\n', '\n'))


if __name__ == '__main__':
    stdin = sys.stdin.read()
    try:
        main(stdin)
    except:
        on_error(stdin)