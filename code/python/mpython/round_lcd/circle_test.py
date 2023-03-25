from machine import Pin,I2C,SPI,PWM,ADC

from ws_lcd_1inch28 import LCD_1inch28
from ws_lcd_1inch28 import QMI8658

import time

Vbat_Pin = 29


LCD = LCD_1inch28()
LCD.set_bl_pwm(65535)
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))   
    
color = LCD.blue

     

while(True):
        #read QMI8658
    LCD.fill(LCD.white)
    xyz=qmi8658.Read_XYZ()
        
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    LCD.circle( 120 + int(120 *y) , 120 - int(120 *x), int(abs(z) * 20), color)
        
    LCD.show()
    time.sleep(0.1)
    