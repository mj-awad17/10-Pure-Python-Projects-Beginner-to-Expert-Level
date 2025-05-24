import os
import time
import random
import sys

# Cross-platform key press detection
if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios
    import select

# Game settings
WIDTH = 30
HEIGHT = 10
SNAKE_CHAR = 'o'
FOOD_CHAR = '*'
EMPTY_CHAR = ' '
DELAY = 0.2  # Snake speed (lower is faster)

# Direction vectors
DIRECTIONS = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1),
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_key():
    if os.name == 'nt':
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            return key
    else:
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1)
    return None


def render(snake, food, score):
    clear()
    print('+' + '-' * WIDTH + '+')
    for y in range(HEIGHT):
        row = '|'
        for x in range(WIDTH):
            if (y, x) in snake:
                row += SNAKE_CHAR
            elif (y, x) == food:
                row += FOOD_CHAR
            else:
                row += EMPTY_CHAR
        row += '|'
        print(row)
    print('+' + '-' * WIDTH + '+')
    print(f"Score: {score}")


def random_food(snake):
    while True:
        food = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if food not in snake:
            return food


def update_direction(key, current_direction):
    key_map = {
        'w': 'UP',
        's': 'DOWN',
        'a': 'LEFT',
        'd': 'RIGHT',
        '\x1b[A': 'UP',     # arrow up
        '\x1b[B': 'DOWN',   # arrow down
        '\x1b[D': 'LEFT',   # arrow left
        '\x1b[C': 'RIGHT',  # arrow right
    }
    new_dir = key_map.get(key)
    if new_dir:
        # prevent snake from reversing
        if (current_direction, new_dir) not in [('UP', 'DOWN'), ('DOWN', 'UP'), ('LEFT', 'RIGHT'), ('RIGHT', 'LEFT')]:
            return new_dir
    return current_direction


def main():
    if os.name != 'nt':
        # Set terminal to raw mode (Unix)
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    snake = [(HEIGHT // 2, WIDTH // 2)]
    direction = 'RIGHT'
    food = random_food(snake)
    score = 0

    try:
        while True:
            key = get_key()
            if key:
                direction = update_direction(key, direction)

            head = snake[0]
            dy, dx = DIRECTIONS[direction]
            new_head = (head[0] + dy, head[1] + dx)

            # Collision check
            if (new_head in snake or
                not (0 <= new_head[0] < HEIGHT) or
                not (0 <= new_head[1] < WIDTH)):
                render(snake, food, score)
                print("💥 Game Over! You crashed.")
                break

            snake.insert(0, new_head)

            if new_head == food:
                score += 1
                food = random_food(snake)
            else:
                snake.pop()

            render(snake, food, score)
            time.sleep(DELAY)

    finally:
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        print("👋 Thanks for playing!")


if __name__ == "__main__":
    main()