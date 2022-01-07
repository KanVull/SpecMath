import math
from scipy.interpolate import lagrange
from scipy.interpolate.interpolate import interp1d

def linear_interpolation(x: list, y: list, X: list):
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

def lagrange_interpolation(x: list, y: list, X: list):
    '''
    x -> list of x arguments
    y -> list size of x list and have values of your f(x)
    X -> list of x arguments you found the y
    returns: list of Y values
    '''
    Y = list()
    for _x in X:
        up = 1
        down = 1
        answer = 0
        for i in range(len(x)):
            up = 1
            down = 1
            for j in range(len(x)):
                if i == j:
                    continue
                up *= _x - x[j]
                down *= x[i] - x[j]
            answer += y[i] * (up/down)
        Y.append(answer)        
    return Y

def newton_interpolation(x: list, y: list, X: list, h=0.05):
    '''
    x -> list of x arguments
    y -> list size of x list and have values of your f(x)
    h -> step of newton function
    X -> list of x arguments you found the y
    returns: list of Y values

    http://miest.narod.ru/iissvit/rass/vip16.htm
    '''
    n = 0
    # расчитываем табличные значения изменения y
    delta_y = {0: y.copy()}
    while True:
        n += 1
        del_y = delta_y[n-1]
        delta_y[n] = [del_y[i-1] - del_y[i] for i in range(1, len(del_y))]
        con = False
        for counted_y in delta_y[n]:
            if abs(counted_y) > h:
                con = True
        if not con:
            break
    Y = list()
    for _x in X:
        P = 0
        for i in range(n+1):
            answer = delta_y[i][0] 
            if i>0:
                q = (_x - x[0]) / h 
                up = 1
                for z in range(i):
                    up *= q - z
                answer *= up/math.factorial(i)
            P += answer
        Y.append(P)
    return Y             
    

x = list(range(0,100))
y = list(map(math.sin, x))
X = [0.74, 3, 66, 98.3]
print(linear_interpolation(x, y, X))

f = interp1d(x, y)
print(f(X))
'''
[0.6226885287578434, 0.14112000805986724, -0.026551154023966794, -0.701129360649201, None]
[ 0.62268853  0.14112001 -0.02655115 -0.70112936]
'''

x = list([3.1, 3.6, 3.9, 4.5])
y = list([5.3711, 14.5359, 22.0989, 42.6251])
X = [3.6, 4, 4.4, 5]
print(lagrange_interpolation(x, y, X))

f = lagrange(x, y)
print(f(X))
'''
[14.5359, 24.99991666666667, 38.664051851851866, 66.00039907407402]
[14.5359     24.99991667 38.66405185 66.00039907]
'''
