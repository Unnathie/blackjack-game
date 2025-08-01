# 🃏 Blackjack Game

Welcome to Blackjack the chaotic cousin of math and luck.  
This is a Python terminal game where you go head-to-head with the computer in a battle of 21.

## 🎮 How It Works

- You're dealt 2 cards. The computer gets 2 too (but only one is shown).
- Cards range from 2 to 11 (Ace can be 1 or 11).
- You choose to "Hit" (draw another card) or "Stand" (stop drawing).
- The goal? Get as close to 21 as possible without busting.
- Natural Blackjack (Ace + 10 card on first draw)? You instantly win. Or lose. Depends who has it.

### 🤖 Dealer Logic
- The computer keeps drawing until its score is at least 17.
- If it busts, you win.
- If not, whoever has the higher score wins.
- Ties are… well… ties.

## 🛠️ How to Play

1. Clone or download the repo.
2. Make sure `art.py` (with ASCII art) is in the same folder.
3. Run:

```bash
python blackjack.py
```

4. Follow the prompts. Make bold choices. Blame the code.

## 💡 Highlights

- Automatic Ace adjustment (Ace = 1 if you go over 21)
- Win/lose messages full of drama
- No money involved. Just pride.

---

🧑‍💻 **Made with logic and luck by Unnathi E Naik**  
🎲 Have fun, and may the cards treat you better than your last math test.
