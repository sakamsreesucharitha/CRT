'''set:

1. Use {} to create a set
2. set does not allow duplicate values
3. set is unindexed
4.set is unordered
5.set is mutable
6.set is heterogeneous
'''
s = {1,True,10,12.45,10,9+5j}
print(s,type(s))
print(s[3])

    
    
    #adding elements
    A = {1,2,3}
    B = {3,4,5}
    A.add(4)
    B.update({6,7})
    print(A,B)
    
    #removing elements
    A.remove(2)
    ''''''
    
1) Definition 