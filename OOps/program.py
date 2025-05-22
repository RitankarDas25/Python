#create class employee with attributes role,department,salary and create a show details method
# create a clss engineer that inherites from employee class and has attributes name and age
class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.department=dept
        self.salary=sal

    def showDetails(self):
        print("Role :",self.role)
        print("Department :",self.department)
        print("Salary : Rs",self.salary)
    
class Engineer(Employee):
    def __init__(self,name,age, role, dept, sal):
        super().__init__(role, dept, sal)
        self.name=name
        self.age=age

    def showDetails(self):
        print("Name :",self.name)
        print("Age :",self.age)
        super().showDetails()

e1= Engineer("Ritankar Das",22,"SD1","Tech","37000")
e1.showDetails()