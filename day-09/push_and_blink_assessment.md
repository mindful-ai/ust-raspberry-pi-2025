# Assessment: Push-and-Blink with Button Press Counter

## 🔧 Title
**Push-and-Blink: Button Press Counter with LED Response**

## 🧩 Objective
Design a Python program using the `gpiozero` library that accomplishes the following:

1. When the program is run:
   - The user can **press a push button** multiple times.
   - The program should **count how many times the button is pressed**.
   - The counting phase ends **when the user holds the button down for 2 seconds continuously**.

2. Once counting ends:
   - An LED should **blink as many times as the number of button presses** detected.

## 🔌 Hardware Setup (on Pioneer600)
- **Push Button**: Connected to **GPIO20**  
- **LED**: Connected to **GPIO26**  

> 📝 Tip: Use pull-up logic; the button is **active low**

---


## 🧪 Notes 
- This exercise tests understanding of:
  - GPIO handling with `gpiozero`
  - State management (press vs. hold)
  - Loops and timing
- You can modify the difficulty by:
  - Replacing time-based hold detection with a second button
  - Adding debounce logic

