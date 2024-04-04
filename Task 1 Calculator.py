
operator=input("Select the Arithmetic Operator(+,-,*,/):")
num1=float(input("Enter  Number 1:"))
num2=float(input("Enter Number 2:"))
if operator == "+":
    result=num1+num2
    print(num1,"+",num2,"=",result)
elif operator == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operator == "*":
    result=num1*num2
    print(num1, "*", num2, "=", result)
elif operator == "/":
    result=num1/num2
    print(num1, "/", num2, "=", result)

else:
    print("Invalid")
