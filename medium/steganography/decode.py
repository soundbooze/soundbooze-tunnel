import re
import sys
import json
import base64

import steganopy.api
from Crypto.Cipher import AES

PASSWORD    = '56a98559dd30621f' # key has to be 16, 24 or 32 bytes long
IV          = 'bd5d78903a919be2'

REGEX       = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
              25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
              25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
              25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def validate_ipaddress(ipaddress):  
    if(re.search(REGEX, ipaddress)):
        return True
    else:  
        return False

def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return data['bc']

def decrypt_aes(ciphertext):
    decrypt_AES = AES.new(PASSWORD, AES.MODE_CBC, IV)
    return decrypt_AES.decrypt(ciphertext)

image = sys.argv[1]
payload = steganopy.api.extract_data_from_stegano_image(image=image)
b64_cipher = json.loads(payload)['bc']

ipaddress = decrypt_aes(base64.b64decode(b64_cipher))

if validate_ipaddress(ipaddress):
    print ipaddress
else:
    print 'Error validating IP Address'
