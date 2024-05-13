#include <Wire.h>
#include <BluetoothSerial.h>

#define echoPin 2               // CHANGE PIN NUMBER HERE IF YOU WANT TO USE A DIFFERENT PIN
#define trigPin 4               // CHANGE PIN NUMBER HERE IF YOU WANT TO USE A DIFFERENT PIN
long duration, distance;

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32_BT"); // Name of your Bluetooth device
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration / 58.2;
  String disp = String(distance);

  //Serial.print("Distance: ");
  Serial.print(disp);
  //Serial.println(" cm");

  // Send distance via Bluetooth
  if (distance < 20){
    delay(1000);
    SerialBT.print('1');
  }

  //delay(1000);
}