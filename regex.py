x="Arun is 30 Ravi is 40"
import re
age=re.findall(r'\d{1,3}',x)
name=re.findall(r'[A-Z][a-z]*',x)
d={}
x=0
for i in name:
    d[i]=age[x]
x=x+1
print(d)