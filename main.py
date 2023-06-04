import datetime

current_date = datetime.datetime.now()

current_year = current_date.year

print("Recipient's name")
r_name = input()
print("Year of birth")
yob = int(input())
print("Your special message")
msg = input()
print("your name")
y_name = input()

age = current_year - yob

card = f"\n{r_name}，let's celebrate your {age} years of awesomeness!\nWishing you a day filled with joy and laughter as you turn {age}\n\n{msg}\n\nWith love and best wishes,\n{y_name}"

print(card)