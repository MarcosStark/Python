employee = ["Marcos", "André", "Vanessa", "Francisco","Claudia", "Marcelo", "Alexandre", "Fernanda", "Tiago"]
emp_pm = ["Marcos", "André", "Vanessa", "Francisco"]
emp_am = ["Claudia", "Marcelo", "Alexandre", "Fernanda", "Tiago"]
emp_car = ["Marcos", "Fernanda", "Tiago"]

"""
#Converts list to set
employee = set(employee)
emp_pm = set(emp_pm)
emp_am = set(emp_am)
emp_car = set(emp_car)

#Employees who own a car and work at night
emp_car_pm = emp_pm.intersection(emp_car)
print(f"Esses são os funcionários que possuem carro e trabalham à noite: {emp_car_pm}")

#Employees who own a car and work at morning
emp_car_am = emp_am.intersection(emp_car)
print(f"Esses são os funcionários que possuem carro e trabalham pelo dia: {emp_car_am}")

#Employees whon own't a car
emp_not_car = employee.difference(emp_car)
print(f"Esses são os funcionários que não possuem carro: {emp_not_car}")
"""
#Other way
#Employees who own a car and work at night
emp_car_pm = set(emp_pm).intersection(emp_car)
print(f"Esses são os funcionários que possuem carro e trabalham à noite: {emp_car_pm}")

#Employees who own a car and work at morning
emp_car_am = set(emp_am).intersection(emp_car)
print(f"Esses são os funcionários que possuem carro e trabalham pelo dia: {emp_car_am}")

#Employees whon own't a car
emp_not_car = set(employee).difference(emp_car)
print(f"Esses são os funcionários que não possuem carro: {emp_not_car}")