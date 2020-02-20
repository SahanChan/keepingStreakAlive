
operation = str(input(
    "Enter operation (Addition: +) (Minus: -) (Multiplication: *) (Division: /)  : "))
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your Second number: "))

if(operation == '+'):
    print("Ans: "+str(num1+num2))
elif(operation == '-'):
    print("Ans: "+str(num1-num2))
elif(operation == '*'):
    print("Ans: "+str(num1*num2))
elif(operation == '/'):
    print("Ans: "+str(num1/num2))
else:
    print("Error")
