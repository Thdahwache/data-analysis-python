import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
  lin_reg = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  years = np.arange(1880,2051,1)
  line1 = lin_reg.intercept + lin_reg.slope * years
    
  plt.plot(years, line1)

    # Create second line of best fit
  
  df_last = df[df['Year']>=2000]
  lin_reg_2000 = linregress(df_last['Year'], df_last['CSIRO Adjusted Sea Level'])
  years = np.arange(2000,2051,1)
  line2 = lin_reg_2000.intercept + lin_reg_2000.slope * years
  
    # Add labels and title
  plt.plot(years, line2)
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()