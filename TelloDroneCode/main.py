from djitellopy import Tello
# from threading import Threads
# threads_initialized = False
import time

tello = Tello()
tello.connect()

#distance = tello.get_distance_tof()

print(tello.get_battery())

tello.takeoff()
time.sleep(5)
# tello.go_xyz_speed(90, 70, 200, 20)
# tello.go_xyz_speed(90, 70, 200, 20)
# tello.go_xyz_speed(90, 70, 200, 20)
# tello.go_xyz_speed(90, 70, 200, 20)
# tello.go_xyz_speed_mid(100, 100, 70, 10)
tello.send_rc_control(10,0,0,0)
# time.sleep(5)
tello.send_rc_control(0,0,0,0)
time.sleep(5)
tello.send_rc_control(-10,0,0,0)
# time.sleep(5)
tello.send_rc_control(0,-0,0,0)
time.sleep(5)




tello.land()
tello.get_flight_time()



