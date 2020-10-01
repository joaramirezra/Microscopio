#include <AccelStepper.h>

#define enable_motor1 3
#define enable_motor2 4

#define pasos_rev 200
#define microPasos 16
#define paso_Tornillo 12.5 //en milimetros

AccelStepper Xaxis(1, 8, 9); // pin 3 = step, pin 6 = direction

int Distance_to_Steps (int distance) { //Di
  int Steps_per_milimeters = (pasos_rev * microPasos / 5) * 4;
  return Steps_per_milimeters * distance;
}

void mover_motor(int pasos, AccelStepper motor) {
  motor.setCurrentPosition(0);
  if (pasos > 0) motor.setSpeed(1800);
  else  motor.setSpeed(-1800);

  while (motor.currentPosition() != pasos) {
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

void move_motor(int distance, int motor_enable , int motor) {
  digitalWrite(motor_enable, LOW);
  if (motor == 1 ) mover_motor(Distance_to_Steps(distance), Xaxis);
  else delay(1);
  digitalWrite(motor_enable, HIGH);
}

void go_to_Home() {
  int cont = 5;
  while (cont > 0) { // this condition must be replaced by limit swich
    move_motor(1, enable_motor1, 1);
    cont--;
  }
  delay(1000);
  cont = 5;
  while (cont > 0) {
    move_motor(-1, enable_motor1, 1);
    cont--;
  }
  delay(1000);  

}
void setup() {
  init_motores();
}

void loop() {
  go_to_Home();
}
