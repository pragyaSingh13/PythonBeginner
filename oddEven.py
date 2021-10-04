from datetime import datetime
print("Department of Enviornmental safety")
vehiclenum = int(input("Please enter you vehicle number: "))

datestr = input("Enter the desired date as d/m/y: ")
date_date = datetime.strptime(datestr,'%d/%m/%Y')

day = int(datestr[0:2])

print("---------------------------------")

if day<1 and day>31:
    print("Invalid date")

if vehiclenum%2==0:
    if day>0 and day<16:
        print("You can take your car on ",date_date)
    else:
        print("Sorry, you're not eligible yet")
else:
    if day>=16 and day<=31:
        print("You can take your car on ",date_date)
    else:
        print("Sorry, you're not eligible yet")

    

    


