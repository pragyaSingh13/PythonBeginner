from datetime import datetime

def checkEligibility(date):
    date_date = datetime.strptime(date,'%d/%m/%Y')
    day = int(date[0:2])
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

checkEligibility(input("Enter the desired date as d/m/y: "))
