from micropython import const
from machine import I2C, Pin
from utime import sleep

DFURM09_I2C_ADDR = const(0x11)


class DFRobot_URM09:
    """
    MicroPython class for communication with the DF2301Q from DFRobot via I2C
    """
    ## automatic mode
    MEASURE_MODE_AUTOMATIC = const(0x80)
    ## passive mode
    MEASURE_MODE_PASSIVE = const(0x00)
    ## passive mode configure registers
    CMD_DISTANCE_MEASURE = const(0x01)
    ## Ranging from 500
    MEASURE_RANG_500 = const(0x20)
    ## Ranging from 300
    MEASURE_RANG_300 = const(0x10)
    ## Ranging from 150
    MEASURE_RANG_150 = const(0x00)

    SLAVEADDR_INDEX = 0
    PID_INDEX = 1
    VERSION_INDEX = 2
    DIST_H_INDEX = 3
    DIST_L_INDEX = 4
    TEMP_H_INDEX = 5
    TEMP_L_INDEX = 6
    CFG_INDEX = 7
    CMD_INDEX = 8
    REG_NUM = 9
    txbuf = [0]

    def __init__(self, sda, scl, i2c_addr=DFURM09_I2C_ADDR, i2c_bus=0):
        """
        Initialize the DFURM09 I2C communication.
        :param sda: I2C SDA pin
        :param scl: I2C SCL pin
        :param i2c_addr: I2C address
        :param i2c_bus: I2C bus number
        """
        self._addr = i2c_addr

        try:
            self._i2c = I2C(i2c_bus, sda=Pin(sda), scl=Pin(scl))
        except Exception as err:
            print(f'Could not initialize i2c! bus: {i2c_bus}, sda: {sda}, scl: {scl}, error: {err}')

    def _write_reg(self, reg, data) -> None:
        """
        Writes data to the I2C register.
        :param reg: register address
        :param data: data to write
        :return: None
        """
        if isinstance(data, int):
            data = [data]

        try:
            self._i2c.writeto_mem(self._addr, reg, bytearray(data))
        except Exception as err:
            print(f'Write issue: {err}')

    def _read_reg(self, reg, length) -> bytes:
        """
        Reads data from the I2C register.
        :param reg: register address
        :param length: number of bytes to read
        :return: bytes or 0
        """
        try:
            result = self._i2c.readfrom_mem(self._addr, reg, length)
        except Exception as err:
            print(f'Read issue: {err}')
            result = [0, 0]

        return result

    def set_mode_range(self, measure_range, mode) -> None:
        """
        Set measure mode range.
        :param measure_range: Measured distance mode
        :param mode: Set mode
        """
        self.txbuf = [measure_range | mode]
        self._write_reg(self.CFG_INDEX, self.txbuf)

    def measurement_start(self) -> None:
        """
        Passive mode ranging command.

        Passive start for measuremnt mode
        """
        self.txbuf = [self.CMD_DISTANCE_MEASURE]
        self._write_reg(self.CMD_INDEX, self.txbuf)

    def get_temperature(self) -> float:
        """
        Get temerature.
        :return: Temperature in degrees Celsius
        """
        result = self._read_reg(self.TEMP_H_INDEX, 2)
        if result == -1:
            return 25.0
        return float(((result[0] << 8) + result[1]) / 10)

    def get_distance(self) -> int:
        """
        Get distance.
        :return: Distance in centimeters
        """
        result = self._read_reg(self.DIST_H_INDEX, 2)
        if result == -1:
            return -1
        if ((result[0] << 8) + result[1]) < 32768:
            return ((result[0] << 8) + result[1])
        else:
            return (((result[0] << 8) + result[1]) - 65536)

    def modify_device_number(self, address) -> None:
        """
        Modify device number (address).
        :param address: Addres for device
        """
        self.txbuf = [address]
        self._write_reg(self.SLAVEADDR_INDEX, self.txbuf)

    def get_device_number(self):
        """
        Get device numer.
        :return: i2c device address
        """
        result = self._read_reg(self.SLAVEADDR_INDEX, 1)
        return result[0]
