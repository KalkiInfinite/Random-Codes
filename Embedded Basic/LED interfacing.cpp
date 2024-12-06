void setup() {  
    pinMode(9, OUTPUT);  
    pinMode(10, OUTPUT);  
    pinMode(11, OUTPUT);  
}  

void loop() {  
    for (int i = 0; i < 256; i++) {     
        analogWrite(9, i);     
        analogWrite(10, 256 - i);     
        delay(10);  
    }  

    for (int i = 0; i < 256; i++) {     
        analogWrite(10, i);     
        analogWrite(11, 256 - i);     
        delay(10);  
    }  

    for (int i = 0; i < 256; i++) {     
        analogWrite(11, i);     
        analogWrite(9, 256 - i);     
        delay(10);  
    }  
}
