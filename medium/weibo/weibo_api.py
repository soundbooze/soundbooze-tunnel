import os
from weibo_api.client import WeiboClient

WEIBOID = '7313234172'

client = WeiboClient()

p = client.people(WEIBOID)

#print p.name

for status in p.statuses.page(1):

    '''
    print status.id
    print status.text
    print status.created_at
    '''

    if status.pic_urls is not None:
        for url in status.pic_urls: 
            print url
            print os.path.basename(url)
            #os.system('wget ' + ur + ' &')
