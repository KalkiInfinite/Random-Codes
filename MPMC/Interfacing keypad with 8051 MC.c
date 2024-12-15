#include <reg51.h> 

void main() {
    unsigned char seg[10] = {
        0xC0, // Hexadecimal pattern for displaying '0'
        0xF9, // Hexadecimal pattern for displaying '1'
        0xA4, // Hexadecimal pattern for displaying '2'
        0xB0, // Hexadecimal pattern for displaying '3'
        0x99, // Hexadecimal pattern for displaying '4'
        0x92, // Hexadecimal pattern for displaying '5'
        0x82, // Hexadecimal pattern for displaying '6'
        0xF8, // Hexadecimal pattern for displaying '7'
        0x80, // Hexadecimal pattern for displaying '8'
        0x90  // Hexadecimal pattern for displaying '9'
    };

    unsigned char x;  // Variable to loop through the array of segment patterns
    unsigned int i;   // Variable for delay loop

    P1 = 0x00; // Initialize port P1 as output

    while (1) { // Infinite loop to continuously display digits
        for (x = 0; x < 10; x++) { // Loop through each digit in the segment array
            P1 = seg[x]; // Output the segment pattern for the current digit to port P1
            for (i = 0; i < 60000; i++); // Delay loop to control the display speed
        }
    }
}
