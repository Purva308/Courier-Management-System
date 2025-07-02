class Employee:
    def __init__(self,employee_id=None,employeeName="",email="",contactNumber="",role="",salary=""):
        self.__employee_id=employee_id
        self.__employeeName=employeeName
        self.__email=email
        self.__contactNumber=contactNumber
        self.__role=role
        self.__salary=salary

    def __str__(self):
        return f"Employee[ID ={self.__employee_id},Name={self.__employeeName},Email={self.__email},Role={self.__role}]"

 #Getters
    def get_employee_id(self):
        return self.__employee_id

    def get_employeeName(self):
        return self.__employeeName

    def get_email(self):
        return self.__email

    def get_contactNumber(self):
        return self.__contactNumber

    def get_role(self):
        return self.__role

    def get_salary(self):
        return self.__salary

    #Setters

    def employee_id(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def employeeName(self, employeeName):
        self.__employeeName = employeeName

    def email(self, email):
        self.__email = email

    def contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def role(self, role):
        self.__role = role

    def salary(self, Salary):
        self.__salary = Salary