menu = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano','Decaf', 'mocha', 'Cortado']

def find_coffee(coffee):
    if coffee[0] ==  'C':
        return coffee
  
# Example 1 using the map function
# map_coffee = map(find_coffee, menu)
# print(map_coffee)

# for each_coffee in map_coffee:
#     print(each_coffee)

# Using the filter function

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for each_coffee_filtered in filter_coffee:
    print(each_coffee_filtered)

else:
     "Did not start with the letter C"