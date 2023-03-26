from mw20 import ssid
from mw20 import password

import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led, LED
import machine


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def web_page(temperature,state_int,state_red,state_yel,state_green):
#Template HTML
    html = f"""
<!DOCTYPE html>
<html>
<body>
<table>
 <tr>
   <td>Internal LED </td>
   <td><form action="./light_int_on"><input type="submit" value="Light on" /></form></td>
   <td><form action="./light_int_off"><input type="submit" value="Light off" /></form></td>
   <td><p> LED is {state_int} </p></td>
 </tr>
 <tr>
   <td> red LED </td>
   <td><form action="./light_red_on"><input type="submit" value="Light on" /></form></td>
   <td><form action="./light_red_off"><input type="submit" value="Light off" /></form></td>
   <td><p> LED is {state_red} </p></td>
 </tr>
 <tr>
   <td> yellow LED </td>
   <td><form action="./light_yel_on"><input type="submit" value="Light on" /></form></td>
   <td><form action="./light_yel_off"><input type="submit" value="Light off" /></form></td>
   <td><p> LED is {state_yel} </p></td>
 </tr>
 <tr>
   <td> green LED </td>
   <td><form action="./light_green_on"><input type="submit" value="Light on" /></form></td>
   <td><form action="./light_green_off"><input type="submit" value="Light off" /></form></td>
   <td><p> LED is {state_green} </p></td>
 </tr>
</table>
<p>Temperature is {temperature}</p>
</body>
</html>
"""
    return str(html)

def serve(connection):
    #Start a web server
    state_int = 'OFF'
    state_red = 'OFF'
    state_yel = 'OFF'
    state_green = 'OFF'
    red = LED(15)
    yellow = LED(14)
    green = LED(13)
    red.off()
    yellow.off()
    green.off()
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/light_int_on?':
            pico_led.on()
            state_int='ON'
        elif request =='/light_int_off?':
            pico_led.off()
            state_int='OFF'
        elif request =='/light_red_on?':
            red.on()
            state_red='ON'
        elif request =='/light_red_off?':
            red.off()
            state_red='OFF'
        elif request =='/light_yel_on?':
            yellow.on()
            state_yel='ON'
        elif request =='/light_yel_off?':
            yellow.off()
            state_yel='OFF'
        elif request =='/light_green_on?':
            green.on()
            state_green='ON'
        elif request =='/light_green_off?':
            green.off()
            state_green='OFF'
        temperature = pico_temp_sensor.temp
        html = web_page(temperature,state_int,state_red,state_yel,state_green)
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()