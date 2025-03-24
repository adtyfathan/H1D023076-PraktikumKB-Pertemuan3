import numpy as np
import random

choices = {
    "batu": "gunting", 
    "gunting": "kertas", 
    "kertas": "batu"
}

ascii_art_player = {
    "batu": """
    _______
---'   ____)    
      (_____)
      (_____)
      (____) 
---.__(___)

    Batu
    """,
    "kertas": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

    Kertas
    """,
    "gunting": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    Gunting
    """
}

ascii_art_computer = {
    "batu": """
       _______
      (____   '---
      (_____)
      (_____)
       (____)
        (___)__.---

           Batu
    """,
    "kertas": """
        _______
  ____(____   '----
 (______
 (_______
  (_______
    (_________.---

           Kertas
    """,
    "gunting": """
       _______
  ____(____   '---
 (______
 (__________
      (____)
       (___)__.---

           Gunting
    """
}

def get_computer_choice():
    return random.choice(list(choices.keys()))

def determine_winner(player, computer):
    if player == computer:
        return f"Seri! Keduanya memilih {player}."
    elif choices[player] == computer:
        return f"Kamu menang! {player.capitalize()} mengalahkan {computer}.\n"
    else:
        return f"Kamu kalah! {computer.capitalize()} mengalahkan {player}.\n"

def display_score(scores):
    print("          Skor Permainan")
    print("===================================")
    print(f"Menang: {scores[0]}, Kalah: {scores[1]}, Seri: {scores[2]}")
    print("===================================")

def main():
    scores = np.array([0, 0, 0]) 
    round_number = 1

    while True:
        print("Babak", round_number)
        print("1. Batu")
        print("2. Gunting")
        print("3. Kertas")
        player_choice = input("Ayo pilih apa bro (batu/gunting/kertas) atau 'keluar' : ").lower()
        if player_choice == "keluar":
            print("Terima kasih sudah bermain!")
            display_score(scores)
            break
        elif player_choice not in choices:
            print("Pilihan tidak valid. Coba lagi.")
            continue
        
        computer_choice = get_computer_choice()
        print("\nPilihanmu:")
        print(ascii_art_player[player_choice])
        print("\nKomputer memilih:")
        print(ascii_art_computer[computer_choice])
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if "menang" in result:
            scores[0] += 1
        elif "kalah" in result:
            scores[1] += 1
        else:
            scores[2] += 1
        
        display_score(scores)
        round_number += 1
        print("\n")

if __name__ == "__main__":
    main()
