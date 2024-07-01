import json

try:
    with open('department_salaries.json', 'r') as file:
        data = json.load(file)

    average_salaries = {}

    for department, salaries in data.items():
        total_salary = sum(salaries)
        average_salary = total_salary / len(salaries)
        average_salaries[department] = average_salary

    with open('avg_salary.json', 'w') as json_file:
        json.dump(average_salaries, json_file, indent=4)
    print("Average salaries calculated and written to avg_salary.json")

except FileNotFoundError:
    print("Error: File not found.Make sure department_salaries.json exists.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in department_salaries.json.")
except Exception as e:
    print(f"An error occurred: {e}")
