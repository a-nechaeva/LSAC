#!/usr/bin/env python3
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply
import time
import os
import shutil
import math

omega = 1
A = 1
A2 = 2
A3 = 3
omega2 = 4
omega3 = 5

def input(t):
    return A2 * math.cos(omega2 * t) + A3*math.sin(omega3 * t)

# Класс для получения данных о заряде батареи
volts = PowerSupply()
# Класс для взаимодействия с двигателем
motorA = LargeMotor('outA')

start_time = time.time()
start_pos = motorA.position

try:
    while (time.time() - start_time) < 2:
        U = input(time.time() - start_time) * 100
        U = min(abs(U), 100) * (U / abs(U))
        motorA.run_direct(duty_cycle_sp=U)
        print(str(time.time() - start_time) + ',' + str(motorA.position - start_pos) + ',' + str(motorA.speed))
        print(U)
    # Останавливаем мотор
    motorA.run_direct(duty_cycle_sp=0)
    time.sleep(1)
except Exception as e:
    raise e
finally:
    # Останавливаем мотор в случае ошибок в коде
    motorA.stop(stop_action='brake')

