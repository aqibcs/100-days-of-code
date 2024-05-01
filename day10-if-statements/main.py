# If-Else Statements:
# 1. Temperature Check:
temperature = 25
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not too hot today.")

# 2. Age Verification:
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")



# Elif Statements:
# 1. Grade Classification:
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 2. Time of Day Greeting:
hour = 15
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")


# Nested If Statements:
# 1. Ticket Pricing:
age = 25
if age >= 18:
    if age <= 25:
        print("Youth ticket price: $10")
    else:
        print("Adult ticket price: $15")
else:
    print("Child ticket price: $5")

# 2. Product Discounts:
product_price = 120
if product_price >= 100:
    if product_price < 150:
        print("10% discount applied.")
    else:
        print("20% discount applied.")
else:
    print("No discount available.")
