import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#calculate mean and variance
def mean(values):
    return sum(values)/ float(len(values))

#calculate the variance of a list of numbers
def variance(values,mean):
    return sum([(x-mean)**2 for x in values])

#calculate mean and variance
dataset=[[1,2],[2,3],[4,3],[3,2],[5,5]]
x=[row[0] for row in dataset]
y=[row[1] for row in dataset]
mean_x,mean_y =mean(x),mean(y)
var_x, var_y = variance(x,mean_x),variance(y, mean_y)
print('x stats: mean=%.3f variance= %.3f'%(mean_x, var_x))
print('x stats: mean=%.3f variance= %.3f'%(mean_y, var_y))
