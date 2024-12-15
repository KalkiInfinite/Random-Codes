#include <reg51.h>

// Pre-calculated sine wave values scaled to 0-255
unsigned char sine_wave[] = {
    128, 150, 172, 192, 210, 226, 239, 248, 254, 255, 
    254, 248, 239, 226, 210, 192, 172, 150, 128, 106, 
    84,  64,  46,  30,  17,   8,   2,   0,   2,   8, 
    17,  30,  46,  64,  84,  106, 128
};

int main(void) {
    unsigned char i = 0;

    P2 = 0xFF; // Make port P2 an output port

    while (1) {
        P2 = sine_wave[i]; // Output the sine wave value to port P2
        i++; // Move to the next value in the sine wave array

        // Reset the index if we've reached the end of the array
        if (i >= sizeof(sine_wave) / sizeof(sine_wave[0])) {
            i = 0;
        }
    }

    return 0;
}
