# Uses python3
def fibonacci(num):
    # F0=0 and F1=1
    l = [0,1]
    for i in range(2,num+1):
        l.append( (l[-2]+l[-1])%10 )
    
    return l[num]

n = int(input())
print(fibonacci(n))
