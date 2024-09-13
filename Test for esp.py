 
final = input("Do you want to see the exchange rate for a specific day? Yes or No. \n").capitalize() 

if final == 'Yes':    
    date_spec = input("Please enter the date you would like to see the exchange rate for: ")
    
df = pd.read_csv("Task4a_data.csv")
df.loc[date_spec]

x=df['Date']
y=df[currency]
plt.xlabel('currency')
plt.ylabel('Exchange rate')  
plt.bar(x,y)
plt.plot(x,y)
            
plt.show()