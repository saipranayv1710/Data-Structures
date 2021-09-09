# Uses python3
# Uses python3
import sys

# Fibonacci code
def fibonacci(num):
    if num<=1:
        return num
    
    prev, curr = 0,1
    for _ in range(num-1):
        prev,curr = curr, prev+curr
    return curr

# Period_length code
# https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/
# https://en.wikipedia.org/wiki/Pisano_period#Pisano_periods_of_Fibonacci_numbers
# Code in inspired from above pages and with slight modifications
# The period always starts with 01 and is known as Pisano period.

def pisano_period(m):
    
    prev,curr = 0,1
    
    # The length of a Pisano Period for a given m ranges from 3 to m * m
    for i in range(0,m*m):
        prev,curr = curr, (prev+curr)%m
        
        #As period start with 0 and 1 and Return period_length
        if prev==0 and curr==1:
            return i+1

# As explained in the week2_algorithmic_warmup.pdf
# For F(2019) mod 5  the period_length will be 20
# 2019/20 = 19 ; new n will be 19 - F19 mod 5 
# Idea here is insted of computing F2019, we compute F19 to get the answer

def fibonacci_mod(n,m):
    
    period_length = pisano_period(m)
    n = n%period_length
    
    #Now compute the mod for F(new_n)
    return fibonacci(n)%m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_mod(n, m))
