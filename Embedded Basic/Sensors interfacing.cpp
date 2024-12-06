void setup()  
{  
    pinMode(2, INPUT);   
    pinMode(3, OUTPUT);  
}  

void loop()  
{  
    digitalWrite(3, LOW);   
    int read = digitalRead(2);   
    
    if (read == HIGH)  
    {  
        digitalWrite(3, HIGH);     
        delay(1000);   
    }  
    
    delay(1000);   
}  
