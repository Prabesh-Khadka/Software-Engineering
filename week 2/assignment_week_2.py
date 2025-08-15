# Define the Human_resources class
class Human_resources:
    def __init__(self, name, salary, job_title):
        self.name = name                # Store the employee's name
        self.salary = salary            # Store the employee's salary as a number
        self.job_title = job_title      # Store the employee's job title
    
    # Display employee information
    def display_info(self):
        print(f"Employee's name: {self.name}")                   # Print employee name
        print(f"Employee's Salary: ${self.salary:,.2f}")         # Print salary with comma separators
        print(f"Employee's Job title: {self.job_title}")         # Print job title
        print("-" * 10)                                          # Separator line for clarity

    # Increase employee salary
    def give_raise(self, amount):
        print(f"{self.name} has received a raise of ${amount:,.2f}")  # Show the raise amount
        self.salary += amount                                        # Add raise to current salary
        print(f"New salary: ${self.salary:,.2f}")                     # Show updated salary
        print("-" * 20)                                              # Separator


# Create employees with correct data types (salary as number)
employee1 = Human_resources("Prabesh Khadka", 55000, "Software Developer")
employee2 = Human_resources("Bapan Shakya", 50000, "Quality Assurance")
employee3 = Human_resources("Anjan Panta", 45000, "Software Developer")

# Display initial info for each employee
employee1.display_info()
employee2.display_info()
employee3.display_info()

# Give raises to employee1
employee1.give_raise(5000)
employee1.give_raise(3000)
employee1.give_raise(10000)

# Display updated info after raises
employee1.display_info()
employee2.display_info()
employee3.display_info()
