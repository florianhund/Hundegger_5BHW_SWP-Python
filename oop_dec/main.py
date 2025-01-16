from typing import Counter


class Person:
    def __init__(self, name, gender):
        self.name = name
        if gender not in ["M", "F", "D"]:
            raise ValueError("Gender must be 'M' (Male), 'F' (Female), or 'D' (Diverse).")
        self.gender = gender


class Employee(Person):
    def __init__(self, name, gender, department):
        super().__init__(name, gender)
        if not isinstance(department, Department):
            raise TypeError("department must be an instance of Department.")
        self.department = department
        department.add_employee(self)


class DepartmentHead(Employee):
    def __init__(self, name, gender, department):
        if not isinstance(department, Department):
            raise TypeError("department must be an instance of Department.")
        if department.department_head is not None:
            raise ValueError(f"Department {department.name} already has a head.")
        super().__init__(name, gender, department)
        department.set_department_head(self)


class Department:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Department name cannot be empty.")
        self.name = name
        self.employees = []
        self.department_head = None

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee instances can be added to a department.")
        self.employees.append(employee)

    def set_department_head(self, head: DepartmentHead):
        if not isinstance(head, DepartmentHead):
            raise TypeError("Head must be an instance of DepartmentHead.")
        self.department_head = head

    def employee_count(self):
        return len(self.employees)


class Company:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Company name cannot be empty.")
        self.name = name
        self.departments = []

    def add_department(self, department: Department):
        if not isinstance(department, Department):
            raise TypeError("Only Department instances can be added to the company.")
        if department in self.departments:
            raise ValueError(f"Department {department.name} is already part of the company.")
        self.departments.append(department)

    def total_employees(self):
        return sum(dept.employee_count() for dept in self.departments)

    def total_departments(self):
        return len(self.departments)

    def largest_department(self):
        if not self.departments:
            raise ValueError("No departments available to determine the largest.")
        return max(self.departments, key=lambda dept: dept.employee_count())

    def gender_percentage(self):
        all_employees = [
            e.gender for department in self.departments for e in department.employees
        ]
        if not all_employees:
            raise ValueError("No employees available to calculate gender distribution.")
        counts = Counter(all_employees)
        total = sum(counts.values())
        return {gender: (count / total) * 100 for gender, count in counts.items()}


if __name__ == "__main__":
    try:
        company = Company("ABC Inc.")

        it = Department("IT")
        hr = Department("HR")

        company.add_department(it)
        company.add_department(hr)

        it_head = DepartmentHead("Alice", "F", it)
        it.add_employee(it_head)
        it.add_employee(Employee("Bob", "M", it))
        it.add_employee(Employee("Charlie", "M", it))

        hr_head = DepartmentHead("Diana", "F", hr)
        hr.add_employee(hr_head)
        hr.add_employee(Employee("Eve", "F", hr))

        print("Total number of employees:", company.total_employees())
        print("Number of department heads:", len([d.department_head for d in company.departments if d.department_head]))
        print("Number of departments:", company.total_departments())
        print(
            "Department with the most employees:",
            company.largest_department().name,
        )
        print("Gender distribution (%):", company.gender_percentage())
    except Exception as e:
        print(f"An error occurred: {e}")
