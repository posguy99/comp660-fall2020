import M5_temperature as temp


def display_menu():
    print("Welcome to the Temperature Conversion Application")
    print("Menu")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")


def convert_temp():
    option = int(input("Enter a menu option: "))
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = temp.to_celsius(f)
        c = round(c, 2)
        print("Degrees Celsius: ", c)
    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = temp.to_fahrenheit(c)
        f = round(f, 2)
        print("Degrees Fahrenheit: ", f)
    else:
        print("You must enter a valid menu number.")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        again = input("Convert another temperature? (y/n): ")
        print("Thank you for using the application!")


if __name__ == "__main__":
    main()
