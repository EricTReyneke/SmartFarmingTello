# from djitellopy import Tello
# # from threading import Threads
# # threads_initialized = False
# import time
#
# tello = Tello()
# tello.connect()
#
# def TellFly():
#     # distance = tello.get_distance_tof()
#
#     print(tello.get_battery())
#
#     tello.takeoff()
#     time.sleep(5)
#     # tello.go_xyz_speed(90, 70, 200, 20)
#     # tello.go_xyz_speed(90, 70, 200, 20)
#     # tello.go_xyz_speed(90, 70, 200, 20)
#     # tello.go_xyz_speed(90, 70, 200, 20)
#     # tello.go_xyz_speed_mid(100, 100, 70, 10)
#     tello.send_rc_control(10, 0, 0, 0)
#     # time.sleep(5)
#     tello.send_rc_control(0, 0, 0, 0)
#     time.sleep(5)
#     tello.send_rc_control(-10, 0, 0, 0)
#     # time.sleep(5)
#     tello.send_rc_control(0, -0, 0, 0)
#     time.sleep(5)
#     tello.land()
#     tello.get_flight_time()


import mysql
import mysql.connector
from mysql.connector import Error

def Connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='prj381_group20',
                                         user='root',
                                         password='')

    sql_select_Query = "select Status from Route"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    checkFly = records[0]

    for rows in records:
        checkFly = rows["Status"]

Connection()