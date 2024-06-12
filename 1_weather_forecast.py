def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    
    except ZeroDivisionError:
        print("Zero Division Error.")
        return None
    
    except OverflowError:
        print("Overflow Error.")
        return None
    
    finally:
        print('Thanks For Using The Weather Converter')

try:
    user_input = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(user_input)

    if celsius is not None:
        print(user_input, 'Fahrenheit is', celsius, 'Celsius')

except ValueError:
    print("Invalid Input. Numbers Only ")
