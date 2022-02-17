#include<Wire.h>
#include <SoftwareSerial.h>
// BMX055 加速度センサのI2Cアドレス  
#define Addr_Accl 0x19  // (JP1,JP2,JP3 = Openの時)

SoftwareSerial mySerial1(4, 5); // RX, TX
const int PRESSURE_PIN = A6;

// センサーの値を保存するグローバル変数
float xAccl = 0.00;
float yAccl = 0.00;
float zAccl = 0.00;



void setup() {
  // Wire(Arduino-I2C)の初期化
  Wire.begin();
  
  Serial.begin(9600);
  mySerial1.begin(57600);
  
  //BMX055 初期化
  BMX055_Init();
  delay(300);

}

void loop() {
  //BMX055 加速度の読み取り
  BMX055_Accl();
  float phi_rad = atan2(zAccl, xAccl);
  float theta_rad = atan2(yAccl, (sqrt(pow(xAccl, 2) + pow(zAccl, 2))));
  float phi = phi_rad*180.0/PI;
  float theta = theta_rad*180.0/PI;


  //触覚センサの読み取り
  int sensor[8];
  float stress;
  float shear_x;
  float shear_y;
  mySerial1.write(0x6d);
  if (mySerial1.available()) {
    for(int i=0; i<8; i++){
      sensor[i] = mySerial1.read();
    }
    stress = (sensor[1]+sensor[3]+sensor[5]+sensor[7]) / 4;
    shear_x = sensor[1]-sensor[7];
    shear_y = sensor[3]-sensor[5];
  }
  else{
    stress = 0;
    shear_x = 0;
    shear_y = 0;
  }
  

  //感圧センサの読み取り
  int pressure_value;
  pressure_value = analogRead( PRESSURE_PIN );

  //データの送信
  Serial.print(phi);
  Serial.print(" ");
  Serial.print(theta);
  Serial.print(" ");
  Serial.print(stress);
  Serial.print(" ");
  Serial.print(shear_x);
  Serial.print(" ");
  Serial.print(shear_y);
  Serial.print(" ");
  Serial.println(pressure_value);

  delay(100);
}



void BMX055_Init()
{
  //------------------------------------------------------------//
  Wire.beginTransmission(Addr_Accl);
  Wire.write(0x0F); // Select PMU_Range register
  Wire.write(0x03);   // Range = +/- 2g
  Wire.endTransmission();
  delay(100);
 //------------------------------------------------------------//
  Wire.beginTransmission(Addr_Accl);
  Wire.write(0x10);  // Select PMU_BW register
  Wire.write(0x08);  // Bandwidth = 7.81 Hz
  Wire.endTransmission();
  delay(100);
  //------------------------------------------------------------//
  Wire.beginTransmission(Addr_Accl);
  Wire.write(0x11);  // Select PMU_LPW register
  Wire.write(0x00);  // Normal mode, Sleep duration = 0.5ms
  Wire.endTransmission();
  delay(100);

}

void BMX055_Accl()
{
  unsigned int data[6];
  for (int i = 0; i < 6; i++)
  {
    Wire.beginTransmission(Addr_Accl);
    Wire.write((2 + i));// Select data register
    Wire.endTransmission();
    Wire.requestFrom(Addr_Accl, 1);// Request 1 byte of data
    // Read 6 bytes of data
    // xAccl lsb, xAccl msb, yAccl lsb, yAccl msb, zAccl lsb, zAccl msb
    if (Wire.available() == 1)
      data[i] = Wire.read();
  }
  // Convert the data to 12-bits
  xAccl = ((data[1] * 256) + (data[0] & 0xF0)) / 16;
  if (xAccl > 2047)  xAccl -= 4096;
  yAccl = ((data[3] * 256) + (data[2] & 0xF0)) / 16;
  if (yAccl > 2047)  yAccl -= 4096;
  zAccl = ((data[5] * 256) + (data[4] & 0xF0)) / 16;
  if (zAccl > 2047)  zAccl -= 4096;
  xAccl = xAccl * 0.0098; // range = +/-2g
  yAccl = yAccl * 0.0098; // range = +/-2g
  zAccl = zAccl * 0.0098; // range = +/-2g
}
