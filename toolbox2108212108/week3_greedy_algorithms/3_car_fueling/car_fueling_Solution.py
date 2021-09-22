# file:///C:/Users/LENOVO/Desktop/Data%20Structures/toolbox_slides/02_greedy_1_intro.pdf

def minCarFueling(d,m,n,x):
    
    # adding sorce and destination points at 0 and n+1 index resp..
    x = [0] + x + [d]
    
    # if distance to be covered is less than the miles/full_tank, then no need of filling
    if m>=d:
        return 0

    current_refill = 0
    num_refill   = 0

    
    # Below loop is to check for the next gas filling station, 
    # when we are at last gas stn then no need of checking further
    while current_refill <=n:
            last_refill = current_refill

            while ( (current_refill <= n) and 
                   ( x[current_refill+1] - x[last_refill]  <= m )):
                current_refill+=1
            
            # curr==last means curr has not moved that means we didn't find gas filling station 
            # in reached distance (m miles)
            if current_refill == last_refill:
                return -1

            if current_refill <= n:
                num_refill+=1

    return num_refill


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    x = list(map(int, input().split()))
    print(minCarFueling(d,m,n,x))