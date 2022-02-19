int PIN_1=A1;
int PIN_2=A2;
int PIN_3=A3;
int PIN_5=A5;
int PIN_6=A6;
int PIN_7=A7;

float R_1=333.3;
float R_3=65.7;
float R_5=58.4;
float R_7=333.3;

float Offset_1=-23.3;
float Offset_3=-26.31;
float Offset_5=-58.4;
float Offset_7=-6.66;

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
    value3 = analogRead(PIN_2);
    value5 = analogRead(PIN_5);
    value7 = analogRead(PIN_7);
    
    value1 = value1/1023*5;
    value3 = value3/1023*5;
    value5 = value5/1023*5;
    value7 = value7/1023*5;

    float Rx_1=(5/value1-1)*R_1+Offset_1;
    float Rx_3=(5/value3-1)*R_3+Offset_3;
    float Rx_5=(5/value5-1)*R_5+Offset_5;
    float Rx_7=(5/value7-1)*R_7+Offset_7;

    if(Rx_1 > 1000) Rx_1 = 0;
    if(Rx_3 > 1000) Rx_3 = 0;
    if(Rx_5 > 1000) Rx_5 = 0;
    if(Rx_7 > 1000) Rx_7 = 0;

    Serial.print(Rx_1);
    Serial.print(" ");
    Serial.print(Rx_3);
    Serial.print(" ");
    Serial.print(Rx_5);
    Serial.print(" ");
    Serial.println(Rx_7);
    

    delay( 100 );
}
