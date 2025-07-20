#Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold):")

if weather == "sunny":
    response = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    response = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    response = "Make sure to wear a warm coat and a scarf."
else :
    response = "Sorry, I don't have recommendations for this weather." 

#Output of response
print(response)
