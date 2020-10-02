#include <AccelStepper.h>

#define enable_motor1 3
#define enable_motor2 5
#define LS_1 4
#define LS_2 6
#define LS_3 7
#define LS_4 10
#define pasos_rev 20
#define microPasos 16

AccelStepper Xaxis(1, 8, 9); // pin 3 = step, pin 6 = direction

//------------------------------------------------------------------------------
int Distance_to_Steps (int distance) { //Distance in millimeters
  int Steps_per_milimeters = (pasos_rev * microPasos / 5) * 4;
  return Steps_per_milimeters * distance;
}

//------------------------------------------------------------------------------
void mover_motor(int pasos, AccelStepper motor) {
  motor.setCurrentPosition(0);
  if (pasos > 0) motor.setSpeed(1800);
  else  motor.setSpeed(-1800);

  while (motor.currentPosition() != pasos) {
    motor.runSpeed();
  }
}

//------------------------------------------------------------------------------
void init_motores() {
  pinMode(enable_motor1, OUTPUT);
  Xaxis.setMaxSpeed(5000);
  Xaxis.setSpeed(800);
  Xaxis.setCurrentPosition(0);
  digitalWrite(enable_motor1, HIGH);
}

//------------------------------------------------------------------------------
void init_limit_switch() {
  pinMode(LS_1, INPUT);
  pinMode(LS_2, INPUT);
  pinMode(LS_3, INPUT);
  pinMode(LS_4, INPUT);
}

//------------------------------------------------------------------------------
int readSensor(int Sensor) {
  return digitalRead(Sensor);
}

//------------------------------------------------------------------------------
void move_motor(int distance, int motor_enable , int motor) {
  digitalWrite(motor_enable, LOW);
  if (motor == 1 ) mover_motor(Distance_to_Steps(distance), Xaxis);
  else delay(1);
  digitalWrite(motor_enable, HIGH);
}

//------------------------------------------------------------------------------
void go_to_Home() {
  while (readSensor(LS_2) == 0) { // this condition must be replaced by limit swich
    move_motor(1, enable_motor1, 1);
  }
  while (readSensor(LS_3) == 0) { // this condition must be replaced by limit swich
    move_motor(-1, enable_motor1, 1);
  }
}

//------------------------------------------------------------------------------

void init_communication() {
  Serial.begin(115200);
}

//------------------------------------------------------------------------------
void setup() {
  init_communication() ;
  init_limit_switch();
  init_motores();
}

int incomingByte = 0;

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte  == 48)go_to_Home();
    else if (incomingByte  == 49 )move_motor(5, enable_motor1, 1);
    else if (incomingByte  == 50 )move_motor(-5, enable_motor1, 1);
  }
}
