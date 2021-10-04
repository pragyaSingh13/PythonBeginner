age =int(input("Enter child's age "))

if age<5 and age>-1:
    print("Go to counter 1 for polio drops") 
elif age>=5 and age<10:
    print("Go to counter 2 for vaccine")
elif age>=10 and age<15:
    print("Go to counter 3 for vitamins")
else:
    print("No need of any dose")

