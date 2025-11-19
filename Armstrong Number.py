given_number = int(input("Enter a number to check if it's armstrong or not : ")) #1634
str_number = str(given_number)
lists = []
length = len(str_number) #4
for i in range (0,length):
    digit = str_number[i]
    digit = int(digit)
    digit = digit**length
    lists.append(digit)
if(sum(lists) == given_number):
    print("Your number is an Armstrong Number")
else:
    print("Your number is not an Armstrong Number")
