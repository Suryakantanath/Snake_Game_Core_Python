import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_boundary(height, width):
    print('-' * width)
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    print('-' * width)

def print_game(snake, food, height, width):
    board = [[' ' for _ in range(width)] for _ in range(height)]

    # Draw boundaries
    for x in range(width):
        board[0][x] = '-'
        board[height - 1][x] = '-'
    for y in range(height):
        board[y][0] = '|'
        board[y][width - 1] = '|'

    # Draw food
    board[food[0]][food[1]] = '.'

    # Draw snake
    for segment in snake:
        board[segment[0]][segment[1]] = '.'

    # Print board
    for row in board:
        print(''.join(row))

def main():
    height, width = 20, 40
    snake = [[10, 15]]  # Initial snake position
    direction = 'RIGHT'

    # Initial food position
    food = [random.randint(1, height - 2), random.randint(1, width - 2)]
    while food in snake:
        food = [random.randint(1, height - 2), random.randint(1, width - 2)]

    while True:
        clear_screen()
        print_game(snake, food, height, width)
        
        # Input for direction
        key = input("Move (W/A/S/D): ").upper()
        if key == 'W' and direction != 'DOWN':
            direction = 'UP'
        elif key == 'S' and direction != 'UP':
            direction = 'DOWN'
        elif key == 'A' and direction != 'RIGHT':
            direction = 'LEFT'
        elif key == 'D' and direction != 'LEFT':
            direction = 'RIGHT'

        # Calculate new head position
        head = snake[0]
        if direction == 'UP':
            new_head = [head[0] - 1, head[1]]
        elif direction == 'DOWN':
            new_head = [head[0] + 1, head[1]]
        elif direction == 'LEFT':
            new_head = [head[0], head[1] - 1]
        elif direction == 'RIGHT':
            new_head = [head[0], head[1] + 1]

        # Check for collisions
        if (
            new_head in snake or  # Collision with itself
            new_head[0] == 0 or new_head[0] == height - 1 or  # Collision with top/bottom boundary
            new_head[1] == 0 or new_head[1] == width - 1  # Collision with left/right boundary
        ):
            print("Game Over!")
            break

        # Move the snake
        snake.insert(0, new_head)

        # Check if food is eaten
        if new_head == food:
            food = [random.randint(1, height - 2), random.randint(1, width - 2)]
            while food in snake:
                food = [random.randint(1, height - 2), random.randint(1, width - 2)]
        else:
            # Remove the tail
            snake.pop()

        time.sleep(0.2)

if __name__ == "__main__":
    main()
