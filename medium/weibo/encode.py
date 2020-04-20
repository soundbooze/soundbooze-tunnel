import re
import sys
from PIL import Image

SIZE   = 690

REGEX  = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
              25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
              25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
              25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def validate_ipaddress(ipaddress):  
    if(re.search(REGEX, ipaddress)):
        return True
    else:  
        return False

ipaddress = sys.argv[1]
image1 = Image.open(sys.argv[2])
image2 = Image.open(sys.argv[3])

if validate_ipaddress(ipaddress):

    z = ipaddress.split('.')

    w1, h1 = image1.size
    w2, h2 = image2.size

    image1 = image1.resize((w1, h1))
    image2 = image2.resize((w2, h2))

    #print image1.format, image1.mode, image1.size
    #print image2.format, image2.mode, image2.size

    new_image1 = image1.resize((w1-int(z[0]), h1-int(z[1])))
    new_image2 = image2.resize((w2-int(z[2]), h2-int(z[3])))

    #print new_image1.size, new_image2.size

    new_image1.save('out1.jpg')
    new_image2.save('out2.jpg')   

else:
    print 'Error validating IP Address'
