string = str(input("Enter a string : "))
space = 0
words = 0
words = string.split()
space = len(words) - 1
words2 = 0
for i in range(0 , len(words)):
    words2 += len(words[i])
print("The number of characters in your string (including space) is : ", space + words2)
print("The number of characters in your string (excluding space) is : ", words2)