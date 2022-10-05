name = (input('Hello User, What is your name? >> '))
user_name = str(name)
if "George Fox" in user_name:
    print("Walk in the Light, wherever you may be, Walk in the Light, wherever you may be! In my old leather breeches and my shaggy, shaggy locks, I am walking in the glory of the Light, said Fox.")

else:
    print(user_name, "... that's a GREAT name! My name is Chatbot :)")

place = (input('Where are you from? >> '))
user_place = str(place)
print("I love", user_place, "so much! I've been there a few times and it's a great place.")

bot_number = 9
user_number = (input("What is your favorite number? >> "))

if float(user_number) > bot_number:
    print("Oh wow, mine's only", bot_number)

elif float(user_number) < bot_number:
    print("That's pretty small... mine's", bot_number)

else:
    print("That's MY favorite number! I think we'll be good friends.")

item = (input("What is your dream Item? >> "))
user_item = str(item)
print("Wow, I've always wanted a", user_item, "too!")
cost = (input(('How much does a', user_item, 'cost? >> ')))
p = float(cost)
number_years = (input("And how many years would you take a loan out to pay for it? >> "))
n = float(number_years)*12
annual_rate = input(('What would a reasonable yearly interest rate on', user_item, 'be? >> '))
r = float(annual_rate)/(100*12)

monthly_payment = (r * p) / (1 - (1 + r) ** (-n))
print(monthly_payment)

print("Well, it's been great chatting with you. Hope you come back soon!")