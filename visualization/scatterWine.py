# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt

wine = pd.read_csv('wine.csv')

plt.scatter(wine['AGST'], wine['Price'])
plt.title("Price vs. Average Growing Season Temp of Bordeaux wine bottles")
plt.xlabel("AGST (Celsius)")
plt.ylabel("Log of Price")
plt.grid(True)
plt.show()

plt.scatter(wine['WinterRain'], wine['Price'], color='black', label='Winter')
plt.scatter(wine['HarvestRain'], wine['Price'], color='red', label='Harvest')
plt.title("Price vs. Rain of Bordeaux wine bottles")
plt.xlabel("Rain (mm)")
plt.ylabel("Log of Price")
plt.legend(loc='upper center')
plt.grid(True)
plt.show()

plt.subplot(211, axisbg="yellow")  # equivalent to: plt.subplot(2, 2, 1)
plt.scatter(wine['Age'], wine['Price'])
plt.title("Price vs. Age of Bordeaux wine bottles")
plt.xlabel("Age in years")
plt.ylabel("Log of Price")
plt.show()

plt.subplot(212, axisbg="cyan")
plt.scatter(wine['FrancePop'], wine['Price'])
plt.title("Price of Bordeaux wine bottles vs. Population")
plt.xlabel("France population (Thousands)")
plt.ylabel("Log of Price")
plt.show()
