import random

def player(prev_play, opponent_history=[]):
    # Simpan history langkah lawan
    if prev_play != "":
        opponent_history.append(prev_play)

    # Kalau history masih kosong → pilih random
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # Strategi sederhana:
    # Prediksi lawan akan mengulang langkah terakhirnya
    # Jadi kita pilih langkah yang mengalahkan langkah terakhir lawan
    last_move = opponent_history[-1]

    counter_moves = {
        "R": "P",  # kertas menang lawan batu
        "P": "S",  # gunting menang lawan kertas
        "S": "R"   # batu menang lawan gunting
    }

    return counter_moves[last_move]
