from enum import Enum
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)


mfr_pins = (8, 10)      ## motor front right pins
mfl_pins = (3, 5)       ## motor front left pins


mrr_pins = (38, 40)     ## motor rear right pins
mrl_pins = (35, 37)     ## motor rear left pins


servo_pin = (12, )


all_mpins = mfr_pins + mfl_pins + mrr_pins + mrl_pins
all_pins = all_mpins + servo_pin


gpio.setup(
       all_pins,
       gpio.OUT
   )


class Motor(Enum):
  
   mfr = 0
   mfl = 1


   mrr = 2
   mrl = 3


def forward():
  
   start_motor(Motor.mfr)
   start_motor(Motor.mfl)
   start_motor(Motor.mrr)
   start_motor(Motor.mrl)


def backward():
  
   start_motor(Motor.mfr, True)
   start_motor(Motor.mfl, True)
   start_motor(Motor.mrr, True)
   start_motor(Motor.mrl, True)


def right():
  
   start_motor(Motor.mfl)
   start_motor(Motor.mrl)
   stop_motor(Motor.mfr)
   stop_motor(Motor.mrr)


def left():
  
   start_motor(Motor.mfr)
   start_motor(Motor.mrr)
   stop_motor(Motor.mfl)
   stop_motor(Motor.mrl)


def halt():
  
   stop_motor(Motor.mfr)
   stop_motor(Motor.mfl)
   stop_motor(Motor.mrr)
   stop_motor(Motor.mrl)


def isMotorValid(motor: Motor) -> tuple:


   if motor == Motor.mfr:
       pins = mfr_pins
  
   elif motor == Motor.mfl:
       pins = mfl_pins


   elif motor == Motor.mrr:
       pins = mrr_pins


   elif motor == Motor.mrl:
       pins = mrl_pins


   else:
       raise Exception(f"Invalid Motor: {motor}")


   return pins


def start_motor(motor: Motor, reverse: bool = False) -> None:


   pins = isMotorValid(motor)


   if not reverse:
       high, low = pins
   else:
       low, high = pins


   print(high, low)
   gpio.output(high, gpio.HIGH)
   gpio.output(low, gpio.LOW)


def stop_motor(motor: Motor) -> None:


   pins = isMotorValid(motor)


   # gpio.output(pins[0], gpio.LOW)
   # gpio.output(pins[1], gpio.LOW)
   gpio.cleanup(pins)
  gpio.setup(pins, gpio.OUT)


if __name__ == "__main__":


   try:
       while True:


           i = input()
           if i == 'w':
               forward()
           elif i == 's':
               backward()
           elif i == 'a':
               left()
           elif i == 'd':
               right()
           elif i == 'h':
               halt()


   except:
       gpio.cleanup()
