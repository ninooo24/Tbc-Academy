import json

try:
    with open('employee.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("File does not exist")


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = int(salary)


class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = [Employee(emp['name'], emp['position'], emp['salary']) for emp in employees]

    def average_salary(self):
        salaries = [emp.salary for emp in self.employees]
        return sum(salaries) / len(salaries) if salaries else 0

    def max_salary(self):
        salaries = [emp.salary for emp in self.employees]
        return max(salaries) if salaries else 0

    def min_salary(self):
        salaries = [emp.salary for emp in self.employees]
        return min(salaries) if salaries else 0

    def count_positions(self):
        positions = {}
        for emp in self.employees:
            positions[emp.position] = positions.get(emp.position, 0) + 1
        return positions


def create_departments():
    departments = []
    for dept_data in data.values():
        department = Department(dept_data['name'], dept_data['description'], dept_data['employees'])
        departments.append(department)
    return departments


def main():
    departments = create_departments()
    for dept in departments:
        print('\n' + dept.name)
        print(f'Description: {dept.description}')
        print(f'Average salary: {dept.average_salary()}')
        print(f'Max salary: {dept.max_salary()}')
        print(f'Min salary: {dept.min_salary()}')
        print(f'Position counts: {dept.count_positions()}')


if __name__ == '__main__':
    main()
