import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter the Url: ")
html=urllib.request.urlopen(url,context=ctx).read()
print('Retrieved', len(html), 'characters')
texthtml=html.decode()
tree=et.fromstring(texthtml)
lst=tree.findall('.//comment')
lst1=[]
print("Comment count: ",len(lst))
for item in lst:
    num=item.find('count').text
    number=int(num)
    lst1.append(number)
print("Sum",sum(lst1))
