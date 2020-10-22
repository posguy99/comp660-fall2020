
# from Maryam's discussion example...

total = 0
count = 0
largest = None
smallest = None

while True:
    try:
        number = input("Please enter a  number: ")
        if number == "done":
            break
        number = float(number)
        count += 1
        total += number
        if smallest is None or number < smallest:
            smallest = number

        if largest is None or number > largest:
            largest = number

    except ValueError:
        print("Invalid input")

print(total, count, smallest, largest)
