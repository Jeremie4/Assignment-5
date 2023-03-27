import random

user_num = int(input("Welcome to the Guessing Game\nThe Computer has picked a number from 1 - 10. Try to match it.\nWhat number do you choose (1-10): "))

ran_num = random.randint(1,10)

if user_num == ran_num:
    msg = "Honored to play with you, Master."
elif user_num + 1 == ran_num or user_num - 1 == ran_num:
    msg = "You are a worthy opponent, Knight."
elif user_num + 2 == ran_num or user_num - 2 == ran_num:
    msg = "You have much to learn, Padawan."
elif user_num + 3 == ran_num or user_num - 3 == ran_num:
    msg = "Youngling, your time will come."
else:
    msg = "Keep working hard in the Service Corps."

end_msg = ("You picked " + str(user_num) + ", and the actual number was " + str(ran_num) + ".\n" + msg)
print(end_msg)