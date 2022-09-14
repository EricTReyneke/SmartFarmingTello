from djitellopy import Tello
# from threading import Threads
# threads_initialized = False

tello = Tello()
tello.connect()

distance = tello.get_distance_tof()

tello.takeoff()
tello.go_xyz_speed(90, 70, 200, 20)
tello.go_xyz_speed(90, 70, 200, 20)
tello.go_xyz_speed(90, 70, 200, 20)
tello.go_xyz_speed(90, 70, 200, 20)
# tello.go_xyz_speed_mid(100, 100, 70, 10)
tello.land()
tello.get_flight_time()
