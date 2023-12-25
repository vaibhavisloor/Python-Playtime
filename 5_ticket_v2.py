height = int(input("Enter your height in cm :"))
age = int(input("Enter your age in years :"))

if(age >= 18):
    if(height >= 120):
        print("You are eligible for the ride")
    else:
        print("You are'nt eligible because you dont meet minimum height requirement ")
else:
    print("You are'nt eliglible becuase you dont meet minimum age requirements")      

if(age > 0 and age<=10 ):
    print("Your ticket cost is $5")
elif (age >10 and age < 18 ):
    print("Your ticket cost is $10")    
elif(age>=18 and age<=100):
    print("Your ticket cost is $15")
else:
    print("Enter valid age")    