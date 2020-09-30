#include <AccelStepper.h>

#define enable_motor1 3
//#define enable_motor2 4
#define pasos_rev 200
#define microPasos 16
#define paso_Tornillo 12.5 //en milimetros

AccelStepper Xaxis(1, 8, 9); // pin 3 = step, pin 6 = direction

int Distance_to_Steps (int distance) { //Di
  int Steps_per_milimeters = (pasos_rev*microPasos/5)*4;
  return pasos_Calculados*distance;
}

void mover_motor(int pasos, AccelStepper motor) {
  motor.setCurrentPosition(0);
  while (motor.currentPosition() != pasos) {
    motor.setSpeed(800);
    motor.runSpeed();
  }
}


void init_motores() {
  pinMode(enable_motor1, OUTPUT);
  Xaxis.setMaxSpeed(5000);
  Xaxis.setSpeed(800);
  Xaxis.setCurrentPosition(0);
  digitalWrite(enable_motor1, HIGH);
}

void setup() {
  init_motores();
}

void loop() {
  digitalWrite(enable_motor1, LOW);
  mover_motor(2560, Xaxis);
  digitalWrite(enable_motor1, HIGH);
  delay(1000);
}
