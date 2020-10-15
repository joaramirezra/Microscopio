EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Shield raspberry pi microscope"
Date "2020-09-15"
Rev "V1"
Comp "Datalacia"
Comment1 "proprietary licence "
Comment2 "all uses under propietary permission"
Comment3 "Johan A. Ramirez"
Comment4 "Autor :"
$EndDescr
$Comp
L Drivers:TMC2100 Motor1
U 1 1 5F616BB5
P 6050 1600
F 0 "Motor1" H 5900 2050 50  0000 C CNN
F 1 "TMC2100" H 6350 1150 50  0000 C CNN
F 2 "Motor_driver:IC_DRV8825_STEPPER_MOTOR_DRIVER_CARRIER" H 7850 1500 50  0001 C CNN
F 3 "" H 7850 1500 50  0001 C CNN
	1    6050 1600
	1    0    0    -1  
$EndComp
Text GLabel 5600 1250 0    50   Input ~ 0
EN_motor1
Text GLabel 5600 1950 0    50   Input ~ 0
Dir_motor1
Text GLabel 5600 1850 0    50   Input ~ 0
Step_motor1
Text GLabel 6450 1650 2    50   Input ~ 0
motor1_1A
Text GLabel 6450 1750 2    50   Input ~ 0
motor_1B
Text GLabel 6450 1450 2    50   Input ~ 0
motor1_2B
Text GLabel 6450 1550 2    50   Input ~ 0
motor1_2A
Text Notes 5400 700  0    118  ~ 0
Driver motor 1\n
Text GLabel 6450 1350 2    50   Input ~ 0
GND_motor
Text GLabel 6450 1250 2    50   Input ~ 0
Vmot_1
Text GLabel 9050 1850 0    50   Input ~ 0
Step_motor2
Text GLabel 9050 1950 0    50   Input ~ 0
Dir_motor2
Text GLabel 9050 1250 0    50   Input ~ 0
EN_motor2
Text GLabel 9900 1350 2    50   Input ~ 0
GND_motor
Text GLabel 9900 1250 2    50   Input ~ 0
Vmot_1
Text GLabel 9900 1550 2    50   Input ~ 0
motor2_2A
Text GLabel 9900 1450 2    50   Input ~ 0
motor2_2B
Text GLabel 9900 1750 2    50   Input ~ 0
moto2_1B
Text GLabel 9900 1650 2    50   Input ~ 0
motor2_1A
$Comp
L Drivers:TMC2100 Motor2
U 1 1 5F618887
P 9500 1600
F 0 "Motor2" H 9300 2050 50  0000 C CNN
F 1 "TMC2100" H 9750 1150 50  0000 C CNN
F 2 "Motor_driver:IC_DRV8825_STEPPER_MOTOR_DRIVER_CARRIER" H 11300 1500 50  0001 C CNN
F 3 "" H 11300 1500 50  0001 C CNN
	1    9500 1600
	1    0    0    -1  
$EndComp
Text GLabel 5750 4600 0    50   Input ~ 0
Step_motor2
Text GLabel 5750 4500 0    50   Input ~ 0
Dir_motor2
Text GLabel 5750 4700 0    50   Input ~ 0
EN_motor2
Text GLabel 5750 4300 0    50   Input ~ 0
Step_motor1
Text GLabel 5750 4200 0    50   Input ~ 0
Dir_motor1
Text GLabel 5750 4400 0    50   Input ~ 0
EN_motor1
$Comp
L MCU_Module:Arduino_Nano_v2.x Arduino_Nano1
U 1 1 5F6775DB
P 6250 4400
F 0 "Arduino_Nano1" H 6650 3450 50  0000 C CNN
F 1 "Arduino_Nano_v2.x" H 6800 3450 50  0001 C CNN
F 2 "Module:Arduino_Nano" H 6250 4400 50  0001 C CIN
F 3 "https://www.arduino.cc/en/uploads/Main/ArduinoNanoManual23.pdf" H 6250 4400 50  0001 C CNN
	1    6250 4400
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Male motor1_plug1
U 1 1 5F65D5CE
P 9050 3550
F 0 "motor1_plug1" H 9000 3700 50  0000 C CNN
F 1 "Conn_01x04_Male" H 9158 3740 50  0001 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 9050 3550 50  0001 C CNN
F 3 "~" H 9050 3550 50  0001 C CNN
	1    9050 3550
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x04_Male motor2_plug1
U 1 1 5F65DC0C
P 10450 3550
F 0 "motor2_plug1" H 10400 3750 50  0000 C CNN
F 1 "Conn_01x04_Male" H 10558 3740 50  0001 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 10450 3550 50  0001 C CNN
F 3 "~" H 10450 3550 50  0001 C CNN
	1    10450 3550
	-1   0    0    1   
$EndComp
Text GLabel 8850 3450 0    50   Input ~ 0
motor1_1A
Text GLabel 8850 3350 0    50   Input ~ 0
motor_1B
Text GLabel 8850 3650 0    50   Input ~ 0
motor1_2B
Text GLabel 8850 3550 0    50   Input ~ 0
motor1_2A
Text GLabel 10250 3550 0    50   Input ~ 0
motor2_2A
Text GLabel 10250 3650 0    50   Input ~ 0
motor2_2B
Text GLabel 10250 3350 0    50   Input ~ 0
moto2_1B
Text GLabel 10250 3450 0    50   Input ~ 0
motor2_1A
Wire Notes Line
	11200 3900 7800 3900
Text Notes 8800 2650 0    118  ~ 0
Motors connectors
Text Notes 8750 700  0    118  ~ 0
Driver motor 2\n
Text Notes 5600 2650 0    118  ~ 0
AtMega328p
$Comp
L Connector:Conn_01x03_Female limit_swtich2
U 1 1 5F7020CE
P 10750 4700
F 0 "limit_swtich2" H 10700 4500 50  0000 L CNN
F 1 "Conn_01x03_Female" H 10778 4635 50  0001 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 10750 4700 50  0001 C CNN
F 3 "~" H 10750 4700 50  0001 C CNN
	1    10750 4700
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Female limit_swtich3
U 1 1 5F702513
P 9050 5800
F 0 "limit_swtich3" H 9000 5600 50  0000 L CNN
F 1 "Conn_01x03_Female" H 9078 5735 50  0001 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 9050 5800 50  0001 C CNN
F 3 "~" H 9050 5800 50  0001 C CNN
	1    9050 5800
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Female limit_swtich4
U 1 1 5F702C0B
P 10700 5800
F 0 "limit_swtich4" H 10650 5600 50  0000 L CNN
F 1 "Conn_01x03_Female" H 10728 5735 50  0001 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 10700 5800 50  0001 C CNN
F 3 "~" H 10700 5800 50  0001 C CNN
	1    10700 5800
	1    0    0    -1  
$EndComp
NoConn ~ 10550 4600
NoConn ~ 10500 5700
NoConn ~ 8850 5700
$Comp
L power:+5V #PWR0101
U 1 1 5F716686
P 10350 4650
F 0 "#PWR0101" H 10350 4500 50  0001 C CNN
F 1 "+5V" H 10365 4823 50  0000 C CNN
F 2 "" H 10350 4650 50  0001 C CNN
F 3 "" H 10350 4650 50  0001 C CNN
	1    10350 4650
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0102
U 1 1 5F717EE9
P 10300 5750
F 0 "#PWR0102" H 10300 5600 50  0001 C CNN
F 1 "+5V" H 10315 5923 50  0000 C CNN
F 2 "" H 10300 5750 50  0001 C CNN
F 3 "" H 10300 5750 50  0001 C CNN
	1    10300 5750
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0103
U 1 1 5F71839E
P 8650 5700
F 0 "#PWR0103" H 8650 5550 50  0001 C CNN
F 1 "+5V" H 8665 5873 50  0000 C CNN
F 2 "" H 8650 5700 50  0001 C CNN
F 3 "" H 8650 5700 50  0001 C CNN
	1    8650 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	8650 4750 8650 4650
$Comp
L power:+5V #PWR0104
U 1 1 5F714336
P 8650 4650
F 0 "#PWR0104" H 8650 4500 50  0001 C CNN
F 1 "+5V" H 8665 4823 50  0000 C CNN
F 2 "" H 8650 4650 50  0001 C CNN
F 3 "" H 8650 4650 50  0001 C CNN
	1    8650 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	8850 4750 8650 4750
NoConn ~ 8850 4650
$Comp
L Connector:Conn_01x03_Female limit_swtich1
U 1 1 5F6AE717
P 9050 4750
F 0 "limit_swtich1" H 9000 4550 50  0000 L CNN
F 1 "Conn_01x03_Female" H 9078 4685 50  0001 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 9050 4750 50  0001 C CNN
F 3 "~" H 9050 4750 50  0001 C CNN
	1    9050 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	10550 4700 10350 4700
Wire Wire Line
	10350 4700 10350 4650
Wire Wire Line
	10500 5800 10300 5800
Wire Wire Line
	10300 5800 10300 5750
Wire Wire Line
	8850 5800 8650 5800
Wire Wire Line
	8650 5800 8650 5700
Text GLabel 8550 4850 0    50   Input ~ 0
Limit_switch1
Text GLabel 8550 5900 0    50   Input ~ 0
Limit_switch3
Text GLabel 10300 4800 0    50   Input ~ 0
Limit_switch2
Text GLabel 10250 5900 0    50   Input ~ 0
Limit_switch4
$Comp
L Device:R_Small R1
U 1 1 5F73E250
P 8650 5000
F 0 "R1" H 8709 5046 50  0000 L CNN
F 1 "10K" H 8709 4955 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 8650 5000 50  0001 C CNN
F 3 "~" H 8650 5000 50  0001 C CNN
	1    8650 5000
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R3
U 1 1 5F73EA80
P 8650 6050
F 0 "R3" H 8709 6096 50  0000 L CNN
F 1 "10K" H 8709 6005 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 8650 6050 50  0001 C CNN
F 3 "~" H 8650 6050 50  0001 C CNN
	1    8650 6050
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R4
U 1 1 5F73F579
P 10300 6050
F 0 "R4" H 10359 6096 50  0000 L CNN
F 1 "10K" H 10359 6005 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 10300 6050 50  0001 C CNN
F 3 "~" H 10300 6050 50  0001 C CNN
	1    10300 6050
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R2
U 1 1 5F73F15B
P 10350 4950
F 0 "R2" H 10409 4996 50  0000 L CNN
F 1 "10K" H 10400 4900 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 10350 4950 50  0001 C CNN
F 3 "~" H 10350 4950 50  0001 C CNN
	1    10350 4950
	1    0    0    -1  
$EndComp
Wire Wire Line
	10250 5900 10300 5900
Wire Wire Line
	10300 4800 10350 4800
Wire Wire Line
	8550 5900 8650 5900
Wire Wire Line
	8550 4850 8650 4850
Wire Wire Line
	8650 4900 8650 4850
Connection ~ 8650 4850
Wire Wire Line
	8650 4850 8850 4850
Wire Wire Line
	10350 4850 10350 4800
Connection ~ 10350 4800
Wire Wire Line
	10350 4800 10550 4800
Wire Wire Line
	8650 5950 8650 5900
Connection ~ 8650 5900
Wire Wire Line
	8650 5900 8850 5900
Wire Wire Line
	10300 5950 10300 5900
Connection ~ 10300 5900
Wire Wire Line
	10300 5900 10500 5900
$Comp
L power:GND #PWR0105
U 1 1 5F75C087
P 8650 5100
F 0 "#PWR0105" H 8650 4850 50  0001 C CNN
F 1 "GND" H 8655 4927 50  0000 C CNN
F 2 "" H 8650 5100 50  0001 C CNN
F 3 "" H 8650 5100 50  0001 C CNN
	1    8650 5100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0106
U 1 1 5F75C5B0
P 10350 5050
F 0 "#PWR0106" H 10350 4800 50  0001 C CNN
F 1 "GND" H 10355 4877 50  0000 C CNN
F 2 "" H 10350 5050 50  0001 C CNN
F 3 "" H 10350 5050 50  0001 C CNN
	1    10350 5050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0107
U 1 1 5F75C982
P 10300 6150
F 0 "#PWR0107" H 10300 5900 50  0001 C CNN
F 1 "GND" H 10305 5977 50  0000 C CNN
F 2 "" H 10300 6150 50  0001 C CNN
F 3 "" H 10300 6150 50  0001 C CNN
	1    10300 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0108
U 1 1 5F75CDEC
P 8650 6150
F 0 "#PWR0108" H 8650 5900 50  0001 C CNN
F 1 "GND" H 8655 5977 50  0000 C CNN
F 2 "" H 8650 6150 50  0001 C CNN
F 3 "" H 8650 6150 50  0001 C CNN
	1    8650 6150
	1    0    0    -1  
$EndComp
Text Notes 8600 4150 0    118  ~ 0
limit switch connectors
Wire Notes Line
	7800 450  7800 6550
Wire Notes Line
	11200 4250 7800 4250
Text GLabel 6750 4400 2    50   Input ~ 0
Limit_switch1
Text GLabel 5750 5000 0    50   Input ~ 0
Limit_switch3
Text GLabel 5750 4900 0    50   Input ~ 0
Limit_switch2
Text GLabel 5750 5100 0    50   Input ~ 0
Limit_switch4
$Comp
L power:+5V #PWR0109
U 1 1 5F7AEB4D
P 6150 3300
F 0 "#PWR0109" H 6150 3150 50  0001 C CNN
F 1 "+5V" H 6165 3473 50  0000 C CNN
F 2 "" H 6150 3300 50  0001 C CNN
F 3 "" H 6150 3300 50  0001 C CNN
	1    6150 3300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0110
U 1 1 5F7B1284
P 6350 5400
F 0 "#PWR0110" H 6350 5150 50  0001 C CNN
F 1 "GND" H 6355 5227 50  0000 C CNN
F 2 "" H 6350 5400 50  0001 C CNN
F 3 "" H 6350 5400 50  0001 C CNN
	1    6350 5400
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0111
U 1 1 5F82A16F
P 7050 1800
F 0 "#PWR0111" H 7050 1650 50  0001 C CNN
F 1 "+5V" H 7065 1973 50  0000 C CNN
F 2 "" H 7050 1800 50  0001 C CNN
F 3 "" H 7050 1800 50  0001 C CNN
	1    7050 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 1850 7050 1850
Wire Wire Line
	7050 1850 7050 1800
$Comp
L power:+5V #PWR0112
U 1 1 5F82EB5A
P 10500 1850
F 0 "#PWR0112" H 10500 1700 50  0001 C CNN
F 1 "+5V" H 10515 2023 50  0000 C CNN
F 2 "" H 10500 1850 50  0001 C CNN
F 3 "" H 10500 1850 50  0001 C CNN
	1    10500 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	10500 1850 9900 1850
$Comp
L power:GND #PWR0113
U 1 1 5F83373B
P 6650 2100
F 0 "#PWR0113" H 6650 1850 50  0001 C CNN
F 1 "GND" H 6655 1927 50  0000 C CNN
F 2 "" H 6650 2100 50  0001 C CNN
F 3 "" H 6650 2100 50  0001 C CNN
	1    6650 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 1950 6650 1950
Wire Wire Line
	6650 1950 6650 2100
$Comp
L power:GND #PWR0114
U 1 1 5F836C9A
P 10150 2000
F 0 "#PWR0114" H 10150 1750 50  0001 C CNN
F 1 "GND" H 10155 1827 50  0000 C CNN
F 2 "" H 10150 2000 50  0001 C CNN
F 3 "" H 10150 2000 50  0001 C CNN
	1    10150 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	9900 1950 10150 1950
Wire Wire Line
	10150 1950 10150 2000
Wire Wire Line
	2950 1600 2950 1700
$Comp
L power:GND #PWR0115
U 1 1 5F848D89
P 2950 1700
F 0 "#PWR0115" H 2950 1450 50  0001 C CNN
F 1 "GND" H 2955 1527 50  0000 C CNN
F 2 "" H 2950 1700 50  0001 C CNN
F 3 "" H 2950 1700 50  0001 C CNN
	1    2950 1700
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0116
U 1 1 5F846A4B
P 2950 1400
F 0 "#PWR0116" H 2950 1250 50  0001 C CNN
F 1 "+5V" H 2965 1573 50  0000 C CNN
F 2 "" H 2950 1400 50  0001 C CNN
F 3 "" H 2950 1400 50  0001 C CNN
	1    2950 1400
	1    0    0    -1  
$EndComp
Text GLabel 1550 1350 0    50   Input ~ 0
Vmot_1
Text GLabel 1550 1750 0    50   Input ~ 0
GND_motor
$Comp
L Connector:Conn_01x03_Female Arduino_power_plug1
U 1 1 5F820890
P 3300 1500
F 0 "Arduino_power_plug1" H 3250 1300 50  0000 L CNN
F 1 "Conn_01x03_Female" H 3328 1435 50  0001 L CNN
F 2 "Connector_BarrelJack:BarrelJack_Horizontal" H 3300 1500 50  0001 C CNN
F 3 "~" H 3300 1500 50  0001 C CNN
	1    3300 1500
	1    0    0    -1  
$EndComp
$Comp
L pcb-rescue:Mounting_Hole-Mechanical MK4
U 1 1 5834FC4F
P 1850 7450
F 0 "MK4" H 1950 7496 50  0000 L CNN
F 1 "M2.5" H 1950 7405 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1850 7450 60  0001 C CNN
F 3 "" H 1850 7450 60  0001 C CNN
	1    1850 7450
	1    0    0    -1  
$EndComp
$Comp
L pcb-rescue:Mounting_Hole-Mechanical MK3
U 1 1 5834FBEF
P 1850 6950
F 0 "MK3" H 1950 6996 50  0000 L CNN
F 1 "M2.5" H 1950 6905 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1850 6950 60  0001 C CNN
F 3 "" H 1850 6950 60  0001 C CNN
	1    1850 6950
	1    0    0    -1  
$EndComp
$Comp
L pcb-rescue:Mounting_Hole-Mechanical MK1
U 1 1 5834FB2E
P 1150 6950
F 0 "MK1" H 1250 6996 50  0000 L CNN
F 1 "M2.5" H 1250 6905 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1150 6950 60  0001 C CNN
F 3 "" H 1150 6950 60  0001 C CNN
	1    1150 6950
	1    0    0    -1  
$EndComp
Text Notes 1750 700  0    118  ~ 0
Power Supply
Wire Notes Line
	11250 800  450  800 
Wire Wire Line
	3100 1600 2950 1600
Wire Wire Line
	3100 1400 2950 1400
$Comp
L Connector:Conn_01x03_Female Motor_power_plug1
U 1 1 5F81EFFC
P 1850 1550
F 0 "Motor_power_plug1" H 1800 1350 50  0000 L CNN
F 1 "Conn_01x03_Female" H 1878 1485 50  0001 L CNN
F 2 "Connector_BarrelJack:BarrelJack_Horizontal" H 1850 1550 50  0001 C CNN
F 3 "~" H 1850 1550 50  0001 C CNN
	1    1850 1550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 1450 1550 1450
Wire Wire Line
	1550 1450 1550 1350
Wire Wire Line
	1650 1650 1550 1650
Wire Wire Line
	1550 1650 1550 1750
Wire Notes Line
	500  2700 11250 2700
Wire Notes Line
	4500 450  4550 450 
Wire Notes Line
	4550 450  4550 500 
Wire Notes Line
	450  6300 7800 6300
Wire Notes Line
	500  6550 6950 6550
Text Notes 1450 6500 0    118  ~ 0
Mounting Holes\n
$Comp
L Device:LED D3
U 1 1 5F933ED6
P 2600 5600
F 0 "D3" V 2639 5483 50  0000 R CNN
F 1 "LED" V 2548 5483 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm_FlatTop" H 2600 5600 50  0001 C CNN
F 3 "~" H 2600 5600 50  0001 C CNN
	1    2600 5600
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D2
U 1 1 5F9348CC
P 2050 5600
F 0 "D2" V 2089 5483 50  0000 R CNN
F 1 "LED" V 1998 5483 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm_FlatTop" H 2050 5600 50  0001 C CNN
F 3 "~" H 2050 5600 50  0001 C CNN
	1    2050 5600
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D1
U 1 1 5F934BC6
P 1500 5600
F 0 "D1" V 1539 5678 50  0000 L CNN
F 1 "LED" V 1448 5678 50  0000 L CNN
F 2 "LED_THT:LED_D3.0mm_FlatTop" H 1500 5600 50  0001 C CNN
F 3 "~" H 1500 5600 50  0001 C CNN
	1    1500 5600
	0    1    -1   0   
$EndComp
$Comp
L Device:LED D4
U 1 1 5F9351E8
P 3200 5600
F 0 "D4" V 3239 5678 50  0000 L CNN
F 1 "LED" V 3148 5678 50  0000 L CNN
F 2 "LED_THT:LED_D3.0mm_FlatTop" H 3200 5600 50  0001 C CNN
F 3 "~" H 3200 5600 50  0001 C CNN
	1    3200 5600
	0    1    -1   0   
$EndComp
$Comp
L Transistor_Array:ULN2003A LED'sDriver1
U 1 1 5F937E39
P 2400 3600
F 0 "LED'sDriver1" H 2400 4150 50  0000 C CNN
F 1 "ULN2003A" H 2700 3050 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W7.62mm_LongPads" H 2450 3050 50  0001 L CNN
F 3 "http://www.ti.com/lit/ds/symlink/uln2003a.pdf" H 2500 3400 50  0001 C CNN
	1    2400 3600
	1    0    0    -1  
$EndComp
Text Notes 1900 4750 0    118  ~ 0
LED Indicators
Wire Notes Line
	3900 6300 3900 7800
Wire Notes Line
	3900 7800 3950 7800
Text GLabel 6750 4600 2    50   Input ~ 0
LED1
Text GLabel 6750 4700 2    50   Input ~ 0
LED2
Text GLabel 6750 4800 2    50   Input ~ 0
LED3
Text GLabel 6750 4900 2    50   Input ~ 0
LED4
Text Notes 1850 2650 0    118  ~ 0
LED's Driver
Text GLabel 2000 3400 0    50   Input ~ 0
LED1
Text GLabel 2000 3500 0    50   Input ~ 0
LED2
Text GLabel 2000 3600 0    50   Input ~ 0
LED3
Text GLabel 2000 3700 0    50   Input ~ 0
LED4
Text GLabel 2800 3700 2    50   Input ~ 0
S_LED1
Text GLabel 2800 3600 2    50   Input ~ 0
S_LED2
Text GLabel 2800 3500 2    50   Input ~ 0
S_LED3
Text GLabel 2800 3400 2    50   Input ~ 0
S_LED4
$Comp
L power:GND #PWR0117
U 1 1 5F96A60E
P 2400 4200
F 0 "#PWR0117" H 2400 3950 50  0001 C CNN
F 1 "GND" H 2405 4027 50  0000 C CNN
F 2 "" H 2400 4200 50  0001 C CNN
F 3 "" H 2400 4200 50  0001 C CNN
	1    2400 4200
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0118
U 1 1 5F96B0A2
P 2950 3150
F 0 "#PWR0118" H 2950 3000 50  0001 C CNN
F 1 "+5V" H 2965 3323 50  0000 C CNN
F 2 "" H 2950 3150 50  0001 C CNN
F 3 "" H 2950 3150 50  0001 C CNN
	1    2950 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2800 3200 2950 3200
Wire Wire Line
	2950 3200 2950 3150
Text GLabel 2050 5950 0    50   Input ~ 0
S_LED2
Text GLabel 2600 5950 0    50   Input ~ 0
S_LED3
Text GLabel 3150 5950 0    50   Input ~ 0
S_LED4
Text GLabel 1500 5950 0    50   Input ~ 0
S_LED1
Wire Wire Line
	1500 5750 1500 5950
Wire Wire Line
	3200 5750 3200 5950
Wire Wire Line
	2050 5750 2050 5950
Wire Wire Line
	2600 5750 2600 5950
$Comp
L Device:R_Small R5
U 1 1 5F993EF3
P 1500 5350
F 0 "R5" H 1559 5396 50  0000 L CNN
F 1 "220" H 1559 5305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 1500 5350 50  0001 C CNN
F 3 "~" H 1500 5350 50  0001 C CNN
	1    1500 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R8
U 1 1 5F9957FF
P 3200 5350
F 0 "R8" H 3259 5396 50  0000 L CNN
F 1 "220" H 3259 5305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 3200 5350 50  0001 C CNN
F 3 "~" H 3200 5350 50  0001 C CNN
	1    3200 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R6
U 1 1 5F995B3C
P 2050 5350
F 0 "R6" H 2109 5396 50  0000 L CNN
F 1 "220" H 2109 5305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 2050 5350 50  0001 C CNN
F 3 "~" H 2050 5350 50  0001 C CNN
	1    2050 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R7
U 1 1 5F995E4F
P 2600 5350
F 0 "R7" H 2659 5396 50  0000 L CNN
F 1 "220" H 2659 5305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 2600 5350 50  0001 C CNN
F 3 "~" H 2600 5350 50  0001 C CNN
	1    2600 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3150 5950 3200 5950
Wire Wire Line
	1500 5250 2050 5250
Connection ~ 2050 5250
Wire Wire Line
	2050 5250 2400 5250
Connection ~ 2600 5250
Wire Wire Line
	2600 5250 3200 5250
$Comp
L power:+5V #PWR0119
U 1 1 5F9B5AF1
P 2400 5150
F 0 "#PWR0119" H 2400 5000 50  0001 C CNN
F 1 "+5V" H 2415 5323 50  0000 C CNN
F 2 "" H 2400 5150 50  0001 C CNN
F 3 "" H 2400 5150 50  0001 C CNN
	1    2400 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 5150 2400 5250
Connection ~ 2400 5250
Wire Wire Line
	2400 5250 2600 5250
Wire Notes Line
	400  2400 11250 2400
Wire Notes Line
	4500 500  4500 6300
Text Notes 5250 6500 0    118  ~ 0
Auxilar 
Wire Notes Line
	450  4500 4500 4500
Wire Notes Line
	450  4850 4500 4850
NoConn ~ 6250 5400
Wire Wire Line
	6150 3300 6150 3400
Wire Wire Line
	1650 1550 1650 1650
Connection ~ 1650 1650
Wire Wire Line
	3100 1500 3100 1600
Connection ~ 3100 1600
NoConn ~ 6450 3400
NoConn ~ 6350 3400
$EndSCHEMATC
