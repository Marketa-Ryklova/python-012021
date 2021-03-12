class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}"
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children


  def get_net_salary(self):
    net_salary = self.salary - (self.salary * 0.15 - self.children * 1500)
    return f" a jeho čístá mzda činí {net_salary} Kč"


pepa = Employee("Josef Novák", "junior developer", 35000, 2)
pepa.get_info()
print(pepa.get_info(), end = '')
print(pepa.get_net_salary())
