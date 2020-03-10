import matplotlib.pyplot as plt
from pylab import *
#中文支持
mpl.rcParams['font.sans-serif'] = ['SimHei']
#自定义数据
x= [0.749, 0.607, 0.411, 0.121,0.072]
y = [0.75, 0.80, 0.85, 0.90,0.95]
plt.plot(x, y, color="r", linestyle="-", marker="", linewidth=1.0,label='本文方法')
plt.legend()
plt.show()