#Moves a stepper motor for 1 seconds
import RoboPiLib_pwm as RPL
import setup
import time

pul_pin = 1
dir_pin = 2

#direction can equal 0 or 1 for forwards or backwards
direction = 0
#The smaller the speed, the faster the rotation
speed = 500

RPL.pinMode(pul_pin,RPL.PWM)
RPL.pinMode(direction_pin,RPL.OUTPUT)

RPL.digitalWrite(dir_pin,direction)
RPL.pwmWrite(pul_pin,speed,speed * 2)

time.sleep(1)
RPL.pwmWrite(pul_pin,0,0)
