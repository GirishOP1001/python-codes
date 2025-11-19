a = input("Enter a string: ")
vow = 0
cons = 0

for ch in a:
    if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
        vow += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        cons += 1

print("Vowels:", vow)
print("Consonants:", cons)