#include <SoftwareSerial.h>
SoftwareSerial mySerial1(4, 5); // RX, TX


void setup() {
  Serial.begin(9600);
  mySerial1.begin(57600);
}

void loop() {
  mySerial1.write(0x6d);
  int sensor[8];
  if (mySerial1.available()) {
    for(int i=0; i<8; i++){
      sensor[i] = mySerial1.read();
    }
    //Serial.print("stress ");
    Serial.print((sensor[1]+sensor[3]+sensor[5]+sensor[7]) / 4);
    Serial.print(" ");
    //Serial.print(" shear_x ");
    Serial.print(sensor[1]-sensor[7]);
    Serial.print(" ");
    //Serial.print(" shear_y ");
    Serial.println(sensor[3]-sensor[5]);
  }
  
  delay(100);
}
