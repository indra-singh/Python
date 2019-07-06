#Write a program to print if a number is a prime number *

n=int(input("Enter lower number :"))
m=int(input("Enter upper number :"))
print("Prime numbers between",n,"and",m,"are:")
for num in range(n,m+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
               break
            else:
                print(num)
