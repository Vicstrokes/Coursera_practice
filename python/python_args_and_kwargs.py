def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(2,5,7,9))


def sum_of1(**kwargs):
    sum1 = 0
    for value in kwargs.values():
        sum1 += value
    return round(sum1,2)
print (sum_of1(coffee = 2.99, cake = 4.55, milk = 5.998))