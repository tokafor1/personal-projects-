# 🎮 Tactego — A Turn-Based Strategy Board Game (Python)

Tactego is a strategic two-player board game inspired by the mechanics of *Stratego*.  
Players start with hidden piece placements, then take turns moving units across the board to outmaneuver and eliminate the opponent — with the ultimate goal of capturing their **Flag**.

This project demonstrates **object-oriented problem solving, board data modeling, user interaction handling, and game logic implementation in Python.**  
It was built as part of a larger effort to strengthen strategic programming and algorithmic reasoning.

---

## 🧠 Core Skills Demonstrated
| Skill Area | Explanation |
|-----------|-------------|
| **Python Programming** | Control flow, input handling, data structures, modular functions |
| **Game Logic Design** | Turn-taking, movement rules, piece interaction logic |
| **Data Modeling** | Use of nested lists to represent a mutable 2D game board |
| **Randomization** | Randomized piece distribution for replay value |
| **Clean Code Structure** | Separation of concerns into reusable functions |

---

## 🪖 Game Overview
Each player (Red & Blue) receives a set of units — such as:

| Piece | Meaning | Example Role |
|------|---------|--------------|
| A | Assassin | Eliminates opposing units |
| M | Mine | Traps enemies that step on it |
| S | Sapper | Useful for clearing mines |
| F | Flag | Must be protected; losing it ends the game |

Pieces are placed automatically and hidden from the opponent's knowledge at the start.

Players then alternate choosing coordinates to **move a piece** to a new location on the board.

---

## 🎯 Objective
**Capture the opponent’s Flag.**  
If your flag is taken — the game ends.

---

## 🕹️ How to Run the Game

```bash
python tactego.py
