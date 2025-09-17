import RPS_game

def main():
    print("=== Rock Paper Scissors Game ===")
    while True:
        player_choice = input("Pilih (rock, paper, scissors) atau 'q' untuk keluar: ").lower()
        if player_choice == "q":
            print("Terima kasih sudah bermain!")
            break
        try:
            result = RPS_game.play(player_choice)
            print(f"Kamu pilih: {result['player']}")
            print(f"Komputer pilih: {result['computer']}")
            print(f"Pemenang: {result['winner']}\n")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
