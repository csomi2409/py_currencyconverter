import time                         

currency = {                        #dictionary for the currency pairs and their conversion rates
    "GBPEUR": 1.13,                 #The GBPEUR pair has a conversion rate (value) of 1.13
    "EURGBP": 0.88,
    "EURHUF": 375,
    "HUFEUR": 0.0026,
    "GBPUSD": 1.25,
    "USDGBP": 0.8,
    "GBPHUF": 426,
    "HUFGBP": 0.0023,
    "HUFUSD": 0.0029,
    "USDHUF": 339,
    "EURUSD": 1.10,
    "USDEUR": 0.90
}

#Asking the user which currency they would like to convert to and from what
first_currency = input("Please input the currency you want to convert:\n(USD,EUR,GBP,HUF)\n>>> ").upper()
second_currency = input("\nPlease input the currency you want to convert into:\n(USD,EUR,GBP,HUF)\n>>> ").upper()
#Add them together so they are the same as the dictionary keys
pair = (first_currency+second_currency)

for i in currency:                          #Go over each key
    if pair == i:                           #if user_input == dictionary_key
        print("You've chosen:", pair)       
        print("The conversion rate is:", currency[pair])
#Ask the amount they would like to convert
amount = float(input("\nPlease input the amount you want to convert: "))
#Do the math
conversion = (amount * currency[pair])

print("\ncalculating...")
time.sleep(1)                               #Acting like big thinking
print("\nTotal amount: ", conversion,second_currency)   #Display final result 
