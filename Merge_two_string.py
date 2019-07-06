'''
a = input("Your first string.")
b = input("Your second string.")
print (a+b)
'''
#s1='ram'
#s2='sin'
#output= rsaimn


#merge 2 string alternatively letters.
a = input("Your first string.")
b = input("Your second string.")

i=0
j=0
newstring=""    # take a empty string
while i< len(a) and j<len(b):
    newstring += a[i]
    newstring += b[j]
    i+=1
    j+=1

while i<len(a):
    newstring += a[i]
    i+=1
while j<len(b):
    newstring += b[j]
    j+=1
print(newstring)


"""
# if a and b length are same.
a = input("Your first string.")
b = input("Your second string.")
i,j=0,0
op=''
while i< len(a) or j<len(b):
    op=op+a[i]+b[j]
    i+=1
    j+=1
print(op)

# if a and b length are diff.

a = input("Your first string.")
b = input("Your second string.")
i,j=0,0
op=''
while i< len(a) or j<len(b):
    if i<len(a):
        op=op+a[i]
        i+=1
    if i<len(b):
        op=op+b[j]
        j+=1
print(op)
"""



