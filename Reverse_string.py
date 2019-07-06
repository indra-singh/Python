#Program : reverse string.
print("###  reverse string using for loop  ###  ")
 #Usiing for loop
def reverse_str(s):
    new_string = ""
    for i in s:
        new_string=i+new_string
    return new_string

print(reverse_str("INDRA"))

print("###  reverse string using recursion  ### ")
#using Recursion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

print (reverse("INDRASINGH"))

#using slice
name=input("enter the name:")
print(name[::-1])
def reverse_slice(s):
    if len(s) == 0:
        return s
    else:
        return s[::-1]

print (reverse_slice("INDRA KUMAR SINGH"))

#Reversed usingh join

def reverse4(s):
    if len(s) == 0:
        return s
    else:
        return "".join(reversed(s))

print (reverse4("IKSINGH"))

