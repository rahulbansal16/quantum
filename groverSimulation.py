'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def mean(a):
    m = 0 
    for i in a:
        m =  m + i
    return m/(len(a)*1.0)

def reflect(a):
    m = mean(a)
    for i in range(0,len(a)):
        a[i] = 2*m - a[i]
    return a


def bb(a):
    a[9] = -a[9]
    return a


def firstBB():    
    a = [0]*16
    for i in range(16):
        a[i] = 1/4.0
    a[9] = -1/4.0
    return a
    
# BB
a = firstBB()
print(a)
for i in range(4):
    a = reflect(a)
    a = bb(a)
print(a)    
    



    
    



