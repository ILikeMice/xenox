import OPi.GPIO as GPIO
import board
import adafruit_tca9548a
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_pca9685
import time

limswitch = "PC14"
GPIO.setup(limswitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

stepper_pulse = "PC5"
stepper_dir = "PC6"

GPIO.setup(stepper_dir, GPIO.OUT)
GPIO.setup(stepper_pulse, GPIO.OUT)

i2c = board.I2C() 

tca = adafruit_tca9548a.TCA9548A(i2c)

ads = ADS.ADS1115(tca[1])

channel0 = AnalogIn(ads, ADS.P0)
channel1 = AnalogIn(ads, ADS.P1)
channel2 = AnalogIn(ads, ADS.P2)

pca = adafruit_pca9685.PCA9685(tca[2])
pca.frequency = 50 

def set_servo(servo_channel, angle):
    if not (0 <= angle <= 270):
        print(f"angle too big: {angle}.")
        return

    min_pulse = 1000  
    max_pulse = 2000 
    pulse_width = min_pulse + (angle / 180.0) * (max_pulse - min_pulse)
   
    duty_cycle = int((pulse_width / 20000.0) * 4095) 
    
    pca.channels[servo_channel].duty_cycle = duty_cycle
    
    
def servo_off(servo_channel):
    pca.channels[servo_channel].duty_cycle = 0
    
    
def read_switch():
    return not GPIO.input(limswitch)     
    
def stepper_home():
    global stepper_position
    
    print("homing...")

    GPIO.output(stepper_dir, 0)
    time.sleep(0.0001)
    
    while not read_switch():
        GPIO.output(stepper_pulse, GPIO.HIGH)
        time.sleep(0.002)
        GPIO.output(stepper_pulse, GPIO.LOW)
        time.sleep(0.002)
    
    stepper_position = 0
    print("Homed!!")
    
    
def stepper_step(direction, steps, delay=0.001):
    global stepper_position
    
    
    GPIO.output(stepper_dir, direction)
    time.sleep(0.0001)  
    
    for i in range(steps):
        if read_switch():
            print("stopping, switch")
            break
            
        GPIO.output(stepper_pulse, GPIO.HIGH)
        time.sleep(delay / 2)
        GPIO.output(stepper_pulse, GPIO.LOW)
        time.sleep(delay / 2)
        
        if direction:
            stepper_position += 1
        else:
            stepper_position -= 1
            

def stepper_move_to_position(targetpos, speed=0.001):
    global stepper_position
    
    steps_to_move = abs(targetpos - stepper_position)
    direction = 1 if targetpos > stepper_position else 0
    
    stepper_step(direction, steps_to_move, speed)    
# all the movement stuff i should need i think