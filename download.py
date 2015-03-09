from bs4 import BeautifulSoup as bae
import requests
import requests_cache
import sys

get = lambda i:requests.get('http://hpmor.com/chapter/'+str(i)).text

i = 1
total = 0

while True:
 try:
  text = bae(get(i)).find(id="storycontent").get_text()
  text = ''.join([c for c in text if c.lower() in '\nabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+[]{}\'";,.\\/?'])
  open('chapter_'+str(i)+'.txt','w').write(text)
  sys.stdout.write('\rDownloaded up to chapter '+str(i))
  sys.stdout.flush()
  i += 1
 except:
  break

print ''
