from datetime import date

print("Enter your birth year?")
birth_year = int(input())

current_year = date.today().year

age = current_year - birth_year

print("You are", age, "years old.")