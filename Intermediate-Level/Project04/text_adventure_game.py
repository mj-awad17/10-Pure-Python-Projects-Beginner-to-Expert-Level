# Text-based advanture game with story, map & Puzzles
# 🧙‍♂️ Text-Based Adventure Game with Story, Map & Puzzle

def show_instructions():
    print("""
=== Welcome, Brave Explorer! ===
Your quest is to retrieve the 💎 Crystal of Light hidden in the Tower.
Explore, gather items, and unlock the secret chamber.

Commands:
- Type 'go [direction]' to move
- Type 'look' to search the room
- Type 'inventory' to check your items
- Type 'map' to view the area
- Type 'quit' to exit
    """)

def show_map():
    print("""
            [Tower]
               |
    [Hut] -- [Forest] -- [River]
               |
            [Cave]
    """)

def show_status(location, inventory):
    print(f"\nYou are in the '{location}'.")
    print(f"Inventory: {inventory}")

def adventure_game():
    rooms = {
        'Forest': {'north': 'Tower', 'east': 'River', 'south': 'Cave', 'west': 'Hut'},
        'Cave': {'north': 'Forest', 'item': 'Sword', 'locked': True},
        'River': {'west': 'Forest', 'item': 'Shield', 'locked': True},
        'Tower': {'south': 'Forest', 'locked': True, 'item': 'Crystal'},
        'Hut': {'east': 'Forest', 'item': 'Armor', 'locked': True},
    }

    inventory = []
    location = 'Forest'

    show_instructions()

    while True:
        show_status(location, inventory)
        move = input("> ").lower().strip()

        if move == "quit":
            print("Thanks for playing. Farewell!")
            break

        elif move == "map":
            show_map()

        elif move == "inventory":
            print("Inventory:", inventory)

        elif move == "look":
            room = rooms[location]
            if "item" in room and room["item"] not in inventory:
                item = room["item"]
                print(f"You see a {item}.")
                take = input(f"Do you want to take the {item}? (yes/no): ").lower()
                if take == "yes":
                    inventory.append(item)
                    print(f"You picked up the {item}.")
                else:
                    print("You left it.")
            else:
                print("Nothing interesting here.")

        elif move.startswith("go "):
            direction = move.split()[1]
            if direction in rooms[location]:
                next_room = rooms[location][direction]
                # Puzzle: Tower is locked unless Sword and Shield are collected
                if next_room == "Tower":
                    if rooms["Tower"].get("locked") and ("Sword" in inventory and "Shield" in inventory and "Armor" in inventory):
                        print("You used the Sword and Shield to break the Tower seal!")
                        rooms["Tower"]["locked"] = False
                        location = "Tower"
                    elif rooms["Tower"]["locked"]:
                        print("The Tower is sealed. You need both the Armor, Sword and Shield to enter.")
                    else:
                        location = "Tower"
                else:
                    location = next_room
            else:
                print("You can't go that way.")

        # Ending condition
        if location == "Tower" and "Crystal" in rooms["Tower"].get("item", []):
            if "Crystal" not in inventory:
                print("You found the 💎 Crystal of Light💎! You win!🎉")
                inventory.append("Crystal")
                break

        else:
            continue

if __name__ == "__main__":
    adventure_game()
