# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
- [X] Detail which bugs you found.
- [X] Explain what fixes you applied.

## 📸 Demo

- [X] [Insert a screenshot of your fixed, winning game here]
<img width="1275" height="789" alt="Screenshot 2026-03-06 at 1 24 55 AM" src="https://github.com/user-attachments/assets/5e85d584-d59c-4f9c-ba1e-1b5411999906" />
<img width="1275" height="789" alt="Screenshot 2026-03-06 at 1 25 34 AM" src="https://github.com/user-attachments/assets/a54457fa-679a-4a76-909e-23a47c0090ac" />
<img width="1425" height="738" alt="Screenshot 2026-03-06 at 10 20 28 PM" src="https://github.com/user-attachments/assets/5fc5cab1-1b0c-45c9-9dbe-284a0dcfaf66" />

## 🚀 Stretch Features

- [X] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
