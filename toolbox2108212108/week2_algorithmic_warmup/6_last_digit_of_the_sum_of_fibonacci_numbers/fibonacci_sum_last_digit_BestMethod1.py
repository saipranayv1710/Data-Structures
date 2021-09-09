# Uses python3
import sys

# Average method to compute last_dig_sum_of_fin numbers, works better for small numbers
def last_digit_of_sum_of_fibonacci(n):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    
    # fib0 + fib1 =1 , fib(2) as so on will be added in the loop
    summ = 1
    prev,curr = 0,1
    for _ in range(n-1):
        prev,curr = curr, (prev+curr)%10
        summ+=curr
        
    return summ%10


# Length of period when period = m
def pisano_period(m):
    
    prev,curr = 0,1
    
    # length of period ranges btw 3 and m*m 
    for i in range(0,m*m):
        prev,curr = curr, (prev+curr)%m
        
        if prev==0 and curr==1:
            return i+1


def BestMethod_for_Last_digit_sum_of_fib_numbers(n):
        period_length = 60  # pisano_period(10)

        # For ex: we have to get sum of last digits of n - fib numbers
        # lets say sum till F123 - to get last digit we can use period 10
        # perfect_bin1, perfect_bin2, remiander_bin = f0-f59, f60-119, f120-f123 
        # This can (f0-f59)*2 + (f0-f3)

        # To compute no of perfect bins
        cnt_of_perfect_bins = n//period_length

        # reminder bin length =  f120-f123 = f0-f3 = last_digit_of_sum_of_fibonacci(3)
        rem_bin_len = (n%period_length)

        # get sum - f0-f59
        perfect_bin_sum = last_digit_of_sum_of_fibonacci(60-1)
        all_perfect_bins_sum = cnt_of_perfect_bins * perfect_bin_sum

        # last_digit_of_sum_of_fibonacci(3) 
        remainder_bin_sum = last_digit_of_sum_of_fibonacci(rem_bin_len)

        return (all_perfect_bins_sum+remainder_bin_sum) %10


if __name__ == '__main__':
    n = int(input())
    print(BestMethod_for_Last_digit_sum_of_fib_numbers(n))
