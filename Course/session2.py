# # is_learning = True

# # while is_learning:
# #     print("learning on!")
# #     print("some more stuff")
# #     is_learning = input("Are you still going at it?")

# # # print("end game")

# friends = ["joe", "billy", "bob"]

# for friend in friends:
#     print(friend)

#----
#else with loops
#----
# cars = ["ok", "ok", "ok", "ok", "faulty", "ok"]

# for status in cars:
#     if status == "faulty":
#         print("Stop production")
#         break
#     print(f"This car is {status}")
#     print("shipping")
# else:    #if the break above is not triggered, then this will be triggered - so if "break" above - don't do else
# 	print("All cars built sucessfully") 

#prime number and for loops
#(nested loops)
# for n in range(2, 10)
#     for x in range(2, n)
#         if n % x == 0
#             print(f"{n} equals {x} * {n//x}")
#             break    # break here will only affect the most recent for
#     else:   #since no break will be triggered for a prime number, we can use an else
#         print(f"{n} is prime")
        
# ----
# List slicing
# ----
# friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
# print(friends[2:4])    # Will get positions 2 thru 4 - ie Anna and bob
# print(friends[1:])      # Will get everyone BUT the first one
# print(friends[:4])      # will get all BUT the 4th one
# print(friends[:])       # will get a new list of all elements
# print(friends[-3:])     # will get elements starting from the end of the list - Anna, bob, jen
# print(friends[-3:4])    # will get elements starting from end of the list through the 4th position 
# print(friends[:-2])    # start from the first element thru not the last two
# print(friends[-3:-1])   #start with 3rd from the end, go through 1st from end

# will work with lists or tuples

#-------
# List comprehensions
#-------
# numbers = [0,1,2,3,4]
# doubled_numbers = []

# #old and busted:
# for number in numbers:
#     doubled_numbers.append(number * 2)
# print(doubled_numbers)

# #new hotness
# doubled_numbers= [number * 2 for number in numbers] #foreach number in number - multiply that number by two and place result
# print(doubled_numbers)
# #or
# doubled_numbers = [number * 2 for number in range(5)] # so you don't have to init number list
# print(doubled_numbers)

# #for strings:
# friend_ages =[22,31,35,37]
# age_string = [f"My friend is {age} years old" for age in friend_ages]
# print(age_string)

# #or
# names = ["Rolf", "Bob", "Jen"]
# lower = [name.lower() for name in names]
# print(lower)

# # Title casing - in case you want to uppercase first letter use:
# print(f"{name.title()}" for name in names)

#---
#List comprehensions with conditionals
#---

# ages = [22,35,27,21,20]
# odds = [age for age in ages if age % 2 == 1]
# print(odds)

# # additional fun!
# friends = ["Rolf", "ruth", "charlie", "jen"]
# guests = ["jose", "bob", "Rolf", "Charlie", "michael"]

# friends_lower = [f.lower() for f in friends]

# present_friends = [
#     name.title() for name in guests if name.lower() in friends_lower
# ]
# print(present_friends)

# ----
# Set and dictionary comprehensions
# ----
# friends = ["Rolf", "ruth", "charlie", "jen"]
# guests = ["jose", "bob", "Rolf", "Charlie", "michael"]

# friends_lower = {n.lower() for f in friends}
# guests_lower = {n.lower() for n in guests}

# present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}

# print(present_friends)

# #new dictionary
# friends = ["Bob", "Julie", "Rick", "Frank"]
# time_since_seen = [3,7,15,11]

# long_timers = {
#     friends[i]: time_since_seen[i] for i in range(len(friends)) if time_since_seen[i] > 5
# }

# print(long_timers)

# --- 
# zip function
# ---
# friends = ["Bob", "Julie", "Rick", "Frank"]
# time_since_seen = [3,7,15,11]

# long_timers = dict(zip(friends, time_since_seen))  # creates a new list of tuples 

#old and busted
# long_timers = {
#     friends[i]: time_since_seen[i] for i in range(len(friends)) 
# }

# ----
# Enumerate fn
# ----
# friends = ["Bob", "Julie", "Rick", "Frank"]

# for counter, friend in enumerate(friends, start=1):   # enumerate retuns counter and the friend item
#     print(counter)
#     print(friend)
    
# print(list(enumerate(friends)))
# print(dict(enumerate(friends)))

# example
import random
 
# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))
 
# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}}
]
 
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
print(lottery_numbers)

top_player = players[0]  # start by saying "the top matching player is the first one"
 
for player in players:  # Go over each player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
    print(matched_numbers)
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # Say this player is the new top player
 
# Calculate their winnings using the formula!
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
 
print(f"{top_player['name']} won {winnings}.")