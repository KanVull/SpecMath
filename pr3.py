import numpy
from scipy import stats
import matplotlib.pyplot as plt
random_values = numpy.random.normal(0, 0.1, 1000)
average = numpy.average(random_values)
std = numpy.std(random_values)
median = numpy.median(random_values)
mode = stats.mode(random_values)[0]
plt.hist(random_values)
plt.show()
print(f'Average {average}')
print(f'STD {std}')
print(f'Median {median}')
print(f'Mode {mode}')