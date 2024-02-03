# # Example 1 to reverse strings
# original_list = [1, 2, 3, 4, 5]
# reversed_iterator = reversed(original_list)

# # Convert the reversed iterator to a list
# reversed_list = list(reversed_iterator)

# print(reversed_list)

# # Example 2
# original_list = [6, 7, 8, 9, 10]
# original_list.reverse()

# print(original_list)

# Example 3 using Slice Function
# trial = "Reversed strings"
# new_trial = trial[ :  : -1]
# print(new_trial)

# Example 4 Using Recurssion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
str = "reversal"
reverse = string_reverse(str)
print(reverse)