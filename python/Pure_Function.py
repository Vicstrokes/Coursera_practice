coffee = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano','Decaf']

# print(sorted(coffee))

# def reverse(str):
#     return str[:: -1]

# reversed_coffee = map(reverse, coffee)

# for item in reversed_coffee:
#     print(item)

global_list = [1,2,3,4]

def add_to(item):
    return global_list.append(item)
add_to(5)
print(global_list)