import pandas as pd
import matplotlib.pyplot as plt

#The menu() function generates the UI the accepts and validates user choice
def menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. Pound Sterling (GBP) to US Dollar (USD)")
        print("8. US Dollar (USD) to Pound Sterling (GBP)")
        print("")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 8:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GBP',
       '7': 'GBP - USD',
       '8': 'USD - GBP'}
   
    currency = currencies.get(menu_choice)
    
    return currency


menu_choice = menu()
currency = get_currency()


#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate

conversion_rate = get_conversion_rate()


#Accepts and validates user input for teh amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the ammount you wish to convert")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  

conversion_amount = float(get_amount_to_convert())

#Performs the converison and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))
    
perfom_conversion() 

df = pd.read_csv("Task4a_data.csv")


start_graph = input("Do you want to see a graph of how the exchange rate changed over time? Yes or No. \n").capitalize()

if start_graph == 'Yes':
    if menu_choice == '1':
    
    #Line Graph
        x=df['Date']
        y=df['GBP - EUR']
        
        plt.xlabel('Date')
        plt.ylabel('GBP exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=7.5 ) 
        plt.tight_layout()
        plt.xticks(rotation = 60) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
        
        plt.show()
        

    elif menu_choice == '2':    
        #Line Graph
        x=df['Date']
        y=df['EUR - GBP']

        plt.xlabel('Date')
        plt.ylabel('EUR exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.800
        
        plt.show()
    
    elif menu_choice == '3':        
        #Line Graph
        x=df['Date']
        y=df['GBP - AUD']

        plt.xlabel('Date')
        plt.ylabel('GDP exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
        
        plt.show()
        
    elif menu_choice == '4':
        #Line Graph
        x=df['Date']
        y=df['AUD - GBP']

        plt.xlabel('Date')
        plt.ylabel('AUD exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
        plt.show()
        
        plt.show()
        
    elif menu_choice == '5':
        #Line Graph
        x=df['Date']
        y=df['GPB - JPY']

        plt.xlabel('Date')
        plt.ylabel('GDP exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
        plt.show()
        
       
        
    elif menu_choice == '6':        
        #Line Graph
        x=df['Date']
        y=df['JPY - GBP']

        plt.xlabel('Date')
        plt.ylabel('JPY exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
        plt.show()
        
        
    elif menu_choice == '7':        
        #Line Graph
        x=df['Date']
        y=df['GBP - USD']

        plt.xlabel('Date')
        plt.ylabel('GBP exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
        plt.show()
        

    elif menu_choice == '8':        
        #Line Graph
        x=df['Date']
        y=df['USD - GBP']

        plt.xlabel('Date')
        plt.ylabel('USD exchange rate') 
        plt.scatter(x,y)
        plt.plot(x,y)
        
        plt.rcParams["figure.figsize"] = [500, 500]
        
        plt.tick_params(axis='x', which='major', labelsize=8 )  
        plt.tight_layout()
        plt.xticks(rotation = 90) # 40 is the rotation angle
        spacing = 0.100
        fig = plt.figure
        plt.subplots_adjust(bottom=spacing)
        spacing = 0.300
                
        plt.show()
        
if start_graph == 'No':
    print("Thankyou, have a nice day.")