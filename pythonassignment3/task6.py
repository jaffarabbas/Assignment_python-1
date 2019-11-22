#6Write a Python script to check if a given key already exists in a dictionary
keys = input("Enter Any key for check duplicate values ")
disa = {"value1" : "" , "value2" :""}
for key,values in disa.items():
    if key in keys:
        print("------------------------------------\n")
        print("KEY IS ALREADY AVAILABLE", disa)