# print("Hello World")

""" # Inputs
# How many voyes did you get?
myVotes = int(input("How many votes did you get in the election? "))
# Total votes in the election
totalVotes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you recieved.
percentageVotes = (myVotes / totalVotes) * 100
print("I recieved " + str(percentageVotes)+"% of the toal votes. ") """

""" # If Statements
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1]) """

""" # If=Else Statements
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC. ")
else:
    print("Open the windows. ") """

""" # Nested If-Else Statements
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print("Your grade is a B.")
elif score >=70:
    print("Your grade is a C.")
elif score >=60:
    print("Your grade is a D.")
else:
    print("Your grade is an F.") """

''' # Membership Operators
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.") '''

# Logical Operators
counties = ["Arapahoe", "Denver", "Jefferson"]

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
