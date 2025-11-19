a=int(input("Enter you Salary in INR: "))
print("Thank you very much! For confirmation, is your salary Rs",a," ?")
b=str(input("Type 'Yes' for confirmation: "))
if (b == 'Yes'):
    if(a<=10000):
        print("Congratulations! you just recieved a bonus of 10%")
        c=(a/10)
        print("Your total salary now is:",a+c)
    elif(a<=20000):
        print("Congratulations! you just recieved a bonus of 20%")
        d=(a/5)
        print("Your total salary now is:",a+d)
    elif(a>20000):
        print("Congratulations! You just recieved a bonus of 40%")
        e = a*2
        f=(e/5)
        print("Your total salary now is:",a+f)
elif(b=="no"):
    print("Thank you! Have a good day!")
else:
    print("oops! seems like you've made a mistake while spelling 'Yes'. Please run the code again!")