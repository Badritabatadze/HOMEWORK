import random

def forest_adventure():
    print("Welcome to the Mysterious Forest Adventure!")
    print("You find yourself at the entrance of a dense forest. Your adventure begins now.")
    
    player_health = 100
    obstacles = ["wild animals", "rivers", "cliffs"]
    
    while True:
        print("\nCurrent Health:", player_health)
        print("Choose your action:")
        print("1. Proceed forward")
        print("2. Search for items")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            obstacle = random.choice(obstacles)
            print("You encounter", obstacle)
            if obstacle == "wild animals":
                damage = random.randint(10, 30)
                player_health -= damage
                print("You lost", damage, "health in the battle with wild animals.")
            elif obstacle == "rivers":
                print("You find a river blocking your path.")
                print("You need to find a way to cross it.")
                # You can add more choices and outcomes here
            elif obstacle == "cliffs":
                print("You reach a cliff.")
                print("You need to find a safe way down.")
                # You can add more choices and outcomes here
            
            if player_health <= 0:
                print("Your health has dropped to zero. Game Over!")
                break
        elif choice == '2':
            print("You search for items but find nothing useful.")
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Start the game
forest_adventure()