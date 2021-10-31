import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(-6, 6, 1000)

    plt.figure()
    l1 = plt.plot(x, 1 / (1 + np.exp(-x)), label='Logistic')
    #plt.xlabel('$x$')
    #plt.ylabel('$\exp(x)$')

    #plt.figure()
    l2 = plt.plot(x, 
    (np.exp(x)-np.exp(-x)) / (np.exp(x)+np.exp(-x)),
    linestyle='--', label='Tanh')
    #plt.xlabel('$x$')
    #plt.ylabel('$-\exp(-x)$')
    #设置坐标轴范围
    plt.xlim((-6, 6))
    plt.ylim((-1, 1))
    #设置坐标轴名称
    plt.xlabel('x')
    plt.ylabel('y')
    #设置坐标轴刻度
    my_x_ticks = np.arange(-6, 8, 2)
    my_y_ticks = np.arange(-1, 1.5, 0.5)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    #设置坐标轴位置
    ax=plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))

    plt.legend()   #设置图例

    plt.show()

if __name__ == '__main__':
    main()