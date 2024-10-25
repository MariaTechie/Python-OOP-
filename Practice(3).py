# Employee class definition
class Employee():
    # Constructor to initialize name, position, and salary
    def __init__(self, name, position, salary):
        self.__name = name  # Private variable for employee name
        self.__salary = salary  # Private variable for employee salary
        self.__position = position  # Private variable for employee position

    # Getter method to retrieve salary
    def getSalary(self):
        return self.__salary

    # Setter method to update salary
    def setSalary(self, value):
        self.__salary = value

    # Getter method to retrieve position
    def getPosition(self):
        return self.__position

    # Setter method to update position
    def setPosition(self, value):
        self.__position = value

    # Getter method to retrieve name
    def getName(self):
        return self.__name

    # Setter method to update name
    def setName(self, value):
        self.__name = value

    # Method to display employee information
    def display(self):
        return f'''
                Name: {self.__name}
                Position: {self.__position}
                Salary: {self.__salary}'''

    # Method to calculate a raise based on years and performance
    def get_raise(self, years, performance):
        # If performance is good and years are more than 5, give a 20% raise
        if performance == 'good' and years > 5:
            salary = self.getSalary()
            percentage = 0.2 * salary
            print(f'{percentage}$ will be added to the salary ')
            salary += percentage
            self.setSalary(salary)
            return f'The new salary will be {self.__salary}'
        
        # If performance is good and years are less than 5, give a 10% raise
        elif performance == 'good' and years < 5:
            salary = self.getSalary()
            percentage = 0.1 * salary
            print(f'{percentage}$ will be added to the salary ')
            salary += percentage
            self.setSalary(salary)
            return f'The new salary will be {self.__salary}'

        # If performance is bad and years are less than 5, no raise
        elif performance == 'bad' and years < 5:
            salary = self.getSalary()
            return f'The current salary is {salary}'

        # If performance is bad and years are more than 5, give a 7% raise
        else:
            salary = self.getSalary()
            percentage = 0.07 * salary
            print(f'{percentage}$ will be added to the salary ')
            salary += percentage
            self.setSalary(salary)
            return f'The new salary will be {self.__salary}'

# Creating an Employee object
object1 = Employee('issa', 'engineer', 800)
# Testing the get_raise method
print(object1.get_raise(6, 'good'))
# Display employee information
print(object1.display())
print("------------------------------------------------------------------------------------------------------------------------------")

# Manager class inheriting from Employee class
class Manager(Employee):
    # Constructor to initialize manager's name, salary, team, and position
    def __init__(self, name, salary, team, position='manager'):
        super().__init__(name, salary, position)  # Call the constructor of Employee
        self.__team = team  # Private variable for the manager's team

    # Getter method to retrieve the team
    def getTeam(self):
        return self.__team

    # Method to add a new member to the team
    def addToTeam(self, new_member):
        return self.__team.extend(new_member)  # Adding items to an existing list

    # Method to view team members
    def viewTeam(self):
        return f'The team members are {self.__team}'

    # Method to assign tasks to team members
    def task(self, employee, description):
        groupe = self.getTeam()
        # Check if the employee is in the team
        if employee not in groupe:
            print(f'{employee} not in the team')
        else:
            print(f'"{description}" has been assigned successfully to {employee}')

# Creating a Manager object
object2 = Manager('jhon', 2920, ['hadi', 'rami', 'carl', 'jake'])
# Viewing the team members
print(object2.viewTeam())
# Adding new members to the team
print(object2.addToTeam(['sami', 'khai', 'damon']))
# Viewing the updated team
print(object2.viewTeam())
# Assigning a task to a team member
object2.task('khai', 'give the design')

# Creating another Employee object
object7 = Employee('toni', 'teacher', 7000)
# Display employee information
print(object7.display())
# Testing the get_raise method
print(object7.get_raise('good', 6))
# Display updated employee information
print(object7.display())
