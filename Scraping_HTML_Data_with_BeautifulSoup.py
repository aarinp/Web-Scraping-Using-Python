import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.check_hostname=ssl.CERT_NONE
list1=[]
list2=[]
digits=0
url = input("Enter the URL:- ")
html=urllib.request.urlopen(url,context=ctx)
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
for tag in tags:
    #print(tag)
    line=tag.decode().rstrip()
    list1.append(line)
for string in list1:
    strings=string.strip()
    #print(strings)
    num=re.findall('[0-9]+',strings)
    list2.append(num)
for num in list2:
    for number in num:
        digits=int(number)+digits
print(digits)
string_digit=str(digits)

#For saving list of string from the  webpage  and Final Output
#file=open('answer_graded_assignment_1.txt','w+')
#file.write("Comments: "+ str(list1))
#file.write('Total Number Of Comments = '+string_digit)
#file.close
