# a = int(input("Enter your luck number between 1 to 10 :"))

# match a:
#     case 1:
#         print("YOU WON CAR")
#     case 3:
#         print("YOU WON BIKE")
#     case 6:
#         print("YOU WON LAPTOP")
#     case _:
#         print("Better luck next time")


import random

random_num = random.randint(1,3)


num = int(input("Enter a number between 1 to 3 :"))

if num == random_num:
        match num:
            case 1:
                print("NO")

            case 2:
                print("yes")
            
            case 3:
                print("NO")

            case _:
                print("invalide choice")

else:
     print("better luck next time! The randome number was : ",random_num)