# 🃏 Blackjack (Python Edition)

Welcome to **Blackjack**, the digital drama of risk, reward, and regret — now in your terminal.  
Built in Python by **Unnathi E Naik**, this game tests your luck against a very determined (but very fair) computer dealer.

## 🎮 Gameplay Overview

- You're dealt two cards from a virtual deck.
- The computer also gets two — but sneaky, it only shows one.
- Try to get as close to **21** as possible without going over.
- You can choose to draw another card ("Hit") or stop ("Stand").
- Natural Blackjack (Ace + 10 on first go)? That’s an instant win (unless the computer has it too...).

## 🤖 Dealer Logic

- The computer keeps drawing until its total is 17 or more.
- Aces (11) get smartly converted to 1 if needed — no busting on a technicality.
- Once both you and the dealer are done, scores are compared and the winner is declared.

## 🛠 How to Run

1. Make sure you have:
   - `blackjack.py` (your main file)
   - `art.py` (for logo and goodbye art)
2. Run the game:

```bash
python blackjack.py
```

3. Type `'Y'` to play or `'N'` to exit with dramatic flair.

## 🎯 Features

- 💥 Natural Blackjack detection
- ♠️ Ace auto-adjustment if total exceeds 21
- 🤺 Interactive decision prompts
- 👾 Dealer AI that plays fair and square (but still wants to win)
- 🧠 Built-in score comparison logic
- 🎨 ASCII art for a bit of pizzazz (check `art.py`)

---

🧑‍💻 **Developed by Unnathi E Naik**  
🌱 No caffeine, just pure Python and probability.  
🎲 Good luck — and remember: sometimes, it's better to **stand**.

