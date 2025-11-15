import random
import os
import time

# Initialize the game settings
WIDTH = 20
HEIGHT = 10
SNAKE_HEAD = 'O'
SNAKE_BODY = 'o'
FOOD = '*'
EMPTY = ' '

# Function to print the game board
def print_board(snake, food):
    os.system('cls' if os.name == 'nt' else 'clear')
    board = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

    # Place the snake on the board
    for x, y in snake:
        board[y][x] = SNAKE_BODY if (x, y) != snake[0] else SNAKE_HEAD

    # Place the food on the board
    x, y = food
    board[y][x] = FOOD

    # Print the board
    for row in board:
        print(' '.join(row))

# Function to move the snake
def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == 'left':
        head_x -= 1
    elif direction == 'right':
        head_x += 1
    elif direction == 'up':
        head_y -= 1
    elif direction == 'down':
        head_y += 1
    return [(head_x, head_y)] + snake[:-1]

# Function to check if the snake eats the food
def check_food(snake, food):
    return snake[0] == food

# Function to generate new food
def generate_food(snake):
    while True:
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)

# Main function to run the game
def main():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = 'right'
    food = generate_food(snake)

    while True:
        print_board(snake, food)
        time.sleep(0.1)

        # Get user input for direction
        new_direction = input("Enter direction (left/right/up/down): ").lower()
        if new_direction in ('left', 'right', 'up', 'down'):
            direction = new_direction

        # Move the snake
        snake = move_snake(snake, direction)

        # Check if the snake eats the food
        if check_food(snake, food):
            snake.append(snake[-1])  # Increase the length of the snake
            food = generate_food(snake)

        # Check if the snake hits the wall
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT):
            print("Game Over! You hit the wall.")
            break

        # Check if the snake eats itself
        if len(snake) != len(set(snake)):
            print("Game Over! You ate yourself.")
            break

if __name__ == "__main__":
    main()
