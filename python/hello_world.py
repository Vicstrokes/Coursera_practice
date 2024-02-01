# print('hello world')
# question = "Where do you live?"
# print(question)
# location = str(input())

# print("Thank you for the info: " + location)

def interview(Name, age):
    answer_this = "What is your name and age?"
    return interview(str(input(Name)), int(input(age)))
print(interview('victor', 32))
