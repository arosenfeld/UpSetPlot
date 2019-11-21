"""
====================
Vertical orientation
====================

This illustrates the effect of orientation='vertical'.
"""

from matplotlib import pyplot as plt
from upsetplot import generate_counts, plot

example = generate_counts()
plot(example, orientation='vertical')
plt.suptitle('A vertical plot')
plt.show()

plot(example, orientation='vertical', show_counts=True)
plt.suptitle('A vertical plot with counts shown')
plt.show()
