# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  it looks as normal game without bugs from first glance.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The Bugs:
[X] the hins is wrong.
[X] the history not working as expected not sync directly with the game.
[X] the message "Guess a number between 1 and 100. Attempts left: 0" is wrong not update with the attempts left and level
[X] "new game" not work after GameOver.
[X] attempts left be negative after moving from level to another.
[] not accept wrong input and show message for that (alphabetic, number above the rage allowed depend on level, negative number)
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  we used Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  For the hint bug, the AI suggested to change the hint logic to compare the guess with the secret number and provide feedback accordingly. In the beginning, the hint logic was not correctly implemented, leading to incorrect hints being displayed. So First we verified the hint logic  see the diffrince between the old code that has the bug and the new code that AI suggested, then we accepted the suggestion and tested the game by making guesses to see if the hints were now accurate. After implementing the AI's suggestion, we found that the hints were now correctly indicating whether the guess was too high, too low, or correct, confirming that the issue was resolved.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
 by testing the game after implementing the fix and observing whether the expected behavior was achieved. For example, after fixing the hint logic, we made several guesses to see if the hints were now accurate. If the hints correctly indicated whether our guesses were too high, too low, or correct, we considered the bug to be fixed. We also checked the game history to ensure that it was now properly syncing with the game state. If the history displayed the correct sequence of guesses and outcomes, we confirmed that the bug was resolved.
 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
