#  import html
#  import http
#  import requests
import urllib
from  urllib import request
import lxml.etree

url = r'services.tvrage.com/feeds/search.php?show=heroes'
#  showName = r'C:\Downloads\The Adjustment Bureau.avi'
#  page = urllib.urlopen(page)
#  data = urllib.request.urlopen(url).read()
#  page =  request.urlopen(url).read()
print(page)
#  page = requests.get()

print(lxml.etree.tounicode(url))



# >>> NSMAP = {None: 'http://www.w3.org/2005/Atom'}                     ①
# >>> new_feed = lxml.etree.Element('feed', nsmap=NSMAP)                ②
# >>> print(lxml.etree.tounicode(new_feed))                             ③
# <feed xmlns='http://www.w3.org/2005/Atom'/>
# >>> new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')  ④
# >>> print(lxml.etree.tounicode(new_feed))
# <feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'/>