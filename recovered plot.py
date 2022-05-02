# -*- coding: utf-8 -*-
"""
Created on Tue May  3 00:31:53 2022

@author: 李子安  Russel
"""

def recovered_plot():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    dB = pd.read_csv('./data.csv', sep = ',')

    S = dB['recovered(R)']
    S = np.array(S)

    plt.plot(S)
    plt.xlabel('t')
    plt.title('Recovered(R)')
    plt.show()

recovered_plot()