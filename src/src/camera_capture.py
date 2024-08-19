from picamera import PiCamera
from time import sleep
import os

class RocketCamera:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1920, 1080)
        self.camera.framerate = 30
        self.output_dir = "rocket_footage"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def start_recording(self, duration=60):
        try:
            file_path = os.path.join(self.output_dir, "launch_footage.h264")
            self.camera.start_recording(file_path)
            sleep(duration)
            self.camera.stop_recording()
        except Exception as e:
            print(f"Error during camera operation: {e}")
        finally:
            self.camera.close()

if __name__ == "__main__":
    rocket_cam = RocketCamera()
    rocket_cam.start_recording(duration=120)
