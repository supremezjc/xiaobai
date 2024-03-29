import matplotlib.pyplot as plt
from randomwalk_ import RandWalk
while True:
    rw = RandWalk()
    rw.fill_walk()
    # 设置绘图窗口大小
    plt.figure(num=1, figsize=(10, 6), edgecolor='green', frameon=False)
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    # 突出起点和终点
    plt.scatter(0, 0,c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk？(y/n):")
    if keep_running == 'n':
        break