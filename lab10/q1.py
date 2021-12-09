class Employee:
    def __init__(self,first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
    
    def generate_email(self):
        self.email = self.first_name + self.last_name + "@upes.com"
    
    def print_employee_details(self):
        print("[*] Employee details:")
        print("\t- First Name: "+self.first_name)
        print("\t- Last Name: "+self.last_name)
        print("\t- Salary: "+str(self.pay))
        print("\t- Email: "+self.email)

emp = Employee("Mohandas","Ghandi",50000)
emp.generate_email()
emp.print_employee_details()