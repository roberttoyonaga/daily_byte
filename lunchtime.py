def lunchtime(meal_items):
    balanced_meals = 0
    food_counter = 0
    drink_counter = 0 

    for item in meal_items:
        if item == "F":
            food_counter += 1
        elif item == "D":
            drink_counter += 1
        if food_counter == drink_counter:
            food_counter = 0 
            drink_counter = 0
            balanced_meals += 1

    return balanced_meals
    
print(lunchtime("FDFFDFDD"))