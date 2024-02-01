# def divide_by(a,b):
#     return a/b
# try:
# ans = divide_by(40,0.5)
# #to give the kind of error that occured you include "Exception as e"
#     print(ans)
# except ZeroDivisionError as e:
#     print("we can not divide by zero: ", e)
#     print(e.__class__)
# except Exception as e: 
#     print("something went wrong!", e)
#     # To print the class of error recieved we use "e.__class__"
#     print(e.__class__)


# Starter code
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')  

ans = divide_by(40, 0)
print(ans)




