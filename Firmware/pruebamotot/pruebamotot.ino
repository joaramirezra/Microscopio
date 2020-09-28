#define step_pin 6
#define dir_pin 7
#define step_pin_1 8
#define dir_pin_1 9
#define VEL 500

void setup() {
  pinMode(step_pin, OUTPUT);
  pinMode(dir_pin, OUTPUT);
  pinMode(step_pin_1, OUTPUT);
  pinMode(dir_pin_1, OUTPUT);
  delay(1000);
  digitalWrite(dir_pin, HIGH);
  digitalWrite(dir_pin_1, HIGH);
}

void mover_motor() {
  digitalWrite(step_pin, HIGH);
  digitalWrite(step_pin_1, HIGH);
  delayMicroseconds(VEL);
  digitalWrite(step_pin, LOW);
  digitalWrite(step_pin_1, LOW);
  delayMicroseconds(VEL);
}


void mover_motor_1() {
  digitalWrite(step_pin_1, HIGH);
  digitalWrite(step_pin, HIGH);
  delayMicroseconds(VEL);
  digitalWrite(step_pin, LOW);
  digitalWrite(step_pin_1, LOW);
  delayMicroseconds(VEL);
}

void loop() {

  // mover derecha
  digitalWrite(dir_pin, HIGH);
  for (int i = 0 ; i < 1300; i++) mover_motor();

  // mover arriba
  digitalWrite(dir_pin_1, LOW);
  for (int i = 0 ; i < 1300; i++) mover_motor_1();

  // mover derecha
  digitalWrite(dir_pin, LOW);
  for (int i = 0 ; i < 1300; i++) mover_motor();

  // mover arriba
  digitalWrite(dir_pin_1, HIGH);
  for (int i = 0 ; i < 1300; i++) mover_motor_1();
}
