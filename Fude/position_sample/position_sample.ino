int PIN_1=A1;
int PIN_2=A2;
int PIN_3=A3;
int PIN_5=A5;
int PIN_6=A6;
int PIN_7=A7;

float R_1=3700;
float R_2=2500;
float R_3=800;
float R_5=800;
float R_6=3000;
float R_7=2800;

void setup(){
    Serial.begin( 9600 );
}

void loop(){
    float value1;
    float value2;
    float value3;
    float value5;
    float value6;
    float value7;

    value1 = analogRead(PIN_1);
    value2 = analogRead(PIN_2);
    value3 = analogRead(PIN_3);
    value5 = analogRead(PIN_5);
    value6 = analogRead(PIN_6);
    value7 = analogRead(PIN_7);
    
    value1 = value1/1023*5;
    value2 = value2/1023*5;
    value3 = value3/1023*5;
    value5 = value5/1023*5;
    value6 = value6/1023*5;
    value7 = value7/1023*5;

    float Rx_1=(5/value1-1)*R_1;
    float Rx_2=(5/value2-1)*R_2;
    float Rx_3=(5/value3-1)*R_3;
    float Rx_5=(5/value5-1)*R_3;
    float Rx_6=(5/value6-1)*R_3;
    float Rx_7=(5/value7-1)*R_3;

    if(Rx_1 > 6000){
      Rx_1 = 6000;
    }
    if(Rx_2 > 4000){
      Rx_2 = 4000;
    }
    
    if(Rx_3 > 6000){
      Rx_3 = 6000;
    }
    if(Rx_5 > 6000){
      Rx_5 = 6000;
    }
    
    if(Rx_6 > 4000){
      Rx_6 = 4000;
    }
    if(Rx_7 > 6000){
      Rx_7 = 6000;
    }

    float value_x = (Rx_1 + Rx_2 + Rx_3) / 3;
    float value_y = (Rx_5 + Rx_6 + Rx_7) / 3;

    /*
    Serial.print(value_x);
    Serial.print(",");
    Serial.println(value_y);
    */

    //Serial.println(Rx_1/Rx_7);
    
    Serial.print(Rx_1/Rx_5);
    Serial.print(" ");
    //Serial.print(Rx_2);
    //Serial.print(" ");
    //Serial.print(Rx_3/Rx_5);
    //Serial.print(" ");
    //Serial.print(Rx_3 - Rx_5 - 500);
    //Serial.print(" ");
    Serial.print(Rx_3 * 5/Rx_5);
    Serial.print(" ");
    Serial.print(Rx_5/Rx_5);
    Serial.print(" ");
    //Serial.print(Rx_6);
    //Serial.print(" ");
    Serial.println(Rx_7 * 5/Rx_5);
    
    

    delay( 100 );
}
