from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
    temp = sense.get_temperature()
    print(temp)
    time.sleep(1)