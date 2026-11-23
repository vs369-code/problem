'''#Input radius and print the area and circumference of a circle (use 3.14159).
r = int(input("Enter radius:"))
print(f"Area of circle:{3.14 * r * r}")
print(f"Circumference of circle:{2*3.14*r}")

#Input principal, rate and time and print simple interest.
p = int(input("Enter principal:"))
r = int(input("Enter rate:"))
t = int(input("Enter time:"))
print(f"Simple of interest is:{(p*r*t)/100}")

#Convert temperature from Celsius to Fahrenheit.
celsius = int(input("Enter temperature(C):"))
print(f"Temperature in fareheit:{9/5*celsius+32}F")

#Convert kilometres to miles (1 km = 0.621371 miles).
km = int(input("Enter kilometres:"))
print(f"Kilometres to miles:{km * 0.621371} miles.")

#Input two integers and print the quotient and remainder of their division.
num = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(f"Qutient of two number is:{num / num2}")
print(f"Remainder of two number is:{num % num2}")

#Input marks of three subjects and print the total and average.
a = int(input("Enter marks of first subject:"))
b = int(input("Enter marks of second subject:"))
c = int(input("Enter marks of third subject:"))

print(f"Total marks of three subject:{a+b+c}")
print(f"Average marks of three subject is:{(a+b+c)/3}")

#Check whether a number is even or odd.
e = int(input("Enter number:"))

if e % 2 == 0:
    print("Even number")
else:
    print("Odd number")   

#Find the larger of two numbers.
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))

if first_number > second_number:
    print(f"The largest number is {first_number}")
else:
    print(f"The largest number is {second_number}") 

#Find the largest of three numbers using nested if and also using if-elif.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a >= c and a >= b:
    print("a is largest.")
elif c >= a and c >= b:
    print("c is largest.")
 
    
else:
    print("b is largest.")  

#Check whether a number is positive, negative or zero.
num = int(input("Enter number:"))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")  
else:
    print("Negative number")

#Check whether a year is a leap year.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")'''

#Check whether an input character is a vowel or a consonant.
chara = input("Enter character:")

if chara in 'aeiou':
    print("Vowel character")
 
else:
    print("consonant character")      







        