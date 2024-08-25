
class RocketError(Exception):
    """Base class for exceptions in this rocket system."""
    pass

class GPIOSetupError(RocketError):
    """Exception raised for errors in GPIO setup."""
    pass

class I2CError(RocketError):
    """Exception raised for errors in I2C communication."""
    pass

class SensorReadError(RocketError):
    """Exception raised when reading sensor data fails."""
    pass

class MotorControlError(RocketError):
    """Exception raised when motor control fails."""
    pass

class ParachuteDeployError(RocketError):
    """Exception raised when parachute deployment fails."""
    pass

class AuthorizationError(RocketError):
    """Exception raised for unauthorized access attempts."""
    pass
