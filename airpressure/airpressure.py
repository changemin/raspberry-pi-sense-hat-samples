from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
    pressure = sense.get_pressure()
    print(pressure)
    time.sleep(1)