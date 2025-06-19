#!/bin/python3
# MasterMind with color words
# Version with compact feedback (English)
# v2.1 - 2025-06-05

import random
import os

ADMIN_PASS = "Rubensigma69"
print("MasterMind")

valid_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def generate_code(length=4):
    return [random.choice(valid_colors) for _ in range(length)]

def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))

    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(c, 0), guess_counts.get(c, 0)) for c in guess_counts)
    return black_pegs, white_pegs

def show_secret(code):
    print("Secret code:", ' '.join(code))

def play_mastermind():
    print("\nWelcome to Mastermind!")
    print("Try to guess the secret sequence of 4 colors.")
    print("Choose from:", ', '.join(valid_colors))
    print("Use spaces between each color. You have 10 attempts.")
    print("Type 'exit' or 'stop' to quit the game early.")

    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_guess = False
        guess = []

        while not valid_guess:
            user_input = input(f"Attempt {attempt}: ").strip().lower()

            if user_input == "cheat":
                pw = input("Admin password required: ").strip()
                if pw == ADMIN_PASS:
                    show_secret(secret_code)
                else:
                    print("Access denied.")
                continue

            if user_input in ["exit", "stop"]:
                print("Game aborted. See you next time!")
                return

            guess = user_input.split()
            valid_guess = len(guess) == 4 and all(word in valid_colors for word in guess)

            if not valid_guess:
                print(f"Invalid input. Pick 4 colors from: {', '.join(valid_colors)}")

        black, white = get_feedback(secret_code, guess)
        print(f"{black} black peg(s), {white} white peg(s)")

        if black == 4:
            print(f"Congratulations! You cracked the code: {' '.join(secret_code)}")
            return

    print(f"Game over! The correct code was: {' '.join(secret_code)}")

if __name__ == "__main__":
    again = 'y'
    while again.lower() == 'y':
        play_mastermind()
        again = input("Play again? (Y/N): ").strip()

