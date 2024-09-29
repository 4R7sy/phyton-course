salary = float(input("Write your average salary: "))
high = salary * 10 / 100
highSalary = salary + high
low = salary * 15 / 100
lowSalary = salary + low
if salary <= 1250:
    print("Your salary is low, so your new salary is {}".format(lowSalary))
else:
    print("Your salary is high, so your new salary is {}".format(highSalary))
