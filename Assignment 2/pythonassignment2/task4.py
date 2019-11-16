lst = []
num = int(input('Enter how many items in list: '))
for n in range(num):
    numbers = int(input('Enter cost of item '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))