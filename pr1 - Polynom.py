from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

coef = [10, 5, 10]
polymonial = Polynomial(coef, domain=[-100, 100])
print(polymonial)
# 10.0 + 5.0 x**1 + 10.0 x**2

plt.plot(*polymonial.linspace())
plt.show()