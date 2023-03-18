## Micro-Controllers Part IV 


---

### by Jogi 

![Jogi](yogi_bear-head.jpg)

---

* Recap last two micro-controller talks
* Show the different envs for Pico
* Compare onboarding 
* compare results
* Know your platform
* New : WLAN and BLE 

---

### Short recap 

* complicated setup
* Arduino enters the world => all in one
* Raspberry Pi Pico => Python


---

### Micro-Controller 

* something to control 
   * LED
   * Motor
   * others
* somehow be controlled
   * Sensors
   * Switches
   * external events

---

## Micro Python : Internal LED (Pin25)

<pre><code data-line-numbers="2|4|6-8">
import machine

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.value(1)
    led_onboard.value(0)

</pre></code>

---

## Micro Python : External red LED (Pin15)

<pre><code data-line-numbers="2|4|6-8">
import machine

red_light = machine.Pin(15, machine.Pin.OUT)

while True:
    red_light.value(1)
    red_light.value(0)

</pre></code>



---

## Dockerfile

<pre><code data-line-numbers="1|3|5-8|10|12|14">FROM mcr.microsoft.com/mssql/server:2019-CU5-ubuntu-18.04

USER root

RUN mkdir /var/opt/sqlserver
RUN mkdir /var/opt/sqlserver/sqldata
RUN mkdir /var/opt/sqlserver/sqllog
RUN mkdir /var/opt/sqlserver/sqlbackups

RUN chown -R mssql /var/opt/sqlserver

USER mssql

CMD /opt/mssql/bin/sqlservr
</pre></code>

---


### Micro:BIT 

* Launched in 2016 by BBC in UK
* Target: Every Schoolkid ~ 12y has one
* Platform
* Web-Editor
* Simulator 
* [The Web-Editor](https://makecode.microbit.org/#editor)

---
### The Micro:BIT Board

![The Board](pics/microbit_1.jpg)


---


### Micro:BIT Homepage

![Homepage MicroBit](pics/microbit_start.png)


---

### Demo-Time 1

[https://makecode.microbit.org/#editor](https://makecode.microbit.org/#editor)


---

### What we (hopefully) saw

* https://microbit.org/
* ditor : https://makecode.microbit.org/
* Simple-Programm : https://makecode.microbit.org/_dt5boP7AKaqj
* Fill-Screen : https://makecode.microbit.org/_R8d2zWgbsUmg
* Moodsend : https://makecode.microbit.org/_VAiVxqE3CgDP

---

### 2021 Raspberry Pi Pico enters the world



---

### Raspberry Pi Pico

* just another Micro-Controller 
* But 3 interesting aspects
    * is from the Raspberry-PI foundation => might attract new "customers"
    * breaks with the "Has to run with Arduino-IDE"-Dogma 
    * Has at least one interesting HW-Block, the PIO


---


### Raspberry Pi Pico

* always starts as UF2-Board
* looks like a USB-Stick
* Microsoft-defined USB-Format
* especially dedicated for downloading firmware to MC via USB
* Cannot put just e.g. python-Files on it

---

### The PICO itself


![raspberry_pi_pico.jpg](./pics/raspberry_pi_pico.jpg)

---

### The PINs of PICO


![RPI-Pico-Pins.jpg](./pics/RPI-Pico-Pins.jpg)

---

### The Blocks of PICO

![rp2040_blocks.jpg](./pics/rp2040_blocks.jpg)

---

### Raspi Pico Dev Environements

* Plain SDK (Assembler/C/C++)
* Micropython
* Circuitpython
* Arduino-IDE

---

### PICO as U2F-USB Mass-Storage

![pico_as_uf2.png](./pics/pico_as_uf2.png)

---

### Dev-Environment : SDK 


![dev_env_pico_plain.png](./pics/dev_env_pico_plain.png)


---

### Dev-Environement : SDK (cmake)

![dev_env_pico_plain_II.png](./pics/dev_env_pico_plain_II.png)

---

### Python 

* Micro-Python
* Circuit Python

---

### Micro-Python

* Attempt to put Python on Micro-Controller-Boards
* Started with an own Board
* Interpreter now available for a lot of µC-Boards
* Including the Raspberry-Pi Pico


---

### Dev-Env Micro-Python


![dev_env_pico_micro.png](./pics/dev_env_pico_micro.png)

---

### Circuit-Python

* Is a fork of Micro-Python
* Done/maintained by Adafruit
* A lot of differences in the libraries
* Main difference visible : Provides a "real" USB-Drive

---

### Dev-Env Circuit-Python

![dev_env_pico_circuit.png](./pics/dev_env_pico_circuit.png)


---

### Arduino for the PICO

* was not in the focus of Raspberry-Pi organisation
* started as community-project
* since end of April 2021 : officially supported

---

### Installation via Board-Library


![pico_boardsmanager.png](./pics/pico_boardsmanager.png)

---

### Dev-Environement : Arduino


![dev_env_pico_arduino.png](./pics/dev_env_pico_arduino.png)

---

### The PIO

* Programmable IO
* "a Co-Processor", dedicated to programm even new serial "buses"
* offloads work from the CPU, compared to "bit-banging"
* https://www.cnx-software.com/2021/01/27/a-closer-look-at-raspberry-pi-rp2040-programmable-ios-pio/


---

### Conclusion for PICO

4 Different Dev-Environments

* C/C++ - SDK via cmake and U2F-Filesystem
* Micro-Python with USB-serial / Thonny
* Circuit-Python with real filesystem
* Arduino - IDE 

Choose yourself


---

### Link-Collection

* see git-repo (branch gh_pages)
* https://github.com/jogi-k/micro-controller-slides/tree/gh-pages
* Micro-Bit-Clone : https://www.crowdsupply.com/seluxit/wappsto-bit
---

### Legal stuff

* 

---

### The END 

![Jogi](yogi_bear-head.jpg)
