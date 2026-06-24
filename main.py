from managers import PlayerManager
from utils import (
    print_header,
    print_player_list,
    input_float,
    input_int,
    input_str,
)

def menu_add_player(manager: PlayerManager):
    print_header("THÊM CẦU THỦ MỚI")

    while True:
        player_id = input_int("  Player ID          : ")
        if manager.id_exists(player_id):
            print(f"Lỗi: ID {player_id} đã tồn tại. Vui lòng nhập ID khác.")
        else:
            break

    name = input_str("Player name    : ")
    speed = input_float("Speed score(0-10) : ")
    technique = input_float("Technique(0-10) : ")
    goal = input_float("Goal score(0-10) : ")

    player = manager.add_player(player_id, name, speed, technique, goal)
    print(f"\nĐã thêm thành công!")
    print(
        f"  Avg: {player.average_score:.2f} | Rating: {player.performance_score_type}"
    )


def menu_show_all(manager: PlayerManager):
    print_header("DANH SÁCH CẦU THỦ")
    print_player_list(manager.get_all())


def menu_search(manager: PlayerManager):
    print_header("TÌM KIẾM CẦU THỦ")
    keyword = input_str("  Nhập tên cần tìm : ")
    results = manager.search_by_name(keyword)
    if results:
        print(f"\nTìm thấy {len(results)} kết quả:")
        print_player_list(results)
    else:
        print(f"Không tìm thấy cầu thủ nào có tên chứa '{keyword}'.")


def menu_update(manager: PlayerManager):
    print_header("CẬP NHẬT CẦU THỦ")
    menu_show_all(manager)

    player_id = input_int("  Nhập ID cần cập nhật : ")
    player = manager.find_by_id(player_id)
    if player is None:
        print(f"Không tìm thấy cầu thủ ID={player_id}.")
        return

    print(f"\nĐang cập nhật: {player.name}")
    print("  (Nhấn Enter để giữ nguyên giá trị cũ)\n")

    raw_name = input(f"  Name [{player.name}]: ").strip()
    name = raw_name if raw_name else None

    def optional_float(prompt: str, current: float):
        raw = input(f"  {prompt} [{current:.1f}]: ").strip()
        if not raw:
            return None
        try:
            val = float(raw)
            if 0.0 <= val <= 10.0:
                return val
            print("Lỗi: Giá trị ngoài khoảng, giữ nguyên.")
        except ValueError:
            print("Lỗi: Không hợp lệ, giữ nguyên.")
        return None

    speed = optional_float("Speed score  (0-10)", player.speed_score)
    technique = optional_float("Technique    (0-10)", player.technique_score)
    goal = optional_float("Goal score   (0-10)", player.goal_score)

    manager.update_player(
        player_id, name=name, speed=speed, technique=technique, goal=goal
    )
    updated = manager.find_by_id(player_id)
    print(f"\nCập nhật thành công!")
    print(
        f"  Avg: {updated.average_score:.2f} | Rating: {updated.performance_score_type}"
    )


def menu_delete(manager: PlayerManager):
    print_header("XÓA CẦU THỦ")
    menu_show_all(manager)

    player_id = input_int("  Nhập ID cần xóa : ")
    player = manager.find_by_id(player_id)
    if player is None:
        print(f"Không tìm thấy cầu thủ ID={player_id}.")
        return

    confirm = input(f"  Xác nhận xóa '{player.name}'? (y/n): ").strip().lower()
    if confirm == "y":
        manager.delete_player(player_id)
        print(f"Đã xóa cầu thủ '{player.name}'.")
    else:
        print("  Hủy thao tác.")


def show_menu():
    print("===MENU===")
    print("  1. Thêm cầu thủ")
    print("  2. Xem tất cả cầu thủ")
    print("  3. Tìm kiếm cầu thủ")
    print("  4. Cập nhật cầu thủ")
    print("  5. Xóa cầu thủ")
    print("  6. Thoát")



def main():
    manager = PlayerManager()

    while True:
        show_menu()
        choice = input("  Chọn chức năng: ").strip()

        match choice:
            case "1":
                menu_add_player(manager)
            case "2":
                menu_show_all(manager)
            case "3":
                menu_search(manager)
            case "4":
                menu_update(manager)
            case "5":
                menu_delete(manager)
            case "6":
                print("\n Cảm ơn bạn đã sử dụng chương trình bóng đái!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
