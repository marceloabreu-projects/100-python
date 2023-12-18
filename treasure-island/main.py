print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
choice = input("Left or Right? (L/R)")
if choice == "L":
    print("Proceed!")
    swim = input("Swim or wait? (S/W)")
    if swim == "S":
        print("Game over!")
    elif swim == "W":
        print("You are close!")
        door = input("Which door? (Red, Blue, Yellow)")
        if door == "Red":
            print("Game over!")
        elif door == "Blue":
            print("Game over!")
        elif door == "Yellow":
            print("You found the treasure!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
elif choice == "R":
    print("Game over!")
else:
    print("Invalid input!")