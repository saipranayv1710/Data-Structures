# Max profit shud be multiplied with max_avg click per day
def max_dot_product(a,b):
    if n==0:
        return 0
    
    a = sorted(a)
    b = sorted(b)
    return sum([i*j for i,j in zip(a,b)])
      
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split() ))
    b = list(map(int, input().split() ))
    print(max_dot_product(a,b))