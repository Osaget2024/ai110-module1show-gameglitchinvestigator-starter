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

**Purpose:** a Streamlit number-guessing game. Pick a difficulty, guess the secret number, and get Higher/Lower hints within a limited number of attempts. Score rewards early wins and penalizes wrong guesses.

**Bugs found**
- Hints were backwards ("Go HIGHER!" for a guess that was too high).
- The secret was turned into a string on even attempts, so comparisons were string-based and wrong.
- The secret regenerated or was ignored by New Game: it always used 1-100, and did not reset status, score or history.
- Attempts started at 1, so the counter was off by one; invalid input also used up an attempt.
- The info banner always said 1-100, whatever the difficulty.
- Hard (1-50) was easier than Normal (1-100).
- Scoring gave +5 for a "Too High" guess on even attempts, and win points used `attempt_number + 1`.

**Fixes applied**
- Moved all logic into `logic_utils.py` (`get_range_for_difficulty`, `get_attempt_limit`, `parse_guess`, `check_guess`, `update_score`).
- Corrected hints, kept the secret an int, and stored game state in `st.session_state` via `start_new_game()`.
- `parse_guess` now validates the range; invalid input doesn't cost an attempt.
- Hard is now 1-200 with 6 attempts; Easy 1-20 / 8; Normal 1-100 / 7.
- Wrong guesses always cost 5 points; wins score `100 - 10*attempt` (min 10).

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py`; choose a difficulty in the sidebar (the range and attempt limit shown update).
2. Type a guess and click **Submit Guess**; a wrong guess shows the correct Higher/Lower hint and the attempts-left counter drops by one.
3. Enter text or an out-of-range number: an error appears and no attempt is used.
4. Keep guessing; the secret stays the same between clicks (see Developer Debug Info).
5. Guess correctly to win (balloons and score), or run out of attempts to lose; **New Game** resets everything for the current difficulty.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
9 passed, 0 failed   (tests/test_game_logic.py)

Note: I ran these with a small stand-in runner because pytest could not be
installed in my sandbox. Please run `pytest` locally and paste the real
output here.
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
