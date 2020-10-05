#include <AccelStepper.h>

#define enable_motor1 3
#define enable_motor2 5
#define LS_1 4
#define LS_2 6
#define LS_3 7
#define LS_4 10
#define steps_per_revolution 20
#define microStetps 16
#define max_Speed 10000

int incomingByte;               // Reads Whats come from python
int Steps_per_movement;            // define the number of mm movement each space
int speed_motors;               // define the speed  of movement [0-100]

AccelStepper Xaxis(1, 8, 9); // pin 8 = step, pin 9 = direction
AccelStepper Yaxis(1, 11, 12); // pin 11 = step, pin 12 = direction

//------------------------------------------------------------------------------
void init_motores() {
  // init motor one
  pinMode(enable_motor1, OUTPUT);
  Xaxis.setMaxSpeed(5000);
  Xaxis.setSpeed(800);
  Xaxis.setCurrentPosition(0);
  digitalWrite(enable_motor1, HIGH); // turn motor off

  // init motor two
  pinMode(enable_motor2, OUTPUT);
  Yaxis.setMaxSpeed(5000);
  Yaxis.setSpeed(800);
  Yaxis.setCurrentPosition(0);
  digitalWrite(enable_motor2, HIGH); // turn motor off
}

//------------------------------------------------------------------------------
void init_limit_switch() {
  pinMode(LS_1, INPUT);
  pinMode(LS_2, INPUT);
  pinMode(LS_3, INPUT);
  pinMode(LS_4, INPUT);
}

//------------------------------------------------------------------------------
void init_enviroment_variables() {
  incomingByte = 0;
  Steps_per_movement = 0;
  speed_motors = 0;
}

//------------------------------------------------------------------------------
void init_communication() {
  Serial.begin(115200);
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
int readSensor(int Sensor) {
  return digitalRead(Sensor);
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/* steps per revolutions must be multiply by the number of microsteps in order
  to find the real steps need per one revolution

  is divided by 5 because pitch of the screw is 1.25 mm, but we need to move in
  millimeters steps, so 4/5 of a revolution es a millimeter, and thats why we
  multiply by four */
int Distance_to_Steps (int distance) { //Distance in millimeters
  int Steps_per_milimeters = (steps_per_revolution * microStetps / 5) * 4;
  return Steps_per_milimeters * distance;
}

//------------------------------------------------------------------------------
void Set_movement_parameters(int movement_speed, int millimeters) {
  Steps_per_movement = Distance_to_Steps(millimeters);
  speed_motors = max_Speed * (double(movement_speed) / 10.0);
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
void move_motor(AccelStepper motor, int speed_mov , int mov_dir , int enable) {
  motor.setCurrentPosition(0);
  motor.setSpeed(mov_dir * speed_mov);

  digitalWrite(enable, LOW); // Turn on motor
  while (motor.currentPosition() != mov_dir * Steps_per_movement) motor.runSpeed();
  digitalWrite(enable, HIGH);// Turn off motor

}

//------------------------------------------------------------------------------
void go_to_Home() {
  int speed_motors_homing = max_Speed * (1.0 / 10.0);
  while (readSensor(LS_2) == 0) move_motor(Xaxis, speed_motors_homing, 1, enable_motor1);
  while (readSensor(LS_3) == 0) move_motor(Xaxis, speed_motors_homing, -1, enable_motor1);
}


//------------------------------------------------------------------------------

void setup() {
  init_enviroment_variables();
  init_communication() ;
  init_limit_switch();
  init_motores();
  Set_movement_parameters(4,4);
}

void loop() {
  if(Serial.available() > 0) {
    incomingByte = Serial.read();
    Serial.write(incomingByte);
    if (incomingByte  == 48)go_to_Home();
    else if (incomingByte  == 49 )move_motor(Xaxis, speed_motors, 1, enable_motor1);
    else if (incomingByte  == 50 )move_motor(Xaxis, speed_motors, -1, enable_motor1);
  }
}
