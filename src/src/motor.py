from typing import Dict

class Motor:
    def __init__(self, power_hp: float, torque_nm: float, efficiency_percent: float, weight_kg: float) -> None:
        self.power_hp: float = power_hp
        self.torque_nm: float = torque_nm
        self.efficiency_percent: float = efficiency_percent
        self.weight_kg: float = weight_kg

    def set_power(self, new_power_hp: float) -> None:
        self.power_hp = new_power_hp

    def set_torque(self, new_torque_nm: float) -> None:
        self.torque_nm = new_torque_nm

    def set_efficiency(self, new_efficiency_percent: float) -> None:
        self.efficiency_percent = new_efficiency_percent

    def set_weight(self, new_weight_kg: float) -> None:
        self.weight_kg = new_weight_kg

    def get_stats(self) -> Dict[str, str]:
        return {
            "Power": f"{self.power_hp} HP",
            "Torque": f"{self.torque_nm} Nm",
            "Efficiency": f"{self.efficiency_percent}%",
            "Weight": f"{self.weight_kg} kg"
        }
