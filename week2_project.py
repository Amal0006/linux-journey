def isEven(number):
	if number%2==0:
		return "Even"
	else:
		return "Odd"

def calculator(num1,num2,operator):
	if operator=="+":
		return num1+num2
	elif operator=="-":
		return num1-num2
	elif operator=="*":
		return num1*num2
	elif operator=="/":
		if num2==0:
			print("Cannot divide by zero")
		else:
			return num1/num2
	else:
		print("Invalid operator")

print("=========Python Mini Project=========")

for i in range(1,6):
	print(i,"is",isEven(i))

num1=float(input("Enter num1: "))
num2=float(input("Enter num2: "))
operator=input("Enter the operator: ")
print("Result: ",calculator(num1,num2,operator))
