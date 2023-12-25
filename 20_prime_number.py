def prime_number(number):
    flag=False
    for i in range(2,number):
        if number%i==0:
            print("The number is non - prime")
            break
        

    if flag == "True":
        print("Number is non-prime")
    else:
        print("Number is prime ")    


number = int(input("Enter the number"))     

prime_number(number)