#!/usr/bin/python
#!/usr/bin/env python
# matix.py
from PIL.Image import linear_gradient
import numpy as np  # need "np." as prefix
#import matplotlib.pyplot as plt

def tanh(x):
    #print("x:", x)
    return (np.exp(x)-np.exp(-x)) / (np.exp(x)+np.exp(-x))

def non_linear(x):
    print(x)
    #plt.figure()
    #plt.plot(x, (np.exp(x)-np.exp(-x)) / (np.exp(x)+np.exp(-x)))
    #plt.show()
    print("y:")
    for i in x:
        print(tanh(i))

def example():
    M = np.mat([[3, 4, 9, 5],
                [0, -1, 10, -5],
                [2, 7, 0, 6]])
    print("M = \n", M)
    N = np.mat([[1, 2],
                [1, 3],
                [-2, 4],
                [5, 9]])
    print("N = \n", N)
    print("matrix: M * N = \n", M * N)
    print("matrix: 2 * N = \n", 2 * N)
    print("matrix: M + M = \n", M + M)
    print("matrix: N.T = \n", N.T)
    print("matrix: N.I = \n", N.I)

#my
def foo():
    np.set_printoptions(precision=2)
    M1 = np.array([[0.1, 0, 0.2, 0.4, 0.2, 0.1, 0, 0.3],
    [0.5, 0.4, 0.2, 0, 0.2, 0.6, 0, 0.2]], float)
    print("M1 = \n", M1)
    #print("M1 = \n", M1.T)
    M2 = np.array([[0.2, 0.1],
    [0.1, 0.3],
    [0.4,0.2],
    [0.5,0.4],
    [0.3,0.2]])
    print("M2\n", M2)
    x = np.array([0.2, 0.1, 0.1, 0.3, 0.4, 0.2, 0.5, 0.4])
    print("x = \n", x)
    sh1 = x.shape
    print("sh1 = ", sh1)
    Mx = np.zeros((M1.shape[0], x.shape[0]))
    Mx = np.dot(M1 ,x)
    print("Mx = \n", Mx)

    #h = tanh(M1 * x.T)
    h = np.array([[0.1] ,[0.3]])
    print("h = \n", h)
    print("M2 * h = \n", np.dot(M2 , h))

def main():
    #A = np.mat([0.3, 0.8])
    #print(tanh(0.3))
    #print(tanh(0.8))
    #print(tanh(A))
    foo()

if __name__ == '__main__':
    main()
