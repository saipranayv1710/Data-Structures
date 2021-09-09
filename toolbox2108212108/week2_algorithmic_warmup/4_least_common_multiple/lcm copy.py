# Uses python3
import sys

def lcm(a,b):
    num = max(a,b)
    i=1
    while True:
        if (num*i)%a==0 and (num*i)%b==0:
            return num*i
        i+=1

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

