# creating a leap year code
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap

year = int(input("Enter a year: "))
print(is_leap(year))
