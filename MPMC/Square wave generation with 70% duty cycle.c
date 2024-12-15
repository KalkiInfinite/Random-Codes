#include <reg51.h>

#define OSC_FREQ 11059200UL
#define TIMER1_PRESCALER 12

void main() {
    unsigned int reload_value;
    reload_value = (OSC_FREQ / (2 * TIMER1_PRESCALER * 5000)) - 1;

    TMOD |= 0x10;
    TH1 = reload_value >> 8;
    TL1 = reload_value & 0xFF;
    TR1 = 1;

    while (1) {
        while (!TF1);
        TF1 = 0;
        P1 ^= 0x20;
    }
}