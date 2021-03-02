# -*- coding:utf-8 -*-

# 15-1 立方

import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c='green', edgecolors='none', s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Cubic of Value", fontsize=24)

plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
# plt.axis([0, 6, 0, 150])

plt.show()
# plt.savefig('squares_plt.png', bbox_inches='tight')