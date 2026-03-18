'''1. Square Star Pattern
n = 4
output:
* ***
* *  * *
****
****
'''

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
        print()
'''
2. right angle triangle
n = 4
output:
*
* *
* * *
* * * *
'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
print()
'''
3. inverted right angle triangle
n=4
output:
*
* * *
* * * * *
* * * * * * *
'''

n = int(input())
for i in range(n):
    for j in range(2*i+1):
        print("*",end=" ")
        print()
'''        
4) number triangle
n=4
output:
1
12
123
1234
'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1),end=" ")
        print()
'''
5) repeated number pattern
n=4
output:
    1
    22
    333
    4444
'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
        print()
        
'''
6) alphabet triangle
n=4
output:
    A
    A B
    A B C
    A B C D
'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
        print()
'''     
7) floyd triangle
n=4
output:
    1
    2 3
    4 5 6 
    7 8 9 10
    '''
n = int(input())
num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num += 1
        print()
'''         
8) hollow square
n=4
output:
    ****
    *  *
    *  *
    ****
    '''

        
            
        
    
            
        
        



        


