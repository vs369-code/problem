#Digital Business card maker

width = 30
name = input("Enter user name:")
job_role = input("Enter job role:")
city = input("Enter city name:")
skills = input("Enter skills:")
cout = len(skills.split(','))
year_of_experience = str(input("Enter year of experience:"))
fav_quote = input("Enter favourite quote:")

border = "=" * width
print(border)
print(f"Name: {name}")
print(f"Job role: {job_role}")
print(f"City:{city}")
print(f"Skills: {skills}")
print(f"Year of experience: {year_of_experience}")
print(f"Favourite quote: {fav_quote}")
print(border)



#width = 30 - sets the card width to 30 characters.
#"=" * width - repeats = 30 times to create a border.
#.center(width) - place text in the centre of the card.
#split(',') → Separates skills wherever a comma appears.
#len() → Counts the number of separated skills.
#count → Stores the total number.

