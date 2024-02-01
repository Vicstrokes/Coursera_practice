# def find_num(num):
# # Linear Time Complexity
#     # count = 0 
#     # for x in range(100):
#     #     if x == num:
#     #         print('Total Iterations: ' , count)
#     #         return x
#     #     count += 1
# # find_num(97)


# # Using Binary Search to solve Linear Time Complexity
#     iteration = 0
#     x = range(100)
#     left = 0
#     right = len(x) - 1

#     while left <= right:
#         iteration += 1
#         middle = (left + right) // 2 
#         isNumber = x[middle]

#     if num == isNumber:
#         print("Iterations: ", iteration)
#         return middle
#     elif num < isNumber:
#         right = middle + 1
#     else:
#         left = middle + 1

#     return -1
    
# print(find_num(97))

def isPalidrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for characters in str:
        if str[startIndex] != str[endIndex]:
            return False
        else:
            return True
print(isPalidrome('pip'))      



def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci (n-2)
print(fibonacci(10))
    