#Number Series: Sequential order of numbers in a particular pattern.
'''1)Print a natural numbers?'''
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)
2)Print n even numbers?
for i in range(2,n+1,2):
    print(i)

3)Print n odd numbers?
for i in range(1,n+1,2):
    print(i)
4)Print n Fibonacci numbers? 0,1,1,2,3,5,8,13,21,34..
n=int(input("Enter a number:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a,b=b,c

    5)Print a multiplication table of a given number?
n=int(input("Enter a number:"))
for i in range(1,21):
    print(n,"x",i, "=",n*i)

6)Print the square of first n natural numbers?

7)print the cube of first n natural numbers?









