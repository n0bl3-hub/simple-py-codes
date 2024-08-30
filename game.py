import random as ran

def dice_roll():
   number =ran.randint(1,6)
   print("you rolled a " + str(number))
   return number


max_score = 20
max_trial = 7

def start_game():
   current_trial = 0
   user_score =0
   print("Welcome to dodjo dice game")
   print("try to reach " + str(max_score) + "points to win the game")
   input("Press Enter to begin")

   while True:
        input("press enter to roll")
        current_roll = dice_roll()
        current_trial += 1
        user_score += current_roll

        if user_score>max_score:
            print("your score is " + str(user_score))
            print("you have extended the max score of 20")
            break
        elif current_trial>max_trial:
            print("you have exceded the max trial of 7")
            print("your score is "+ str(user_score))
            break
        elif user_score== max_score:
            print("your score is "+ str(user_score))
            print("congrat, you won")
            break
        else:
            print("You rolled a " + str(current_roll))
            print("Your score is " + str(user_score))


      

#    while user_score < max_score and current_trial < max_trial:
#         current_roll = dice_roll()
#         user_score += current_roll 
#         current_trial = current_trial + 1
#         if user_score > max_score:
#             print("Your final score was " + str(user_score))
#             print("You have exceeeded the maximum score.")
#             break
#         elif user_score == max_score:
#             print("Your final score" + str(user_score))
#             print("Congratulations, you have won")
#             break
#         if user_score< max_score:
#            print("Your final score was" + str(user_score))

     
          
        
        


start_game() 