import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [101,24,78,23,90]
tick_label1=['a','b','c','d','e']
plt.bar(x,y,tick_label=tick_label1, color='red', width=0.6)
plt.xlabel('x - axis bar graph')
plt.ylabel('y - axis bar graph')
plt.title(" bar graph testing")
plt.show()



import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [6,2,0,9]
q=[0,3,4]
w=[3,4,0]
plt.subplot(3,1,1)
plt.plot(x,y)
plt.subplot(3,1,2)
plt.plot(q,w)
plt.subplot(3,1,3)
plt.plot(x,y)
plt.show()
