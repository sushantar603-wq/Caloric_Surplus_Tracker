#  Caloric Surplus Tracker

##  Project Overview
The **Caloric Surplus Tracker** is a lightweight, command-line Python application designed for individuals focusing on healthy weight gain and muscle building. 

While most commercial fitness apps are bloated with ads, require subscriptions, and are heavily geared toward weight loss, this tool provides a fast, distraction-free way to log daily food intake, track protein, and ensure you are consistently hitting a daily caloric surplus. 

This project was developed as a Bring Your Own Project (BYOP) capstone to demonstrate the practical application of core Python concepts like data persistence, file I/O operations, and CLI logic.

##  Features
* **Daily Meal Logging:** Quickly input food items, calorie counts, and protein amounts.
* **Persistent Data Storage:** Uses Python's built-in `json` module to save your data locally. Records are not lost when the application closes.
* **Goal Tracking:** Automatically calculates total daily intake against a predefined surplus goal (e.g., 2800 kcal) and calculates exactly how much more is needed to hit the target.
* **Error Handling:** Built-in validation ensures the program doesn't crash if text is entered instead of numbers.
* **No External Dependencies:** Built entirely using Python's standard library. 

##  How to Set Up
Someone who has never seen this project can easily run it by following these steps:

1. **Prerequisites:** Ensure you have Python 3.x installed on your system.
2. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPO_LINK_HERE>
   cd caloric-surplus-tracker
