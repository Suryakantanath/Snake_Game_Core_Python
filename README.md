# Snake Game

## **Description**
This is a simple text-based snake game built in Python. The game is rendered inside the terminal, with a snake represented as a growing line of dots (`.`) and food represented as single dots (`.`). The player controls the snake using keyboard inputs (`W`, `A`, `S`, `D` keys).

The objective of the game is to eat as much food as possible, which increases the length of the snake. The game ends if the snake hits its own body or the boundary walls.

---

## **Features**
- **Dynamic gameplay**: The snake moves in real-time.
- **Keyboard control**: Use `W`, `A`, `S`, `D` keys to control the snake's movement.
- **Score tracking**: The length of the snake reflects the score.
- **Randomized food**: Food appears randomly within the game boundaries.
- **Collision detection**: Game ends on hitting the boundaries or the snake's body.

---

## **How to Play**
1. **Run the Game**:
   - Ensure you have Python installed on your system.
   - Run the script using the command:
     ```
     python snake_game.py
     ```

2. **Game Controls**:
   - `W`: Move up
   - `A`: Move left
   - `S`: Move down
   - `D`: Move right

3. **Objective**:
   - Control the snake to eat the randomly appearing food.
   - Avoid colliding with the walls or your own body.

4. **Game Over**:
   - The game ends when the snake hits the boundary or itself.
   - To restart, simply re-run the script.

---

## **Requirements**
- Python 3.6 or later
- Cross-platform compatibility (Windows, macOS, Linux)

---

## **Code Structure**
### **Functions**
1. **`clear_screen()`**:
   - Clears the terminal screen for each frame of the game.

2. **`draw_boundary(height, width)`**:
   - Creates the boundary for the game using `|` and `-`.

3. **`print_game(snake, food, height, width)`**:
   - Renders the current state of the game in the terminal.

4. **`main()`**:
   - Initializes the game loop and handles the gameplay logic.

### **Game Logic**
- The snake's position is tracked as a list of coordinates.
- The game checks for collisions at each step:
  - **Wall collision**: If the snake's head touches the boundary.
  - **Self-collision**: If the snake's head overlaps with its body.
- When food is eaten:
  - The snake grows longer.
  - A new piece of food is randomly placed within the boundary.

---

## **Customization Options**
1. **Adjust Game Area**:
   - Modify the `height` and `width` variables in the `main()` function to change the game dimensions.

2. **Game Speed**:
   - Adjust the `time.sleep(0.2)` value to increase or decrease the snake's speed.

3. **Food Symbol**:
   - Change the food symbol by modifying the `'.'` character in the `print_game()` function.

---

## **Future Enhancements**
- Add difficulty levels with varying speeds.
- Implement a scoring system displayed in real-time.
- Add colorful outputs to improve visual appeal.

---

## **License**
This project is open-source and available under the MIT License.

---

## **Author**
Developed by a Python enthusiast using basic text-based logic to simulate a nostalgic snake game. Feel free to contribute and improve!

