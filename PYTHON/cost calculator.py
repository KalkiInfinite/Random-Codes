def calculate_admission_cost(ages):
    total_cost = 0
    for age in ages:
        if age <= 2:
            cost = 0.00
        elif 2 < age <= 12:
            cost = 14.00
        elif age >= 65:
            cost = 18.00
        else:
            cost = 23.00
        total_cost += cost
    return total_cost

num_guests = int(input("Enter the number of guests: "))
guest_ages = [int(input(f"Enter the age of guest {i+1}: ")) for i in range(num_guests)]
total_admission_cost = calculate_admission_cost(guest_ages)
print(f"The total admission cost for the group is ${total_admission_cost:.2f}")