def servings(text):
    while True:
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("Invalid Input. Valid Numbers Only")

try:
    original_serving = servings("Enter Number of Servings the Recipe is Originally for: ")

    desired_serving = servings("Enter Number of Servings You Wish to Make: ")

    try:
        adjustment_factor = desired_serving / original_serving

        print('Recipe is Now Adjusted For', desired_serving, 'Servings')

    except ZeroDivisionError:
        print("Zero Divison Error ")


finally:
    print("Enjoy Your Cooking!")
