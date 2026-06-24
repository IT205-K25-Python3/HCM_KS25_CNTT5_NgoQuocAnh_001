def input_float(prompt: str, min_val: float = 0.0, max_val: float = 10.0):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Vui lòng nhập giá trị từ {min_val} đến {max_val}.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập số.")


def input_int(prompt: str, min_val: int = 1):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            print(f"Vui lòng nhập số nguyên >= {min_val}.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập số nguyên.")


def input_str(prompt: str):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Không được để trống.")



def print_header(title: str):
    print(f"{title}")


def print_player_list(players):
    if not players:
        print("Lỗi: Không có cầu thủ nào")
        return
    print(f"  {'ID':<5} {'Name':<20} {'Speed':>7} {'Tech':>7} {'Goal':>7} {'Avg':>6}  Rating")

    for p in players:
        print(
            f"  {p.id:<5} {p.name:<20} "
            f"{p.speed_score:>7.1f} {p.technique_score:>7.1f} "
            f"{p.goal_score:>7.1f} {p.average_score:>6.2f}  "
            f"{p.performance_score_type}"
        )
