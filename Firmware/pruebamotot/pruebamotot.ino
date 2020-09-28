#define enable_motor1 3

#include <AccelStepper.h>

AccelStepper Xaxis(1, 8, 9); // pin 3 = step, pin 6 = direction

void setup() {
  pinMode(enable_motor1, OUTPUT);
  Xaxis.setMaxSpeed(5000);
  Xaxis.setSpeed(600);
  Xaxis.setCurrentPosition(0);
  digitalWrite(enable_motor1, HIGH);
}

void loop() {
  digitalWrite(enable_motor1, LOW);
  Xaxis.setCurrentPosition(0);
  while (Xaxis.currentPosition() != 3200) {
    Xaxis.setSpeed(3200);
    Xaxis.runSpeed();
  }
  digitalWrite(enable_motor1, HIGH);
  delay(1000);
}
