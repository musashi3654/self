from vpython import *
import serial
import time
import math

ser = serial.Serial('COM3', 115200, timeout= 1)
time.sleep(1)

scene  = canvas(title = "MPU5060", width =800, heigth = 600)

x_axis = arrow(pos= vector(0 ,0 ,0) , axis = vector(1,0,0), color = color.red)
y_axis = arrow(pos= vector(0 ,0 ,0) , axis = vector(0,1,0), color = color.green)
z_axis = arrow(pos= vector(0 ,0 ,0) , axis = vector(0,0,1), color = color.blue)

cube = box(length=1, height=0.2, width=0.6, color=color.orange)
roll0 =0
yaw0=0
pitch0 = 0
initialized = False


def update_orintatino(roll, pitch ,yaw):
    roll = math.radians(roll)
    yaw = math.radians(yaw)
    pitch = math.radians(pitch)

    axis = vector(math.cos(yaw) * math.cos(pitch),
                  math.sin(pitch),
                  math.sin(yaw) * math.cos(pitch))
    up = vector(-math.cos(yaw) * math.sin(roll) * math.sin(pitch) + math.sin(yaw) * math.cos(roll),
                math.cos(pitch) * math.sin(roll),
                -math.sin(yaw) * math.sin(roll) * math.sin(pitch) - math.cos(yaw) * math.cos(roll))
    





    
    cube.axis = axis
    cube.up = up

while True :
    

    rate(60)
    line = ser.readline().decode('utf-8').strip()
    if (line) :
        try :
            roll, pitch ,yaw = map(float , line.split(','))
            roll_current = roll
            pitch_current = pitch
            yaw_current = yaw
            if not initialized:
                roll0 = roll_current
                pitch0 = pitch_current
                yaw0 = yaw_current
                initialized = True
            roll_rel = roll - roll0
            pitch_rel = pitch - pitch0
            yaw_rel = yaw - yaw0

            update_orintatino(roll_rel, pitch_rel ,yaw_rel)
        except :
            pass

