import re

file=input("Enter File's Name: ")
handle = open(file)
initial=0
for line in handle:
    a=line.rstrip()
    digit=re.findall('[0-9]+',a)
    for i in range(len(digit)):
        num=digit[i]
        number=int(num)
        initial=initial+number
print(initial)
        
        

