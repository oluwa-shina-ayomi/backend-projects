### number guessing game

a simple cli number guessing game built with python.
you try to guess a random number between 1 and 100 within a set number of attempts.
the game includes different difficulty levels, tracks how long it took you to guess right, and lets you keep playing until you decide to stop.

---

### features

* 3 difficulty levels (easy, medium, hard)
* built-in timer that tracks elapsed time
* option to keep playing after each round
* handles invalid inputs cleanly

---

### requirements

* python 3.7 or higher

---

### how to run

```bash
git clone <repo-link>
cd number-guessing-game
python guess.py
```

---

### example walkthrough

```bash
welcome to the number guessing game
i'm thinking of a number between 1 and 100

please select a difficulty level
1. easy (10 chances)
2. medium (5 chances)
3. hard (3 chances)

enter your choice (level 1, 2 or 3): 1

great you have selected the easy difficulty level
let's start the game

enter your guess: 45
incorrect the number is greater than 45

enter your guess: 68
incorrect the number is less than 68

enter your guess: 59
congratulations you guessed the correct number in 3 attempts
elapsed time: 0h 0m 22.13s

wanna keep playing, yes or no? no
byeeeeeee
```

---

### note

this is just a practice project, thi main thing i learned here was how to implement a timer and covert it to a readable format

### project url
<https://roadmap.sh/projects/number-guessing-game>
