from models import Player


class FootballPlayer(Player):

    def calculate_average(self):
        self.average_score = round(self.speed_score * 0.30 + self.technique_score * 0.40 + self.goal_score * 0.30, 2)
        self.classify_performance()
        return self.average_score

    def classify_performance(self):
        if self.average_score < 5.0:
            self.performance_score_type = "Dự bị yếu"
        elif self.average_score < 6.5:
            self.performance_score_type = "Trung bình"
        elif self.average_score < 8.0:
            self.performance_score_type = "Tốt"
        else:
            self.performance_score_type = "Ngôi sao"
        return self.performance_score_type


class PlayerManager:

    def __init__(self):
        self._players: list[FootballPlayer] = []

    def id_exists(self, player_id: int):
        return self.find_by_id(player_id) is not None

    def add_player(self, player_id: int, name: str,
                   speed: float, technique: float, goal: float):
        player = FootballPlayer(player_id, name, speed, technique, goal)
        player.calculate_average()
        self._players.append(player)
        return player

    def get_all(self):
        return list(self._players)

    def find_by_id(self, player_id: int):
        for p in self._players:
            if p.id == player_id:
                return p
        return None

    def update_player(self, player_id: int,
                      name: str | None = None,
                      speed: float | None = None,
                      technique: float | None = None,
                      goal: float | None = None) -> bool:
        player = self.find_by_id(player_id)
        if player is None:
            return False
        if name is not None:
            player.name = name
        if speed is not None:
            player.speed_score = speed
        if technique is not None:
            player.technique_score = technique
        if goal is not None:
            player.goal_score = goal
        player.calculate_average()
        return True

    def delete_player(self, player_id: int):
        player = self.find_by_id(player_id)
        if player is None:
            return False
        self._players.remove(player)
        return True

    def search_by_name(self, keyword: str):
        kw = keyword.lower()
        return [p for p in self._players if kw in p.name.lower()]