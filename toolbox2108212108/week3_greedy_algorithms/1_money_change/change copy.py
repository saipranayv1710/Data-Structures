# Uses python3
def get_change(n):
    
    # write your code here
    coins = 0
    for den in [10,5,1]:
        rem = n%den
        coins += (n//den)
        n = rem

    return coins 

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))