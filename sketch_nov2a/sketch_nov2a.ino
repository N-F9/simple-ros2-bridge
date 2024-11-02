const int ledPin = 13;
char command;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
  Serial.begin(9600);
  Serial.println("Type 'o' to turn on LED, 'f' to turn off LED");
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    
    if (command == 'o') { 
      digitalWrite(ledPin, HIGH);
      Serial.println("LED is on");
    } else if (command == 'f') {
      digitalWrite(ledPin, LOW);
      Serial.println("LED is off");
    }
  }
}