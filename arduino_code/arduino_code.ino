const int ledPin = 13;
char command;
bool ledState = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);
  Serial.println("Type 'o' to turn on LED, 'f' to turn off LED, 't' to toggle LED");
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    Serial.print("Received command: ");
    Serial.println(command);
    
    if (command == 'o') { 
      on();
    } else if (command == 'f') {
      off();
    } else if (command == 't') {
      toggle();
    }
  }
}

void on() {
  digitalWrite(ledPin, HIGH);
  ledState = true;
  Serial.println("LED is ON");
}

void off() {
  digitalWrite(ledPin, LOW);
  ledState = false;
  Serial.println("LED is OFF");
}

void toggle() {
  if (ledState) {
    off();
  } else {
    on();
  }
}
