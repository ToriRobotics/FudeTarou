
const int FORCE_PIN = A6;

void setup(){
    Serial.begin( 9600 );
}

void loop(){
    int value;
    float volt;

    value = analogRead( FORCE_PIN );

    volt = value * 5.0 / 1023.0;

    Serial.print( "Value: " );
    Serial.print( value );
    Serial.print( "  Volt: " );
    Serial.println( volt );
    delay( 100 );
}
