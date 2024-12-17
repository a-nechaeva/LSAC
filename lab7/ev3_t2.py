#!/usr/bin/env python3
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply
import time
import os
import shutil

# Класс для получения данных о заряде батареи
volts = PowerSupply()
# Класс для взаимодействия с двигателем
motorA = LargeMotor('outA')

def goal(V, t):
    return V * t

V = 2
k = 0.5

try:
    # Сохраняем начальное время
    start_time = time.time()
    # Сохраняем начальную позицию
    start_pos = motorA.position
    # В течение двух секунд записываем в файл данные в формате: <time,angle,speed>
    while (time.time() - start_time) < 30:
        g = goal(V, t=time.time() - start_time)
        U = k * (motorA.position - g) * 100
        U = min(abs(U), 100) * (U / abs(U))
        motorA.run_direct(duty_cycle_sp=U)
        print(str(time.time() - start_time) + ',' + str(motorA.position - start_pos) + ',' + str(- g + (motorA.position - start_pos)))
    # Останавливаем мотор
    motorA.run_direct(duty_cycle_sp=0)
    time.sleep(1)
except Exception as e:
    raise e
finally:
    # Останавливаем мотор в случае ошибок в коде
    motorA.stop(stop_action='brake')
