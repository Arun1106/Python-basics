import re
a="abcded@gmail.com"
if re.findall("\w[a-z]@[a-z].[a-z]{2,3}",a):
    print("valid")
else:
    print("not valid")