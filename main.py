import math
from datetime import datetime, date

# TAPVT26D Veckouppgift check 20
print("--------------------------------------")
print("- Uppgift 2")
my_name = "Mats"
print(f"This program was made by {my_name}")

print("\n")
print("--------------------------------------")
print("- Uppgift 3")
ticket_price = 100  # ticket price
start_money = 200  # money to spend

print(f"Det blir {start_money - ticket_price} kronor över.")
remaining_money  = start_money - ticket_price / 2
print("Varje person får " + str(remaining_money))

print("\n")
print("--------------------------------------")
print("- Uppgift 4")
print("- 1a ------------------")
number_one = input("Please enter a number: ")
number_one = int(number_one)
print(f"The first number is {number_one}")

print("\n")
print("- 1b -------------------")
number_two = input("Please enter another number: ")
number_two = int(number_two)
numbers_sum = number_one + number_two # Add the two numbers
print(f"The numbers sum is {numbers_sum}")

print("\n")
print("- 2a -------------------")
jacket_price = 2000
sale_discount = 0.75
print(f"The jacket price after discount is {jacket_price - jacket_price * sale_discount} kronor.")

print("\n")
print("- 2b -------------------")
sales_discount = float(input("Please enter the discount in %: ")) / 100
item_price = int(input("Please enter the item price: "))
print(f"You have to pay {item_price * sales_discount} kronor.")


print("\n")
print("--------------------------------------")
print("- Uppgift 5")
print("- 1a -------------------")

distance_km = 470
vehicle_speed = int(input("In what average speed will you travel (km/h: "))
travel_time = distance_km / vehicle_speed # (t = s / v)
hours = round(travel_time // 1)
minutes = round(travel_time % 1 * 60)

print(f"The time to go to stockholm in {vehicle_speed} km/h is {hours} hours and {minutes} minutes.")

print("\n")
print("- 1b -------------------")
minutes = minutes + hours * 60
print(f"The time to go to stockholm in {vehicle_speed} km/h is {minutes} minutes.")

print("\n")
print("- 2 -------------------")

leg_one = int(input("Please enter length of leg 1: "))
leg_two = int(input("Please enter length of leg 2: "))

# Summan av katerterna i kvadrat = hypotenusan i kvadrat. Kvadratroten av hypotenusan i kvadrat ger dess längd
hypotenuse = math.sqrt(leg_one ** 2 + leg_two ** 2)

print(f"The hypotenuse is {hypotenuse}")

print("\n")
print("- 3a -------------------")
print(f"Date of today: {date.today()}")

print("\n")
print("- 3b -------------------")
seven_days_seconds = 24 * 60 * 60  * 7 # Hours Minutes Seconds * days
date_now  = datetime.now().timestamp()
date_in_7_days = datetime.fromtimestamp(date_now + seven_days_seconds).date()

print(f"Date in 7 days: {date_in_7_days}")