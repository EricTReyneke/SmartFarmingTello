from djitellopy import Tello

tello = Tello()
tello.connect()

#distance = Tello.get_distance_tof()

tello.takeoff()

x = 4

for i in x:
    def curve_xyz_speed(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int):
        x1: 90
        x2: 100
        y1: 70
        y2: 80
        z1: 200
        z2: 210
        speed: 20

        cmd = 'curve {} {} {} {} {} {} {}'.format(x1, y1, z1, x2, y2, z2, speed)
        self.send_control_command(cmd)


tello.land()
