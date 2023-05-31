print("Recipient's name")
r_name = input()
print("Year of birth")
yob = int(input())
print("Your special message")
msg = input()
print("your name")
y_name = input()

age = 2023 - yob

card = f"{r_name}，let's celebrate your {age} years of awesomeness!\nishing you a day filled with joy and laughter as you turn {age}\n\n{msg}\n\nWith love and best wishes,\n{y_name}"

print(card)