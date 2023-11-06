from machine import ADC, Pin
import time
import math
import machine
import tm1637


pressurecool_sensor = machine.ADC(26)
pressureoil_sensor = machine.ADC(27)
pressurefuel_sensor = machine.ADC(28)
LED = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN)
temp_sensor = machine.ADC(4)
mydisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

        
while True:
        LED(1)
        pressurecool = pressurecool_sensor.read_u16()*0.7333
        print(pressurecool, "cool pressure integral")  # valor lido pelo sensor em integral
        to_volts = 4.5 / 65535
        pressurecool_2 = pressurecool * to_volts # valor convertido para volts
        print(round(pressurecool_2,1), "pressure volts")
        pressurecool_bar = 2.59 * pressurecool_2 - 1.29 # valor convertido para BAR
        print(round(pressurecool_bar,1), "pressure BAR")
    
        pressureoil = pressureoil_sensor.read_u16()*0.7333
        print(pressureoil, "oil pressure integral")  # valor lido pelo sensor em integral
        to_volts = 4.5 / 65535
        pressureoil_2 = pressureoil * to_volts # valor convertido para volts
        print(round(pressureoil_2,1), "pressure volts")
        pressureoil_bar = 2.59 * pressureoil_2 - 1.29 # valor convertido para BAR
        print(round(pressureoil_bar,1), "pressure BAR")
    
        pressurefuel = pressurefuel_sensor.read_u16()*0.7333
        print(pressurefuel, "fuel pressure integral")  # valor lido pelo sensor em integral
        to_volts = 4.5 / 65535
        pressurefuel_2 = pressurefuel * to_volts # valor convertido para volts
        print(round(pressurefuel_2,1), "pressure volts")
        pressurefuel_bar = 2.59 * pressurefuel_2 - 1.29 # valor convertido para BAR
        print(round(pressurefuel_bar,1), "pressure BAR")
    
        to_volts_temp = 3.3 / 65535
        temperature = temp_sensor.read_u16()
        temperature_2 = temperature * to_volts_temp
        celsius_degrees = 27 - (temperature_2 - 0.706) / 0.001721
        print(int(round(celsius_degrees,0)))

        print("__________________________________")
        LED(0)
        time.sleep(4)



        #adjust the brightness to make it lower
        mydisplay.brightness(5)
        time.sleep(1)
    
        #show temperature
        mydisplay.temperature(int(celsius_degrees))
        time.sleep(4)
        
        
        #show numbers
        mydisplay.show("cool")
        time.sleep(2)
        mydisplay.pressure(int(pressurecool_bar))
        time.sleep(5)
    
        mydisplay.show(" oil")
        time.sleep(2)
        mydisplay.pressure(int(pressureoil_bar))
        time.sleep(5)
    
        mydisplay.show("fuel")
        time.sleep(2)
        mydisplay.pressure(int(pressurefuel_bar))
        time.sleep(5)
    
        mydisplay.show("    ")
    

    
        
        
        
      
         
