import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return a + b/x

x = np.array(range(1, 200))
y = 3/x + 5
n = len(x)
s=sum(y)
s1 = np.sum(1 / x)  #  1/x
s2 = np.sum((1 / x) ** 2) #  (1/x)**2
s3 = np.sum(y / x)  # y/x                   
a = round((s*s2-s1*s3)/(n*s2-s1**2),3)
b = round((n*s3-s1*s)/(n*s2-s1**2),3)

X = list(range(1, 100, 10))
Y = list(map(f, X))

plt.plot(x,y,'-r',X,Y,'o')
plt.show()

