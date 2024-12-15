#include <reg51.h>

sbit led = P2^0;
void delay(void);

void main() {
  led = 0;
  while(1) {
    led = 0;
    delay();
    led = 1;
    delay();
  }
}

void delay() {
  TMOD = 0x20;
  TH1 = 0xA4; 
  TL1 = 0x00;
  TR1 = 1;

  while(TF1 == 0);  
  
  TR1 = 0;  
  TF1 = 0;  
}
