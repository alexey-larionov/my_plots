import matplotlib.pyplot as plt

x=[1,2,3]
y=[3,4,7]

plt.plot(x,y,"r+", label="red")
plt.plot(y,x,"bo")
plt.legend()

plt.show()