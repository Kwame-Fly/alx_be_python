#Age calculator

#Prompt the user for current age
current_age = int (input ("How old are you?"))
#Assume the current year is 2023
current_year = 2023
#Assume the future age is 2050
future_year = 2050
years_to_add = future_year - current_year
future_age = current_age + years_to_add
#Print result of future age
print (f"In 2050, you will be {future_age} years old")

