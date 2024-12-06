# Code by Piyush
employee_data = {}

emp_id = input("Enter employee ID (or 'q' to quit): ")
while emp_id != 'q':
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    employee_data.update({emp_id: (name, department)})

    filename = "employeedetails.txt"
    with open(filename, "w") as file:
        for emp_id, (name, department) in employee_data.items():
            file.write(f"{emp_id},{name},{department}\n")

    print(f"Employee details have been saved to '{filename}'.")
    emp_id = input("Enter employee ID (or 'q' to quit): ")