import random

#imported the random module from python library

print("Welcome to Password Generator\n")

#p1 contains the alphabets of both upper case and lower case
p1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#p2 contains the special characters

p2="!@#$%^&*()_-+?/\ "

#p3 contains the numbers

p3="1234567890"

length_password=int(input("Enter the length of the password : "))

#Taking length of password as input

if length_password>=12:
    """checking the condition for the length of the password
        combining the random passwords generated"""
    a="".join(random.sample(p1,length_password-4))+"".join(random.sample(p2,2))+"".join(random.sample(p3,2))

    #printing the result if the condition goes True

    print("\nYour Password is : ",a)

else:
    #Else condition if the condition goes False 

    print("\nPlease Enter the length of the password  greater than 12" )

    #Printing the else condition