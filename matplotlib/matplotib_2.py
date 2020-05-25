import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
fig=plt.figure(figsize=(6,6))
axl=fig.add_subplot(4,3,1)
ax2=fig.add_subplot(4,3,2)
ax3=fig.add_subplot(4,3,3)
axl.plot(np.random.randint(1,5,5),np.arange(5))
ax2.plot(np.arange(10),np.arange(10))
plt.show()
print('____________________________')
