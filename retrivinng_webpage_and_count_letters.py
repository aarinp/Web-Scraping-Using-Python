import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count={}
for line in fhand:
    words=line.decode().strip()
    print (words)
    
    for letters in words:
        count[letters]=count.get(letters,0)+1
print(" ")
print (count)
    
