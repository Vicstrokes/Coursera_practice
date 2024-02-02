coffee = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano','Decaf']

# print(sorted(coffee))

# def reverse(str):
#     return str[:: -1]

# reversed_coffee = map(reverse, coffee)

# for item in reversed_coffee:
#     print(item)

global_list = [1,2,3,]

# def add_to(item):
#     return global_list.append(item)
# add_to(5)
# print(global_list)

def add_to_list(list, item):
    new_list = list.copy()
    new_list.append(item)
    return new_list

new_list_added = add_to_list(global_list, 4)
print(global_list)
print(new_list_added)
