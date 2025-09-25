# Greet customers
print("Welcome to the DIY Tea & Juice Maker!")

# Get the base preference
base = int(input("What kind of base do you want? \
Please enter 1 for milk or 2 for fruit: "))

# Scenario when base preference is milk depending on lactose intolerance
if base == 1:
    lactose_intolerance = str(input("Do you have \
lactose intolerance? y for yes, n for no: "))
    if lactose_intolerance == "y":
        milk_preference = str(input("Do you want soy \
milk or oat milk? Please type in your choice [soy/oat]: "))
    else: 
        milk_preference = "regular"

# Scenario when base preference is fruit
if base == 2:
    fruit_preference = str(input("Which fruit do you want? \
Please type in your choice [mango/strawberry]: "))

# Get the tea type
tea_preference = str(input("From the following tea type:\n- No Tea\n- Black Tea\
\n- Green Tea\n- Matcha\nPlease choose a tea type: "))

# Terminating scenario in case of invalid tea choice
if base == 2 and tea_preference == "Matcha":
    print("Invalid choice! End of the program")
    
else:
    # Get the topping type
    topping_preference = str(input("From the following toppings:\n- No Topping\n- Bobas\
\n- Coconut Jelly\nPlease enter your choice for toppings: "))

    # Get desired drink size
    drink_size = str(input("Please enter your desired size of cup \
(Please enter s for small, m for medium, or l for large): "))

    # Set the drink size milimeters
    if drink_size == "s":
        mililiter_drink_size = 355
    elif drink_size == "m":
        mililiter_drink_size = 473
    else:
        mililiter_drink_size = 621

    # Get desired temperature for the drink
    desired_temperature = float(input("Please enter your desired \
temperature of your beverage (between 1 and 4 degrees): "))

    # Terminating scenario in case of invalid temperature choice
    if desired_temperature < 1.0 or desired_temperature > 10.0:
        print("Invalid choice! End of the program")
    else:
        # Manipulate the desired temperature for calculations
        if 1.0 <= desired_temperature <= 4.0:
            desired_temperature_final = desired_temperature
        elif 4.0 < desired_temperature <= 10.0:
            desired_temperature_final = 4.0

        # Set variables used for the equation
        cdrink = 4.184
        ΔTdrink = 25.0 - desired_temperature_final
        ΔTice = desired_temperature_final - 0.0
        hfusion = 334.0

        # Calculate the amount of ice required to bring the drink to desired temperature
        amount_ice = int(((1/5)*(mililiter_drink_size * cdrink * ΔTdrink)/(hfusion + cdrink * ΔTice)))

        # Display drink
        if base == 1:
            print("Your drink is a", milk_preference, "milk and"\
            , tea_preference, "with", topping_preference + ".")
        elif base == 2:
            print("Your drink is a", fruit_preference, "juice and"\
, tea_preference, "with", topping_preference + ".")

        # Display amount of ice needed to cooldown the drink_size
        print("The temperature of your beverage will be", desired_temperature_final\
,"Celcius degree after all", amount_ice, "ice cubes melted.")

        # Say farewell to the customers
        print("Have a nice day!")
