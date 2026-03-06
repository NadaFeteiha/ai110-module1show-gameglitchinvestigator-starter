# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  it looks as normal game without bugs from first glance. the game has 3 level and every level has different attempts to guess the secret number.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The Bugs:
[X] the hins is wrong.
[X] the history not working as expected not sync directly with the game.
[X] the message "Guess a number between 1 and 100. Attempts left: 0" is wrong not update with the attempts left and level
[X] "new game" not work after GameOver.
[X] attempts left be negative after moving from level to another.
[X] not accept wrong input and show message for that (alphabetic, number above the rage allowed depend on level, negative number)
[X] new game should reset the input field to empty but it doesn't.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  we used Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  For the hint bug, the AI suggested to change the hint logic to compare the guess with the secret number and provide feedback accordingly. In the beginning, the hint logic was not correctly implemented, leading to incorrect hints being displayed. So First we verified the hint logic  see the diffrince between the old code that has the bug and the new code that AI suggested, then we accepted the suggestion and tested the game by making guesses to see if the hints were now accurate. After implementing the AI's suggestion, we found that the hints were now correctly indicating whether the guess was too high, too low, or correct, confirming that the issue was resolved.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
 i asked to fix the history bug that not display the history of guesses correctly, the AI suggested the code that made the history not appear at all, so we rejected the suggestion and instead we implemented a different fix that involved properly syncing the history with the game state. After implementing our fix, we tested the game by making several guesses and checking the history display to ensure that it now showed the correct sequence of guesses and outcomes, confirming that our fix was successful.

 Also it keep change the ui by adding "Developer Debug Info" tab at the bottom of the page without asking to do that, and that was not what we wanted, so we rejected that suggestion as well and ask do not change the UI.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
 by testing the game after implementing the fix and observing whether the expected behavior was achieved. For example, after fixing the hint logic, we made several guesses to see if the hints were now accurate. If the hints correctly indicated whether our guesses were too high, too low, or correct, we considered the bug to be fixed. We also checked the game history to ensure that it was now properly syncing with the game state. If the history displayed the correct sequence of guesses and outcomes, we confirmed that the bug was resolved.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  the input validation test was one of the tests we ran. We tested the game by entering various invalid inputs, such as alphabetic characters, numbers above the allowed range for the current level, and negative numbers. The expected behavior was that the game would reject these inputs and display an appropriate error message. When we ran this test, we observed that the game correctly identified and rejected invalid inputs, displaying the correct error messages. This showed us that our input validation logic was working as intended and that the game was now more robust against invalid user input.

- Did AI help you design or understand any tests? How?
yes I asked the AI to implement input validation for the game, and it suggested a test case to check if the game correctly handles invalid inputs. The AI provided a specific example of how to test the input validation by entering alphabetic characters, numbers above the allowed range, and negative numbers. This suggestion helped me understand how to design a test that would effectively verify that the input validation logic was working correctly. By following the AI's suggestion, I was able to create a test that confirmed our input validation was functioning as expected.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
how to use git and commit often, and also to test the code after every change to make sure that the change is correct and does not break anything else in the code and also write clear prompts to the AI to get the best suggestions from the beginning and avoid wasting time on wrong suggestions.

  - This could be a testing habit, a prompting strategy, or a way you used Git.
  all of the above.

- What is one thing you would do differently next time you work with AI on a coding task?
to keep commit so i be sure I saved the code before asking the AI for new suggestion, and if the suggestion is wrong I can easily revert to the last commit without losing much work.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
It code be so helpful and save a lot of time or it can be misleading and waste a lot of time  and that depend of clear prompts about what and where change and read the code before accepting the suggestion to make sure it is what I want and not change something else that I don't want to change. also it can be helpful in suggesting test cases that I might not think about, which can improve the quality of my code.