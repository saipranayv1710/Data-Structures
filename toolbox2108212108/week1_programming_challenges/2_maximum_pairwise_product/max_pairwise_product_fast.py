# Second method to decrease the time complexity
def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_product = 0
    
    #find max_index1
    max1 = max(numbers)
    max_index1 = numbers.index( max(numbers))
    
    max2 = 0
    for idx,num  in enumerate(numbers):
        if idx!=max_index1:
            max2 = max(max2,num)
            
    max_product =  max1*max2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
