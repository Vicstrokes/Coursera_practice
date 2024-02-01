# bill = 175.00

# tax_rate = 15

# total_tax = (bill * tax_rate) /100.00

# print ('Total tax: ', total_tax)

def calculate_tax (amount, tax):
    return round((amount * tax) / 100.00, 2)
print('Total tax: ', calculate_tax(5000.00 , 20))