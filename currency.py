value = input('How much money would you like to withdraw today?')
decimized_value = float(value)
hundred_division = decimized_value//100
hundered_remainder = round(decimized_value%100,2)

if(hundered_remainder > 50):
    fifty_value=hundered_remainder//50

print(hundred_division, hundered_remainder)
