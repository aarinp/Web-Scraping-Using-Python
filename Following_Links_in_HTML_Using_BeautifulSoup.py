import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.check_hostname=ssl.CERT_NONE

count=int(input("Enter Count: "))
position=int(input("Enter Position: "))
url = input("Enter the URL:- ")

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print (s[position-1])
    print (t[position-1])
    url = s[position-1]
