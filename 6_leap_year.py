year = int(input("Enter the year "))

if(year%4==0 or year%400==0):
    print("It is a leap year");
else:
    print("It is not a leap year");

#If the year is divisble by 100 then it should be divisible 400 to be 