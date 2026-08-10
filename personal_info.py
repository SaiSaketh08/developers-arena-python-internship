# Personal Information Manager
# Week 1 Python Internship Project
# The Developers Arena

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store personal information
name = "Sai Saketh"
age = 17
city = "Hyderabad"
hobby = "Cricket"

# Get information from the user
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What is your favorite food? ")

while favorite_food.strip() == "":
    print("Please enter a valid food!")
    favorite_food = input("What is your favorite food? ")

favorite_color = input("What is your favorite color? ")

while favorite_color.strip() == "":
    print("Please enter a valid color!")
    favorite_color = input("What is your favorite color? ")
# Calculate age in months
age_in_months = age * 12

# Display information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

# Goodbye message
print()
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)