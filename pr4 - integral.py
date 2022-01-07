def left_rectangles(function, x1, x2, n):
    h = (x2 - x1) / float(n)
    return sum([function(x1 + (i*h)) for i in range(n)]) * h

function = lambda x: x**2 + 2*x
# Интеграл этой функции на отрезке 4 - 10 = 396

print(left_rectangles(function, 4, 10, 20))
print(left_rectangles(function, 4, 10, 40)) 
print(left_rectangles(function, 4, 10, 1000)) 

'''
381.69
388.82249999999993
395.71203600000007
'''