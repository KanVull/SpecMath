import math
from scipy.interpolate.interpolate import interp1d

def linear_interpolation(x: list, y: list, X):
    '''
    x -> list of x arguments
    y -> list size of x list and have values of your f(x)
    X -> list of x arguments you found the y
    returns: list of Y values
    '''
    x, y = zip(*sorted(zip(x, y)))
    Y = list()
    for find_x in X:
        if find_x > x[-1] or find_x < x[0]:
            Y.append(None)
        else:
            i = 0
            while x[i] < find_x:
                i += 1  
            Y.append(
                y[i-1] + (y[i] - y[i-1]) / (x[i] - x[i-1]) * (find_x - x[i-1])
            )    
    return Y

def newton_polynomial(x: list, y: list, h: float, X):
    '''
    x -> list of x arguments
    y -> list size of x list and have values of your f(x)
    h -> step of newton function
    X -> list of x arguments you found the y
    returns: list of Y values

    http://miest.narod.ru/iissvit/rass/vip16.htm
    '''

x = list(range(0,100))
y = list(map(math.sin, x))
X = [0.74, 3, 66, 98.3, 103]
print(linear_interpolation(x, y, X))

X = [0.74, 3, 66, 98.3]
# deleting over-range value
f = interp1d(x, y)
print(f(X))

'''
[0.6226885287578434, 0.14112000805986724, -0.026551154023966794, -0.701129360649201, None]
[ 0.62268853  0.14112001 -0.02655115 -0.70112936]
'''