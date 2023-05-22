import matplotlib.pyplot as plt
import numpy as np
import random
from typing import List


random.seed(42)

colors: List[str] = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'] * 2
text: List[str] = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                   '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'] * 2

# random number generation (example)
inner_circle_size = np.array([random.random() / 10 for _ in range(len(colors))])
outer_circle_size = np.array([random.random() / 10 for _ in range(len(colors))])

n = len(inner_circle_size)
angle = np.arange(0, np.pi * 2, np.pi * 2 / n)
radius = 1 * np.ones(angle.shape)

x_circle = radius * np.cos(angle)
y_circle = radius * np.sin(angle)
x_len = len(x_circle)

fig = plt.figure(figsize=(6, 6))
# scatter plot circle
s_mul = 5000
font_size = 12
for idx in range(x_len):
    # S_i
    plt.scatter(x_circle[idx], y_circle[idx],
                color="white", alpha=1, edgecolors="none",
                s=(inner_circle_size[idx] * s_mul), marker='o', zorder=1)

    plt.scatter(x_circle[idx], y_circle[idx],
                color=colors[idx], alpha=0.5, edgecolors='none',
                s=(inner_circle_size[idx] * s_mul), marker='o', zorder=2)

    # S_T
    plt.scatter(x_circle[idx], y_circle[idx],
                facecolors='none', edgecolors='black',
                s=(outer_circle_size[idx] * s_mul), marker='o', zorder=2)

    # variable name
    if x_circle[idx] > 0:
        rotation_angle = angle[idx] * 180/np.pi
    else:
        rotation_angle = angle[idx] * 180/np.pi + 180

    mul = 1.6
    x_test = mul * radius[idx] * np.cos(angle[idx])
    y_test = mul * radius[idx] * np.sin(angle[idx])
    plt.text(x_test, y_test, text[idx],
             color=colors[idx], size=font_size,
             rotation=rotation_angle, rotation_mode='anchor',
             horizontalalignment='center', verticalalignment='center')

# line S_ij
# example - random line
sample_list: List[int] = [i + 1 for i in range(len(colors))]
for idx in range(len(sample_list)):
    i, j = random.sample(sample_list, 2)
    plt.plot([x_circle[i], x_circle[j]], [y_circle[i], y_circle[j]],
              linewidth=(random.random() * 5), color='k', alpha=0.3, zorder=0)

# figure setting
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.yticks(ticks=[])
plt.xticks(ticks=[])
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()
