#Importing libraries
from __future__ import with_statement
import contextlib
try:
from urllib.parse import urlencode
except ImportError:
from urllib import urlencode
try:
from urllib.request import urlopen
except ImportError:
from urllib2 import urlopen
import sys

#Function to shorten a URL using tinyurl api
def do_short(url):
request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
with contextlib.closing(urlopen(request_url)) as response:
return response.read().decode('utf-8')


#Getting input and sending short URL
long_url = input("enter the long URL: ")
 
short_url = do_short(long_url)
print("Short url is: ",short_url)
