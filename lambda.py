mx=lambda x,y:x if x>y else y
print(mx(8,9))
n=[1,2,3,4,5]
print(list(map(lambda x:x**x,n)))
y=[100,99,101,102,98]
print(list(filter(lambda x:x>=100,y)))