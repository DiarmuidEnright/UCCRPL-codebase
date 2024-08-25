from picamera import PiCamera
from time import sleep
import os
from typing import Optional
from settings import CAMERA_RESOLUTION, CAMERA_FRAMERATE, OUTPUT_DIR, RECORDING_DURATION

class RocketCamera:
    def __init__(self) -> None:
        self.camera: PiCamera = PiCamera()
        self.camera.resolution = CAMERA_RESOLUTION
        self.camera.framerate = CAMERA_FRAMERATE
        self.output_dir: str = OUTPUT_DIR
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def start_recording(self, duration: Optional[int] = RECORDING_DURATION) -> None:
        try:
            file_path: str = os.path.join(self.output_dir, "launch_footage.h264")
            self.camera.start_recording(file_path)
            sleep(duration)
            self.camera.stop_recording()
        except Exception as e:
            print(f"Error during camera operation: {e}")
        finally:
            self.camera.close()

if __name__ == "__main__":
    rocket_cam: RocketCamera = RocketCamera()
    rocket_cam.start_recording(duration=120)
