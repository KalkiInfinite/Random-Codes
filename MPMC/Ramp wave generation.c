#include <reg51.h>

int main (void)
{
    unsigned char i = 0;    // Define a counter
    P2 = 0xFF;             // Make port P2 as output port

    while (1)              // Do forever
    {
        P2 = i;            // Copy i into port P2 to be converted
        i++;               // Increment the counter
    }

    return 0;
}
