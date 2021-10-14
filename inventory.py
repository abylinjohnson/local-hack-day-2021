components = ["","Transformer","Resistor","Capacitor","Diode","Transistor","IC","IC Base","Regulator IC","Rectifier","LDR","Magnetic Sensor","Mic","IR Led","Photo Diode","Photo Transistor","Thermistor","Piezo Element","LM 35","Coil","LDR Module",
"IR Module","Sound Module","Reed Sensor","Force Sensor","Flex Sensor","Load Cell","Rain Sensor","Water Level Sensor","Water Flow Sensor","Float Sensor","RO Float Sensor","MQ-2 ","MQ-3","MQ-5 ","MQ-6","Pulse Sensor","Flame sensor","Eye Blink Sensor","PIR Sensor","SD card Module","Metal Detector","IR Temp Sensor",
"DHT-11","Soil Moisture","Peltier","ultrasonic","Sensor Bracket","Vibration Sensor","Heartbeat Sensor","Color Sensor","EEG Sensor","IR Speed Sensor","ISD 1820 Voice Module","RTC Module","Current Sensor","Voltage Sensor","Boost Converter","Arduino UNO R3","Arduino UNO SMD","Arduino Mega","Arduino Nano","Attiny 85",
"Node MCU","DC-DC 3v","Rasperry Pi 3","Raspberry Pi 4","Raspberry Pi PICO","RFID EM18","RFID-Tag","RF-TX,RX","Zigbee-S2B","Zigbee-NRF24L01-TTL","Zigbee Adapter","WIFI-ESP8266","GSM Module","GPS-NEO6M","Fingerprint-R307","Pressure-BMP180","Raspberry PI Camera","Bluetooth Module","MCP 3008 ADC","L293D Motor Driver",
"L298 Motor Driver","DC DIMMER-PWM","DC 3v-20000v","TDS Sensor","PH Sensor","Hall Effect Sensor","Joystick","USB-TTL","ADXL 337","LCD Display","LCD Breakout","LED Display","MAX 7219 DOT Matrix","Relay Module","Relay","Connecting Wire","Jumper Wire","Main Cord Wire","LED","RGB LED","DC Motor","DC Gear Motor","DC BO Motor","Coreless Motor",
"BLDC Motor","Servo Motor","AC Motor","AC Gear Motor","Robotic Gripper","Robotic Arm","Air Pump Motor","Water Pump Motor","Generator Motor","Soldering Iron","Soldering Paste","Soldering Wick","Soldering Lead","Desoldering Pump","Wire Stripper","Wire Cutter","Temp Controller","CPU Fan Cooler","Cooling Fan","Thermal Paste","ESC For BLDC",
 "Propeller","LIPO Battery","Drone Camera","Drone","Drone Controller","DIY Drone Kit","Glue Gun","Glue Stick","Hose","Battery","Cell","ROBO Wheel","Solar Panel","Ferrite Magnet","Neodymium Magnet","PCB","Buzzer","Speaker","Digital Multimeter","Analog Multimeter","Magnetic Compass","Galvanometer","DC Adapter","Battery Eliminator",
 "220 T0 110V Converter", "12v DC-USB","I2C LCD Module","ON/OFF Switch","Push Button","DPDT Switch","Physics Lab Items","Chemistry Lab Items","Chemistry Lab Kit","DIY Spares","DIY KITS","Machanical Spares","Cylinder Piston","Solenoid valve","Manual valve","Hose Connector","Air Gauge","DC Male","DC Female","9v Battery Connector","2 Cell Holder","4 Cell Holder",
 "9v Cell Holder","Arduino cable","USB-MicroUSB cable","HDMI-VGA Cable","2 PIN PBT Connector","Berg Strip","Laser Light","USB Female","L-clamp For Motor","Keypad","Crocodile Clip","Electro Magnet"]
print("Hi-Tech Manual:\n")
while True:
    print("Enter 1 for search by number")
    print("Enter 2 for search by name")
    print("Enter 3 for print all")
    print("Enter 4 to terminate")
    choice = input()
    if choice == "1":
        print("Enter the Number:\n")
        num = int(input())
        print("##############")
        print(components[num])
        print("##############")
    if choice == "3":
        for i in range(len(components)):
            print(str(i)+" " + components[i] + "")
    if choice == "2":
        name = input("Enter the Name of the component:")
        for i in range(len(components)):
            if name.lower() in components[i].lower():
                print(str(i)+" "+components[i])
    if choice == "4":
        break
