from djitellopy import Tello, Tello, BackgroundFrameRead
import threading
threads_initialized = False

tello = Tello()
tello.connect()

tello.takeoff()
tello.land()