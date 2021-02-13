# This is a sample Python script.


import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
#import numpy as np


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def printPolynom(a,b,c,delta_t,n):
    x=[]
    y_our=[]
    y_real=[]
    f_d2=c
    f_d1=a*(delta_t)**2+b*(delta_t)
    delta_1=2*a*(delta_t)**2
    for i in range(n):
        f_d1 += delta_1
        f_d2 += f_d1
        x.append(i*delta_t)
        y_our.append(f_d2)
        y_real.append(a*(x[-1])**2+b*(x[-1])+c)
    plt.plot(x, y_our, '-ok',label='our')
    plt.plot(x, y_real, '-or',label='real')
    plt.legend()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printPolynom(1,2,1,5,10)
    print_hi('PyCharm')


