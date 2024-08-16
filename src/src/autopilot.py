class Autopilot:
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.current_waypoint = 0

    def next_waypoint(self):
        if self.current_waypoint < len(self.waypoints):
            target = self.waypoints[self.current_waypoint]
            self.current_waypoint += 1
            return target
        return None

    def control(self, sensor_data):
        target = self.next_waypoint()
        if target:
            pass
