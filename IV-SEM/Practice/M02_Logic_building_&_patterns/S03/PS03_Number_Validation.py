'''
# find largest number(using you logic building and patterns) from the given list of numbers
numbers = [3, 5,7, 2, 8, 1]

largest = numbers[0] # assume first number is largest
for num in numbers:
    if num > largest:
        largest = num
        print(largest)
        
#'''
2) steps to find largest number:
1. Assume the first number in the list is the largest and store it in a variable called 'Largest'.




1) find the sum of numbers in the array
a=[]
for i in range(5):
    num=int(input("Enter a number:"))
    a.append(num)