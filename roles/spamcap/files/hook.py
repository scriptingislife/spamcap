#!/usr/bin/python3
import sys
import json
import email
import hashlib

OUTPUT_DIR = '/tmp/'

def create_filename(mime):
    if mime['Message-ID'] is None:
        m = hashlib.md5()
        return m.update(mime.get_payload()).hexdigest()
    return str(mime['Message-ID']).replace('<', '').replace('>', '') + '.json'

def on_error(stdin):
    with open('spamcap.err', 'a') as f:
        f.write('\n')
        f.write(stdin)
        f.write('\n')

def main(stdin):
    msg = email.message_from_string(stdin)
    out = {}
    out['date'] = msg['Date']
    out['id'] = msg['Message-Id']
    out['from'] = msg['from']
    out['body'] = msg.get_payload()
    out['raw'] = str(msg)    

    with open(OUTPUT_DIR + create_filename(msg), 'w') as f:
        f.write(json.dumps(out))


if __name__ == '__main__':
    stdin = sys.stdin.read()
    try:
        main(stdin)
    except:
        on_error(stdin)