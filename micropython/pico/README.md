# DFRobot_URM09
- [中文版](./README_CN.md)

This is an ultrasonic distance sensor module with open dual probe. It adopts I2C communication and standard interface of Gravity PH2.0-4P vertical patch socket. The module is compatible with controllers with 3.3V or 5V logical level, such as Arduino and Raspberry Pi. The ultrasonic sensor comes with built-in temperature compensation, providing effective ranging within 2cm to 500cm. It offers resolution of 1cm and accuracy of ±1%. There are three measurement ranges designed for programs to select: 150cm, 300cm, 500cm. Please note that setting shorter range will cause shorter ranging cycle and lower sensitivity. You may need to set it according to the actual use.

This module can be widely applied to outdoor environment, not least with rapid changes of temperature difference. It is definitely a prime select when it comes to projects like robot auto collision avoidance walk, car reversing alarm, doorbell, guard alert, subway safety line prompt, and one meter line prompt in bank and front of ATM machine. <br>
This ranging module, with small size, provides strong environment applicability, high accuracy and wide measurement range, plug and play, easy to use.

![效果图](../../resources/images/SEN0304_WIKI_Cover.jpg)


## Product Link(https://www.dfrobot.com/product-1832.html)

    SKU：SEN0304

## Table of Contents

* [Summary](#Summary)
* [Installation](#Installation)
* [Methods](#Methods)
* [Compatibility](#Compatibility)
* [History](#History)
* [Credits](#Credits)

## Summary

Effective ranging within 2cm to 500cm, resolution of 1cm and accuracy of ±1%

There are three measurement ranges: 150cm, 300cm, 500cm. Two measurement modes: active or passive(select by program).

Revisable I2C device address, avoiding multiple devices address conflicts.

## Installation
Download the library file before use, paste it into directory for Pico.

## Compatibility

* MicroPython Version

| MicroPython | Work Well | Work Wrong | Untested | Remarks |
|-------------| :-------: | :--------: | :------: | ------- |
| v1.22.2     |     √     |            |          |         |

* MicroPython Boards

| Boards | Work Well | Work Wrong | Untested | Remarks |
|--------| :-------: | :--------: | :------: | ------- |
| PicoW  |     √     |            |          |         |

## History
- 
- 2024/04/16 - V1.0.0 Version


## Credits

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))
Addjusted by Badger(karol@narowski.com.pl), 2024
