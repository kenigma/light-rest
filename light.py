import RPi.GPIO as GPIO

RELAIS_1_GPIO = 15

def get(action):
  GPIO.setmode(GPIO.BOARD) # GPIO Numbers instead of board numbers
  GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
  if action == "on":
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
  else:
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # off
  print("Incoming action is: {}".format(action))
