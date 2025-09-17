import random

def get_computer_choice():
    """Mengembalikan pilihan komputer: rock, paper, atau scissors"""
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player_choice, computer_choice):
    """Menentukan pemenang"""
    if player_choice == computer_choice:
        return "Draw"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "Player"
    else:
        return "Computer"

def play(player_choice):
    """Main 1 ronde dengan input player"""
    player_choice = player_choice.lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        raise ValueError("Pilihan harus 'rock', 'paper', atau 'scissors'")

    computer_choice = get_computer_choice()
    winner = get_winner(player_choice, computer_choice)
    
    return {
        "player": player_choice,
        "computer": computer_choice,
        "winner": winner
    }
