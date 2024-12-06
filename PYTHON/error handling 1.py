while True:
    try:
        name = input("Enter your name: ")
        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        surname = input("Enter your surname: ")
        if not isinstance(surname, str):
            raise ValueError("Surname must be a string")

        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be a positive integer")

        height = float(input("Enter your height (in cm): "))
        if height <= 0:
            raise ValueError("Height must be a positive number")

        weight = float(input("Enter your weight (in kg): "))
        if weight <= 0:
            raise ValueError("Weight must be a positive number")

        print("Personal details entered successfully:")
        print(f"Name: {name}")
        print(f"Surname: {surname}")
        print(f"Age: {age}")
        print(f"Height: {height} cm")
        print(f"Weight: {weight} kg")
        break
    except ValueError as e:
        print("Invalid input. Please try again.")
        print(e)