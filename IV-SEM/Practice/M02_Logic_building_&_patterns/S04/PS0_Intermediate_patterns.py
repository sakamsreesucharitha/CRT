#1. Pyramid 
#n = 4
#output:
    *
    * *
    * * *
    * * * *
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
            print()
            '''
            '''
        
li = [1,2,3,4,5]
#output: [2,4,6,8,10]
res = []
for ele in li:
    res.append(ele * 2)
    print(res)
    
    print([ele* 2 for ele in li])
    
    li = [1,2,3,4,5]
    res = [] 
    for i in li:
        if i % 2 == 0:
            res.append(i)
    print(res)
    
    print([i for li in li if li % 2 == 0])
    print(tuple(i for i in li if i % 2 == 0))
    print({i:i*2 for i in li if i % 2 == 0})
    
    li1 = ['a','b','c']
    #"a b c"
    res = " "
    for ch in li1:
        res += res + ch + " " 
    print(res)
    
    5.Palindrome Pattern
    n=4
    output:
        1
        212
        32123
        4321234
        
        n = int(input())
        for i in range(n):
            for j in range(i+1,0,-1):
                print(j,end="")
                for k in range(2,i+2):
                    print(k,end="")
                    print()
                    
                    ''''''
            
    
    
            
            
            
    
    
    
    
    