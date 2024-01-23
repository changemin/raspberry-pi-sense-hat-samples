from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)

while True:
  sense.show_message("Hello World@@@", text_colour=(255,255,255), back_colour=(0,0,0), scroll_speed=0.25)