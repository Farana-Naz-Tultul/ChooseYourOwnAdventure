player = input("Welcome to the Adventure game. What shall I call you? ")
print("Welcome", player, "to this adventure.")

answer = input("You are on a dirt road, which now has come to an end. To continue forward, you must go left or right. Which way would you like to go (left/right)? ").lower()

if answer == "left":
    answer = input("You have come across a river. Do you wanna swim across or walk around it (swim/walk)? ").lower()
    if answer == "swim":
        print("You swim across the river and a crocodile attacks you. You lose...")
    elif answer == "walk":
         print("You walk aa long way around the river and faint due to fatigue. You lose...")
    else:
        print("Not a valid answer. You lose...")

elif answer == "right":
    answer = input("You come across a bridge which looks wobbly. Do you wish to cross it or head back (cross/back)? ").lower()
    if answer == "cross":
        answer = input("You see a stranger on the bridge. Do you wish to talk to them (yes/no? ").lower()
        if answer == "yes":
            print("The stranger gives you a valuable treasure. You win!!!")
        elif answer == "no":
            print("You ignore the stranger and offend them. You lose...")
        else:
            print("Not a valid answer. You lose...")

    elif answer == "back":
         print("You go back so you lose...")
    else:
        print("Not a valid answer. You lose...")

else:
    print("Not a valid answer. You lose...")

print("Thank you for playing. Goodbye!")