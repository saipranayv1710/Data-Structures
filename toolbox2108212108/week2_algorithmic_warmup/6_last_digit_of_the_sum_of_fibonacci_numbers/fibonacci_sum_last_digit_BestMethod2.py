# Uses python3
import sys

# Length of period when period = m
def pisano_period(m):
    
    prev,curr = 0,1
    
    # length of period ranges btw 3 and m*m 
    for i in range(0,m*m):
        prev,curr = curr, (prev+curr)%m
        
        if prev==0 and curr==1:
            return i+1


def second_BestMethod_for_Last_digit_sum_of_fib_numbers(n):

    period_length = 60  # pisano_period(10)

    # For ex: we have to get sum of last digits of n - fib numbers
    # lets sum till F123 - to get last digit we can use period 10
    # perfect_bin1, perfect_bin2, remiander_bin = f0-f59, f60-119, f120-f123 
    # This can (f0-f59)*2 + (f0-f3)

    # To compute no of perfect bins
    cnt_of_perfect_bins = n//period_length

    # reminder bin length =  f120-f123 = f0-f3 = last_digit_of_sum_of_fibonacci(3)
    rem = (n%period_length)

    # As the period is only 60, if we store the last digits of first 60 fibonacci numbers in a list to would be easy to compute
    # f0-f59 last digits should be stored in a list
    list_60 = [0,1]
    prev,curr = 0,1
    for _ in range(2,60):
        prev,curr = curr, (prev+curr)%10
        list_60.append( curr )

    # get sum - f0-f59
    perfect_bin_sum = sum(list_60)%10
    all_perfect_bins_sum = cnt_of_perfect_bins * perfect_bin_sum

    # last_digit_of_sum_of_fibonacci(3) 
    remainder_bin_sum = sum(list_60[:rem+1])%10

    return (all_perfect_bins_sum+remainder_bin_sum) %10


if __name__ == '__main__':
    n = int(input())
    print(second_BestMethod_for_Last_digit_sum_of_fib_numbers(n))
