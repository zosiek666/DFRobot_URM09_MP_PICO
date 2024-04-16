from time import sleep
from DFRobot_URM09 import DFRobot_URM09
SDA_PIN = 16
SCL_PIN = 17
URM09 = DFRobot_URM09(SDA_PIN,SCL_PIN)

def setup():
  address = URM09.get_device_number()
  print("The old device address for i2c is at %#x" %address)
  sleep(0.1)
  #Change the device number of i2c, value range 1 to 127
  URM09.modify_device_number(0x11)
  sleep(0.1)
  address = URM09.get_device_number()
  print("The new device address for i2c is at %#x" %address)
  print("The new address needs to be powered off and reconnected to take effect")

if __name__ == "__main__":
  setup()