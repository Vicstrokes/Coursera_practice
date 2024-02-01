bill_total = 1000
discount1 = 0.1
discount2 = 0.2
country = 'Biafra'

amount = int(input('How much are paying?  ' ))
question1 = input('which country are you from: ')

if amount >= bill_total and country == question1:
    print(f"Bill is either 1000 or above and is qualified for 20% discount. Amount paid is: "  + str(amount) +"  and the country is : " + str(question1))
    amount = amount - (amount * discount2)

elif amount >= 800 and country == question1:
    print(f"This individual is qualified for 10%. Amount paid is: "  + str(amount) +"  and the country is : " + str(question1))
    amount = amount - (amount * discount1)

elif amount >= bill_total and country != question1:
    print(f"Bill is either 1000 or above and is qualified for 10% discount. Amount paid is: "  + str(amount) +"  and the country is : " + str(question1))
    amount = amount - (amount * discount1)

else :
    print(f"This individual is not qualified for any discount. Amount paid is: " + str(amount) +"  and the country is : " + str(question1))
print (f"Total bill: " + str(amount))