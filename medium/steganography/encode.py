import os
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

EMBEDJSON   = "embed.json"

def validate_ipaddress(ipaddress):  
    if(re.search(REGEX, ipaddress)):
        return True
    else:  
        return False

def pad_plaintext(message):
    for i in range(32 - len(message)): # Pad until 32 characters
        message += " "
    return message

def encrypt_aes(plaintext):
    encrypt_AES = AES.new(PASSWORD, AES.MODE_CBC, IV)
    return encrypt_AES.encrypt(plaintext)

def write_json(ciphertext):
    data = { "bc" : ciphertext }
    with open(EMBEDJSON, 'w') as json_file:
        json.dump(data, json_file)

image     = sys.argv[1] 
ipaddress = sys.argv[2]
output    = sys.argv[3]

if validate_ipaddress(ipaddress):

    ipaddress = pad_plaintext(ipaddress)
    ciphertext = encrypt_aes(ipaddress)
    write_json(base64.b64encode(ciphertext))
    steganopy.api.create_stegano_image(original_image=image, data_to_hide=EMBEDJSON).save(output)
    os.remove(EMBEDJSON)

else:
    print 'Error validating IP Address'
