# file:///C:/Users/LENOVO/Desktop/Data%20Structures/toolbox2108212108/week2_algorithmic_warmup/week2_algorithmic_warmup.pdf
# From the Hint mentioned in the above doc
# f0=0
# f1**2 + f2**2 +...+ f5**2    =    f5 * (f5+f4)

def las_digit_fib(n):
    # As we know the length of the period(10) of fibonacci_last digit is 60
    list_60 = [0,1]
    prev,curr = 0,1
    for _ in range(2,60):
        prev,curr = curr, (prev+curr)%10
        list_60.append( curr )

    rem = n%60
    return list_60[rem]

def squares_fibo(n):
    if n<=1:
        return n
    else:
        f5 = las_digit_fib(n)
        f4 = las_digit_fib(n-1)

        return (f5 * (f5+f4))%10

if __name__ == '__main__':
    n = int(input())
    print(squares_fibo(n))