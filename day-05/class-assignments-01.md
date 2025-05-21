# 🧠 Assessment Problem: Build a "Guess My Number" Game using Tkinter

## 🎯 Objective

Design and develop a simple **"Guess My Number"** game using **Python's Tkinter library**. The game should allow the player to guess a randomly generated number between 1 and 100. The game must provide feedback for each guess (Too high, Too low, Correct!) and maintain a guess count. 

The project should emphasize:
- **Tkinter-based GUI**
- **Separation of game logic and GUI**
- **Integration through a main script**

---

## 📁 Project Structure

Your submission must follow this structure:

guess_my_number/<br>
├── game_logic.py # Contains the core game logic<br>
├── gui.py # Contains the Tkinter GUI components<br>
└── main.py # Integrates the logic and GUI<br>


---

## 📜 Functional Requirements

### 1. Game Logic (`game_logic.py`)
- Generate a random number between 1 and 100.
- Accept a user's guess and return:
  - `"Too high"` if the guess is greater.
  - `"Too low"` if the guess is smaller.
  - `"Correct!"` if the guess matches.
- Keep track of the number of guesses.
- Provide a method to reset the game.

### 2. GUI (`gui.py`)
- Use **Tkinter** to design the interface.
- GUI should contain:
  - A label for instructions.
  - An entry widget for the user's guess.
  - A button to submit the guess.
  - A label to display feedback (Too high/Too low/Correct).
  - A label to show the number of attempts.
  - A "New Game" button to restart.
- GUI should **not contain any game logic**.

### 3. Integration (`main.py`)
- Import and initialize the GUI and game logic.
- Ensure all interactions (submit guess, reset) work via the GUI.

---

## ✅ Evaluation Criteria

| Criteria                          | Weightage |
|----------------------------------|-----------|
| Functionality (all features work)| 30%       |
| Proper logic/GUI separation      | 20%       |
| Code readability & structure     | 20%       |
| Usability of GUI                 | 15%       |
| Extra features (e.g. difficulty levels, guess history) | 15% |

---

## 🔧 Bonus Suggestions

- Add a dropdown to choose difficulty (Easy: 1–50, Hard: 1–200).
- Show guess history in the GUI.
- Add sound effects for correct/incorrect guesses.

---

## 📝 Submission

Please submit your zipped project folder containing:
- `game_logic.py`
- `gui.py`
- `main.py`

Include a `README.md` explaining how to run the project.

---

## 💡 Hints

- Use `random.randint()` to generate the number.
- Use `tk.Label()`, `tk.Entry()`, `tk.Button()` for GUI components.
- Use `.config()` to update text on widgets dynamically.

---

Good luck! 🎮
