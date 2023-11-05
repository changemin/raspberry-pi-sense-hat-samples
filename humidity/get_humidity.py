from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
    humidity = sense.get_humidity()
    print(humidity)
    time.sleep(1)