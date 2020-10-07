#include <AccelStepper.h>

#define enable_motor1 6
#define enable_motor2 9
#define LS_1 12
#define LS_2 12
#define LS_3 12
#define LS_4 12
#define steps_per_revolution 20
#define microStetps 16
#define max_Speed 10000

int incomingByte;               // Reads Whats come from python
int Steps_per_movement;         // define the number of mm movement each space
int speed_motors;               // define the speed  of movement [0-100]
String inputString ;            // a String to hold incoming data
bool stringComplete ;           // whether the string is complete

AccelStepper Xaxis(1, 5, 4); // pin 8 = step, pin 9 = direction
AccelStepper Yaxis(1, 8, 7); // pin 11 = step, pin 12 = direction

//------------------------------------------------------------------------------
void init_motores(int enable , AccelStepper motor ) {
  // init motor one
  pinMode(enable, OUTPUT);
  motor.setMaxSpeed(5000);
  motor.setSpeed(800);
  motor.setCurrentPosition(0);
  digitalWrite(enable , HIGH); // turn motor off
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
  inputString = "";
  stringComplete = false;
  inputString.reserve(200);        // reserve 200 bytes for the inputString:
}

//------------------------------------------------------------------------------
void init_communication() {
  Serial.begin(9600);
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
  motor.setMaxSpeed(5000);
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
void actions_serial( String input_frame) {
  int cont = 0;
  String frame [5];
  String str_aux;

  // This section helps to split the string using comas as a separator
  for (int i = 0 ; i < input_frame.length(); i++) {
    if (input_frame[i] != ',' && i < (input_frame.length() - 1)) str_aux += input_frame[i];
    else {
      frame[cont++] = str_aux;
      str_aux = "";
    }
  }

  if (frame[0].toInt() == 0)delay(1);//go_to_Home();
  else if (frame[0].toInt() == 1 )move_motor(Xaxis, speed_motors, 1, enable_motor1);
  else if (frame[0].toInt() == 2 )move_motor(Xaxis, speed_motors, -1, enable_motor1);
  else if (frame[0].toInt() == 3 )move_motor(Yaxis, speed_motors, 1, enable_motor2);
  else if (frame[0].toInt() == 4 )move_motor(Yaxis, speed_motors, -1, enable_motor2);
  else if (frame[0].toInt() == 5 )Set_movement_parameters(frame[1].toInt(), frame[2].toInt());
}

//------------------------------------------------------------------------------
void setup() {
  init_enviroment_variables();
  init_communication() ;
  init_limit_switch();
  delay(100);
  init_motores(enable_motor1, Xaxis);// init motor 1
  init_motores(enable_motor2, Yaxis);// init motor 1
  Set_movement_parameters(4, 4);
}

//------------------------------------------------------------------------------
void loop() {
  if (stringComplete) {
    inputString = inputString.substring(0, inputString.length() - 1);
    actions_serial(inputString);
    // clear the string:;
    inputString = "";
    stringComplete = false;
  }
}

//------------------------------------------------------------------------------
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') stringComplete = true;
  }
}
