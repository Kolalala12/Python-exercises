#05,06. Calculate Mean, Median, and Mode with time calculator

import statistics
from time import time

start = time()
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)
end = time ()

execution_time = end - start
print(mean, median, mode)
print(execution_time)
