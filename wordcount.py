from bs4 import BeautifulSoup as bae
import requests
import requests_cache

get = lambda i:requests.get('http://hpmor.com/chapter/'+str(i)).text

i = 1
total = 0

while True:
 try:
  words = len(bae(get(i)).find(id="storycontent").get_text().split())
  total += words
  print 'Chapter',i,'has',words,'words'
  i += 1
 except:
  break

print 'for a grand total of',total,'words!'
