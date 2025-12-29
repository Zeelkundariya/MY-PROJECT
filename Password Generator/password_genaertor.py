import random

upper = int(input("Enter number of uppercase alphabets you want to add: "))
lower = int(input("Enter number of lowercase alphabets you want to add: "))
digits = int(input("Enter number of digits you want to add: "))
symbols = int(input("Enter number of symbols you want to add: "))

pas = []
low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym = "!@#$%^&*()~<>?/|\\{}[]"  # Added escape character for backslash

for i in range(upper):
    pas.append(random.choice(up))
    
for i in range(lower):
    pas.append(random.choice(low))
    
for i in range(symbols):
    pas.append(random.choice(sym))
    
for i in range(digits):
    pas.append(str(random.randint(0, 9)))

random.shuffle(pas)
password = "".join(pas)

print("Your Generated Password is:", password)