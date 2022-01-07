from math import sin, cos
def derivative(function, x, step):
    return (function(x+step/2) - function(x-step/2)) / step

# sin' = cos
answer = cos(1)
print(answer)
print('Численный для шага 0.01', derivative(sin, 1, 0.01))
print('Численный для шага 0.001', derivative(sin, 1, 0.001)) 

'''
0.5403023058681398
Численный для шага 0.01 0.5403000546113423
Численный для шага 0.001 0.5403022833555537
'''