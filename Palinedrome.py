given_number = int(input("Enter a number to check if it's palindrome or not : "))
str_number = str(given_number)
if(str_number == str_number[::-1]):
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")