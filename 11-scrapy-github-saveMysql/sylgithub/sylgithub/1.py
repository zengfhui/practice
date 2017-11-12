a = '2013T02:10:10Z'
b = a.split('T')[0]
c = a.split('T')[1].strip('Z')
d = b+c
print(b,c,d)
