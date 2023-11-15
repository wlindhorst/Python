# # First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# # Remember the uppercase H, the comma, and the space between words!
# name = input("What is your name? ")
# print (f"Hello, {name}")

# # Secondly, ask the user for their age and convert it into a number.
# # Then, print out how many months that equals to (you'll have to multiply the age by 12).
# age = int(input("What is your age? "))
# print(f"You are {age * 12} months")

# # short_tuple = ("Bob", "Joe")
# nearby_people = {'Rolf', 'Jen', 'Anna'}
# user_friends = set()  # This is an empty set, like {}

# # Ask the user for the name of a friend
# new_name = input("New name: ")

# # Add the name to the empty set
# user_friends.add(new_name)

# # Print out the intersection between both sets. This gives us a set with those friends that are nearby.
# all_peeps = nearby_people.intersection(user_friends)
# print(all_peeps)
nearby_people = {"Rolf", "Jen", "Anna"}
user_friends = set()  # This is an empty set, like {}
 
# friend = input("Enter your friend name to see if he is nearby: ")
text = "34cm"
result = text.endswith('cm')
print(result)
# # Add the friend to the user_friends set
# user_friends.add(friend)
 
# # Print out the friends that are nearby... those which are in both sets!
# print(user_friends.intersection(nearby_people))

# # create a set of integer type
# student_id = {112, 114, 116, 118, 115}
# print('Student ID:', student_id)

# # create a set of string type
# vowel_letters = {'a', 'e', 'i', 'o', 'u'}
# print('Vowel Letters:', vowel_letters)

# # create a set of mixed data types
# mixed_set = {'Hello', 101, -2, 'Bye'}
# print('Set of mixed data types:', mixed_set)