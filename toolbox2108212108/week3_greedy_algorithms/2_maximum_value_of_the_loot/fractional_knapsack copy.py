# Uses python3
# file:///C:/Users/LENOVO/Desktop/Data%20Structures/toolbox_slides/02_greedy_3_fractionalknapsack.pdf

def get_optimal_value(W,l):
    
    # Sorting based on the vi/wi values in DESC order
    l = sorted(l , key = lambda x: x[0]/x[1], reverse=True)    
    
    V = 0
    for i in range(n):
        # l[i][0] is Value and l[i][1] is weight

        if W==0:
            return V

        a = min( l[i][1] , W)
        V = V+ a*(l[i][0] / l[i][1])
        W = W-a

    return V


if __name__ == "__main__":
    n, capacity = list(map(int, input().split()))
    values_weights = [ list(map(int, input().split())) for _ in range(n)]
    opt_value = get_optimal_value(capacity, values_weights)
    print("{:.4f}".format(opt_value))
