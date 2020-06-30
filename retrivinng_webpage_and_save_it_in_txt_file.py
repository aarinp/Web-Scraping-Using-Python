import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
string=''
for line in fhand:
    words=line.decode().strip()
    string=string+words+"\n"
    print(words)
print ("\n")
print(string)
file=open("DrChucks.txt",'w+')
file.write(string)
file.close
