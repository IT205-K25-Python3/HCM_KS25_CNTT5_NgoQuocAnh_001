from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(
        self,
        player_id: int,
        name: str,
        speed_score: float,
        technique_score: float,
        goal_score: float,
    ):
        self.id = player_id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.average_score: float = 0.0
        self.performance_score_type: str = ""

    @abstractmethod
    def calculate_average(self):
        pass

    @abstractmethod
    def classify_performance(self):
        pass

    def __str__(self):
        return (
            f"[{self.id}] {self.name} | "
            f"Speed: {self.speed_score:.1f} | "
            f"Technique: {self.technique_score:.1f} | "
            f"Goal: {self.goal_score:.1f} | "
            f"Avg: {self.average_score:.2f} | "
            f"Rating: {self.performance_score_type}"
        )
