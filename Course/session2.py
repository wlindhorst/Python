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
        
        