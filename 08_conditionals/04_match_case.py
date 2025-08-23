a = int(input("Enter your luck number between 1 to 10 :"))

match a:
    case 1:
        print("YOU WON CAR")
    case 3:
        print("YOU WON BIKE")
    case 6:
        print("YOU WON LAPTOP")
    case _:
        print("Better luck next time")