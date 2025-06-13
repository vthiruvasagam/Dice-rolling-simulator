import random

def roll_dice():
    dice_face = random.randint(1, 6)
    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }
    for line in dice_art[dice_face]:
        print(line)

def main():
    print("🎲 Welcome to Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        roll_dice()
        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! 🎉")
            break

if __name__ == "__main__":
    main()




