from typing import List, Optional, Any, Dict

class Autopilot:
    def __init__(self, waypoints: List[Any]) -> None:
        self.waypoints: List[Any] = waypoints
        self.current_waypoint: int = 0

    def next_waypoint(self) -> Optional[Any]:
        if self.current_waypoint < len(self.waypoints):
            target: Any = self.waypoints[self.current_waypoint]
            self.current_waypoint += 1
            return target
        return None

    def control(self, sensor_data: Dict[str, Any]) -> None:
        target: Optional[Any] = self.next_waypoint()
        if target:
            pass