class MyOrg(list):
    def __init__(self, name,salary,job_name,phone_number):
        self.name = name
        self.salary = salary
        self.job_name = job_name
        self.phone_number = phone_number
    
    def information(self):
        return self.name, self.salary, self.job_name,self.phone_number

    def add_to_list(self):
        info = MyOrg.information
        print(info,'<<')
        employeeList = []
        employeeList.extend([info])
        for emp in employeeList:
            print(employeeList[::-1])



employee_Fahad = MyOrg(
    name=input('Employee Name : '), 
    salary=input('Salary : '), 
    job_name=input('Job Name :'),
    phone_number=input('phone_number :'),
)

print(employee_Fahad.information())
employee_Fahad.add_to_list()

