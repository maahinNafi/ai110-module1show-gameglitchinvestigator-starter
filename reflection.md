# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  Game looked completely normal at first. 
  Bugs were that the higher and lower does not work as intended. I guessed 5, it said go higher. I guessed 6 it said go lower. While, the number was 41 all along.
  When clicking New Game. The game over is still continuously displayed.
  Attempts left is glitchy and somehow reached 8 from 5 when trying to rapidly click new game.
  The game does not allow you to play a new game at all.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT to give me a prototype of the architect and then used Claude to fix any bugs. One error in the code that Calude suggested to fix was comparing int to int instead of string to int. 
When I initially used ChatGPT for the fix it barely fixed the code and moved around the layout of the whole website.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed if I ran python -m streamlit run app.py and manually tested if the intended fix worked.
One manual test I ran was checking to see if the logic behind restarting the game actually worked.
Yes AI helped in understanding the test by aiding in putting inline comments to show what fixes actually worked.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The original code ran random.randint(low, high) with no protectition so every rerun ran a brand new secret number.
Everytime Steamlit reruns it wipes everything clean, however a session state acts like a cookie remembering the secret, the score, and the attempts.
By generating a new secret if one does not already exist.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I definetely want to get more comfortable with Claude and resuse it in helping me build more scalable projects.
One thing I want to do differently is using Claude within VSCode instead of on the browser.
This project showed me how capable AI is in coding now. 