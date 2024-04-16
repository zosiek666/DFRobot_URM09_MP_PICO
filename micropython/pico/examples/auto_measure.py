from time import sleep
from DFRobot_URM09 import DFRobot_URM09
SDA_PIN = 16
SCL_PIN = 17
URM09 = DFRobot_URM09(SDA_PIN,SCL_PIN)

def setup():
  URM09.set_mode_range(URM09.MEASURE_RANG_500, URM09.MEASURE_MODE_AUTOMATIC)


def loop():
  sleep(0.1)
  #Read distance register
  dist = URM09.get_distance()
  #Read temperature register
  temp = URM09.get_temperature()
  print("Distance is %d cm         " %dist)
  print("Temperature is %.2f .c    " %temp)
  sleep(0.1)

if __name__ == "__main__":
  setup()
  while True:
    loop()