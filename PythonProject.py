from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
date = now.strftime("%d")

byear = int(input("enter the birth year"))
bmonth = int(input("enter the birth month in number"))
bdate = int(input("enter the birth date in number"))
year = int(year)
month = int(month)
date = int(date)
if byear<year:
    if bmonth<month:
        if bdate>date:
            x = year - byear 
            y = month - bmonth            
            z = bdate - date
            print(f"your age is {x} and {y} and {z} days")
        else:
            x = (year - byear) - 1
            y = 12 - (month - bmonth)
            z = 31 - (bdate + date)
            print(f"your age is {x} and {y} and {z} days")
    else:
        print("check your birth year once again")