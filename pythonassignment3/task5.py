#5Write a program to identify duplicate values from list 
l =[1,2,2,6,6,"jaffar","gamaportal8@gmail.com"]

for x in l:
    if l.count(x) > 1:
        print(x)

print("---------------------------------------------\n")