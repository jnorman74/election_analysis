# print("Hello World")

# Inputs
""" # How many voyes did you get?
myVotes = int(input("How many votes did you get in the election? "))
# Total votes in the election
totalVotes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you recieved.
percentageVotes = (myVotes / totalVotes) * 100
print("I recieved " + str(percentageVotes)+"% of the total votes. ")
print("")
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
print("") """
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

""" # Logical Operators
counties = ["Arapahoe", "Denver", "Jefferson"] """

""" if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.") """


""" for county in counties:
    print(county)
    
for i in range(len(counties)):
    print(counties[i]) """

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

""" for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county)) """

""" for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
print("")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
print("") """
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)



print("")

for county_dict in voting_data:
    print(county_dict['registered_voters'])

print("")

for county_dict in voting_data:
    print(county_dict['county'])

print("")

for county_dict in voting_data:
    print(f"county_dict['county'] has county_dict['registered_voters':,] registered voters.")

print("")

""" candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate) """

""" for county, voters in counties_dict.items():
    f"{county} county has {voters:,} registered voters." """


