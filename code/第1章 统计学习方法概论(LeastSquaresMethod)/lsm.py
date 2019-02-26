
import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

# 目标函数 y=sin2x 
def real_func(x):
    """
    sin(2πx)
    """
    return np.sin(2*np.pi*x)

def fit_func(p: list, x):
    """
    ps: numpy.poly1d([1,2,3]) 生成  1x2+2x1+3x0
    one-dimensional polynomial 多项式
    """
    f = np.poly1d(p)
    return f(x)

# 残差
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret