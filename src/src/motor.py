class Motor:
    def __init__(self, power_hp, torque_nm, efficiency_percent, weight_kg):
        self.power_hp = power_hp
        self.torque_nm = torque_nm
        self.efficiency_percent = efficiency_percent
        self.weight_kg = weight_kg

    def set_power(self, new_power_hp):
        self.power_hp = new_power_hp

    def set_torque(self, new_torque_nm):
        self.torque_nm = new_torque_nm

    def set_efficiency(self, new_efficiency_percent):
        self.efficiency_percent = new_efficiency_percent

    def set_weight(self, new_weight_kg):
        self.weight_kg = new_weight_kg

    def get_stats(self):
        return {
            "Power": f"{self.power_hp} HP",
            "Torque": f"{self.torque_nm} Nm",
            "Efficiency": f"{self.efficiency_percent}%",
            "Weight": f"{self.weight_kg} kg"
        }
