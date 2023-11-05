from sense_hat import SenseHat
import time

sense = SenseHat()

interval = 1

red = (255, 0, 0)
shaked_time = time.time()
lights_on = False
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        shaked_time = time.time()
        lights_on = True
    
    if time.time() - shaked_time >= 2:
        lights_on = False

    if lights_on:
        sense.show_letter("!", red)

    else:
        sense.clear()