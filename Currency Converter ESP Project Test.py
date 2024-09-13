import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('task4a_data.csv')

#print(df.loc[:,'Area'])  # select data based on titles ['rows', 'columns']
#print(df.iloc[;0]) # select data based on tindex number in CSV

choice = input("Would you like to see a graph on how your selected currency changed over time? Yes or No. \n")

if choice == 'Yes':
        
        #Line Graph
        x=df['Date']
        y=df['GBP - EUR']

        plt.xlabel('Date')
        plt.ylabel('Currency exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.show()

