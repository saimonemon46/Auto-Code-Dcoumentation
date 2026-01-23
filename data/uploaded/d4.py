
# # Randomisation and python lists
# import random
# random_integer = random.randint(1,10)
# print(random_integer)


# random_float = random.random()
# print(random_float*5)



# # head 0 tail 1
# import random
# random_side = random.randint(0,1)
# if random_side == 0:
#     print("Head")
# else:
#     print("Tail")


## list
# fruits = ["Apple", "Banana", "Cherry"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])


# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america[7])
# print(states_of_america[-1])
# print(states_of_america[-8])

# states_of_america[1] = "Pencilv"
# print(states_of_america)



# a = [1,2,0]
# b = [3,5,8,8,7]
# a.extend(b)
# print(a)
# print(b)



# b.extend(a)
# print(b)




# # list input then randomly choose 


# import random

# # Define the names as a list
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# # Select a random person from the list
# person_who_will_pay = random.choice(names)

# print(f"{person_who_will_pay} is going to buy today's meal!")


# # game
# list1 = [" ", " ", " "]
# list2 = [" ", " ", " "]
# list3 = [" ", " ", " "]

# # 3d list
# map = [list1, list2, list3]

# print("Hiding your treasure! 'X' marks the spot")
# position = input("Enter the position : A(0-2) B(0-2) C(0-2) : ")
# letter = position[0].lower()

# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1])

# map[letter_index][number_index] = "X"
# print(f"{list1}\n{list2}\n{list3}")



## Rock Paper Scissors
import random
list = ["r","p","s"]
user = input("Enter your choice r for rock, p for paper, s for scissor :")
computer = random.choice(list)
print(f"You choose {user} and computer choose {computer}")

if user == computer:
    print("It's a draw.")
elif user == "r" and computer == "s" or user == "p" and computer == "r" or user == "s" and computer == "p":
    print("You win.")
else:
    print("You lose.")

























