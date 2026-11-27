#----------Tip and Bill splitter----------------- 

layout = 30

total_bill = int(input("Enter amount of bill:"))
tip_percentage = int(input("Enter tip percentage of bill:"))
tip = total_bill * tip_percentage/100
number_of_people = int(input("Enter number of people:"))
individual_share = total_bill/number_of_people
print(f"Total bill:{total_bill+tip} ")
print(f"Tip amount:{tip}")
print('='*layout)
print(f"Each person pays:{individual_share}")


