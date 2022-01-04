import math
def sin(x, n=10):
    return sum([ ((-1)**k * x**(1 + 2.0*k)) / math.factorial(1 + 2.0*k) for k in range(n) ])

if __name__ == '__main__':
    print(sin(0.8))
    print(math.sin(0.8))    

'''
Output:
0.7173560908995229
0.7173560908995228
'''    