# Anton Franzen 2021

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2, 4, -3])
v2 = np.array([0, -3, -3])

# Let se what the angle is between those 2 vectors in 3 dimensional space and plot it.

ang = np.arccos( np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)))
print(ang)

#Lets plot them

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], 'b')
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], 'r')

plt.axis((-6, 6, -6, 6))
plt.title(f'Angle between those vectors are: {ang} radians')
plt.show()