# Uses python3
import sys

#Partial sum
def partial_fibo_sum(m,n):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    
    # fib0 + fib1 =1 , fib(2) as so on will be added in the loop
    summ = 0
    prev,curr = 0,1
    for i in range(2,n+1):
        prev,curr = curr, prev+curr
        if i>=m:
            summ+=curr%10
        
    return summ%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
