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
kp = 3
ki = 2

try:
    # Сохраняем начальное время
    start_time = time.time()
    # Сохраняем начальную позицию
    start_pos = motorA.position
    # Интегральная ошибка
    integral_error = 0

    # В течение двух секунд записываем в файл данные в формате: <time,angle,speed>
    while (time.time() - start_time) < 2:
        # Вычисляем ошибку
        error = motorA.position - start_pos - goal(V, t=time.time()-start_time)

        # Обновляем интегральную ошибку
        integral_error += error * (time.time() - start_time)

        # Вычисляем управляющее воздействие ПИ-регулятора
        reg = kp * error + ki * integral_error

        # Ограничиваем управляющий сигнал в диапазоне [-100, 100]
        U = max(min(reg, 100), -100)

        # Управление мотором
        motorA.run_direct(duty_cycle_sp=U)

        # Печать текущих значений
        print(str(time.time() - start_time) + ',' + str(motorA.position - start_pos) + ',' + str(-goal(V, t=time.time()-start_time) + (motorA.position - start_pos)))

    # Останавливаем мотор
    motorA.run_direct(duty_cycle_sp=0)
    time.sleep(1)
except Exception as e:
    raise e
finally:
    # Останавливаем мотор в случае ошибок в коде
    motorA.stop(stop_action='brake')
