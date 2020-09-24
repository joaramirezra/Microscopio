#define pin_motor 2
int cont = 0;
void setup() {
  pinMode(pin_motor, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(5, INPUT);  
  delay(100);
  digitalWrite(3, HIGH);

}

void mover_motor() {
  digitalWrite(pin_motor, HIGH);
  delayMicroseconds(500);
  digitalWrite(pin_motor, LOW);
  delayMicroseconds(500);
}


void loop() {
    if(digitalRead(5)) digitalWrite(3, LOW);
    else digitalWrite(3, HIGH); 
    mover_motor();
    
}
