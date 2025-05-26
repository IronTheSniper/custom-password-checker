# Custom Password Checker Solo Project
# Strong password: Ironman49!
# Medium password: iroman49
# Weak password: ironman

# Password rating 
score = 0

print("Custom Password Checker\n")

# Ask the user to input password
print("Ensure your password meets these requirements:\n\n"
        " - 8 or more characters.\n"
        " - Atleast 1 capital letter.\n"
        " - Atleast 1 special character.\n"
        " - Atleast 1-2 numbers.\n")
password = input("Enter Password: ")

# Uppercase check 
first_letter = password[0]
if first_letter == first_letter.upper() and first_letter != first_letter.lower():
    score +=1
        
# Lowercase check 
for char in password:
    if char == char.lower() and char != char.upper():
        score += 1
        break 

# Charcater length check
if len(password) >= 8:
    score +=1 

# Special charcater check
special_char = ["!", "@", "#", "$", "%", "^", "&",]
for char in special_char:
    if char in password:
        score += 1
        break

# Number check
for char in password:
    if char.isdigit():
        score += 1
        break

# Provide Feedback
if score <= 2:
     print("Weak password.")
elif score <= 4:
    print("Medium password.")
else:
    print("Strong password.")

