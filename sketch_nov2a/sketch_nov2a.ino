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
    char temp = command;
    command = Serial.read();
    Serial.println(command);
    
    if (command == 'o') { 
      on();
    } else if (command == 'f') {
      off();
    } else if (command == 't') {
      if(temp == 'o') {
        command = 'f';
        off();
      }
      if(temp == 'f') {
        command = 'o';
        on();
      }
    }
  }
}

void on() {
  digitalWrite(ledPin, HIGH);
  Serial.println("LED is on");
}

void off() {
  digitalWrite(ledPin, LOW);
  Serial.println("LED is off");
}