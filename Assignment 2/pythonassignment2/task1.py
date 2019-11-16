sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
per=(sub1+sub2+sub3+sub4+sub4)/(500)*100
if(per>=90):
    print("Grade: A")
elif(per>=80&per<90):
    print("Grade: B")
elif(per>=70&per<80):
    print("Grade: C")
elif(per>=60&per<70):
    print("Grade: D")
else:
    print("Grade: F")
