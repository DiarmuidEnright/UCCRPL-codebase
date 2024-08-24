from typing import Tuple

class ReturnToHome:
    def __init__(self, home_coordinates: Tuple[float, float]) -> None:
        self.home_coordinates: Tuple[float, float] = home_coordinates

    def calculate_vector(self, current_coordinates: Tuple[float, float]) -> Tuple[float, float]: 
        pass

    def execute(self, current_coordinates: Tuple[float, float]) -> None:
        vector: Tuple[float, float] = self.calculate_vector(current_coordinates)
        pass
