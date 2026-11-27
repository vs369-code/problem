#Input marks (0-100) and print grade: A (90+), B (75+), C (60+), D (40+), else Fail.

marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")    
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")  

#Input three sides and check whether they can form a triangle.

a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
    print("It is a triangle.")
else:
    print("It is not a triangle.")  

#Make a simple calculator: input two numbers and an operator (+, -, *, /, //, %, **) and print the result

while True:
    a = float(input("Enter first number:"))
    opr = input("Enter operator (+, -, *, /):")
    b = float(input("Enter second number:"))

     
    if opr == "+":
        print(f"Answer:{a+b}")
    elif opr == "-":
        print(f"Answer:{a-b}")
    elif opr == "*":
        print(f"Answer:{a*b}")    
    elif opr == "/":
        if b != 0:
            print("Answer:", a / b)
        else:
            print("Cannot divide by zero")    
    else:
        print("Error!")

    choose = input("Do you want to calculate again? (yes/no):").lower()
    if choose == "no":
        print("calculator closed.")
        break
   

     




 


 

             
 











