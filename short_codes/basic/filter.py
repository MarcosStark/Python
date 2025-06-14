list1 = [10, 15, 18, 20, 30, 45]

#Sem lambda
def double(x):
    return x >= 20

result1 = filter(double, list1)
print(list(result1))

#Com lambda
print(list(filter(lambda x: x >= 20, list1)))