# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:30:05 2022

@author: akhil
"""

""" importing the required libraries"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


"""reading the agricultural land data from csv file"""
agricultural_land_data = pd.read_csv('API_AG.LND.AGRI.ZS_DS2_en_csv_v2_4669757.csv',
                                     skiprows=[0, 1, 2, 3])

"""reading the forest land data from csv file"""
forest_area_data = pd.read_csv('API_AG.LND.FRST.ZS_DS2_en_csv_v2_4701080.csv',
                          skiprows=[0, 1, 2, 3])

"""reading the co2 emission  data from csv file"""

co2_emission_data = pd.read_csv('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_4701269.csv',
                                skiprows=[0,1,2,3])

X_values = range(1990, 2017)

world_agricultural_land = agricultural_land_data.iloc[259, 34:61]
world_forest_data = forest_area_data.iloc[259, 34:61]
world_co2_emission_data = co2_emission_data.iloc[259, 34:61]


"""converting the readed data into data frame"""
df = pd.DataFrame({'Agricultural land':world_agricultural_land,
                   'Forest land': world_forest_data,
                   'CO2 emission amount': world_co2_emission_data})
print(df)


"""displaying the plot for Agricultural land"""
plt.plot(X_values, world_agricultural_land)
plt.title('World agricultural land area from 1990 to 2019')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.show()

"""displaying the plot for world forest data"""
plt.plot(X_values, world_forest_data)
plt.title('World forest area from 1990 to 2019')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.show()

"""displaying the plot for world co2 emission data"""
plt.plot(X_values, world_co2_emission_data)
plt.title('World CO2 emission data from 1990 to 2019')
plt.xlabel('Year')
plt.ylabel('kilo tonnes')
plt.show()

print('The average percentage of worlds agricultural land is: ' + 
      str(np.mean(world_agricultural_land)))
print('The average percentage of worlds forest land is: ' + 
      str(np.mean(world_forest_data)))
print('The average amount of co2 emitted during this period is: ' +
      str(world_co2_emission_data))
corr1, pvalue = stats.pearsonr(world_co2_emission_data, world_forest_data)
print('The correlation between world forest area and CO2 emission is: ' + 
      str(corr1))
corr2, pvalue = stats.pearsonr(world_agricultural_land, world_co2_emission_data)
print('The correlation between world agricultural land and CO2 emission is: ' +
      str(corr2))