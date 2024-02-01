"""1.   Under the num_list create a new for loop and print out each value on the list in sequential order.

2.  Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition

3.  Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.

4.  Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number

5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.

6.  Inside the for loop increment the counter by 1.

7.  Add a print statement outside the for loop to print the value of the count variable.

8.  Finally, add a break statement directly after the print statement inside the if condition for finding the number.  """



# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# for i in list1:
#     for j in list2:
#         print(str(i) +" " + str(j))


num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# for idx, num in enumerate(num_list):
#     if num > 45:
#         print(f'over 45',idx, num)
#     else:
#         print(f'under 45')


# for idx, num in enumerate(num_list):
    # if num == 36:
        # print(f'number at index: ',idx)
        # break
    # else:
        # print(f'under 45')


# count = 0
# for count in range(100):
#     if count < 50:
#         count += 1
#         print(count)
#         break
    
# count = 0

# for x,num in enumerate(num_list):
#     count += 1
#     if num == 36:
#         print('Number found at ', x)
#         break

# print(count)

a = isinstance(1,str)

print(a) 