import sys

class Room:
    def __init__(self, name, description, exits, puzzle=None):
        self.name = name
        self.description = description
        self.exits = exits  # dict: direction -> room_name
        self.puzzle = puzzle
        self.solved = False

class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self):
        print(self.question)
        user_answer = input("> ").strip().lower()
        return user_answer == self.answer.lower()

class Game:
    def __init__(self):
        self.rooms = self.create_map()
        self.current_room = 'Entrance'
        self.inventory = []

    def create_map(self):
        return {
            'Entrance': Room(
                'Entrance',
                'You stand at the entrance of a mysterious cave. Paths lead north and east.',
                {'north': 'Puzzle Room', 'east': 'Treasure Room'}
            ),
            'Puzzle Room': Room(
                'Puzzle Room',
                'A locked door blocks your way. There is a riddle on the wall.',
                {'south': 'Entrance', 'north': 'Exit'},
                Puzzle("I speak without a mouth and hear without ears. What am I?", "echo")
            ),
            'Treasure Room': Room(
                'Treasure Room',
                'You see a glittering chest. There is a key inside.',
                {'west': 'Entrance'}
            ),
            'Exit': Room(
                'Exit',
                'You see sunlight! You have escaped the cave. Congratulations!',
                {}
            )
        }

    def play(self):
        print("Welcome to the Cave Adventure!")
        while True:
            room = self.rooms[self.current_room]
            print(f"\n{room.description}")

            if self.current_room == 'Treasure Room' and 'key' not in self.inventory:
                print("You take the key.")
                self.inventory.append('key')

            if room.puzzle and not room.solved:
                if 'key' in self.inventory:
                    print("You use the key to unlock the puzzle door.")
                    if room.puzzle.ask():
                        print("Correct! The door opens.")
                        room.solved = True
                    else:
                        print("Wrong answer. Try again next time.")
                        continue
                else:
                    print("The door is locked. Maybe there's a key somewhere.")
                    continue

            if self.current_room == 'Exit':
                print("Game Over. Thanks for playing!")
                break

            print("Exits:", ', '.join(room.exits.keys()))
            move = input("Which direction do you want to go? ").strip().lower()
            if move in room.exits:
                self.current_room = room.exits[move]
            else:
                print("You can't go that way.")

if __name__ == "__main__":
    Game().play()