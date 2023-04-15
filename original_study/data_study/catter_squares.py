import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family='Microsoft YaHei')

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置表格的平方数。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize= 14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围。
ax.axis([0, 1100, 0, 110000])

plt.savefig('squares_plot.png', bbox_inches='tight')