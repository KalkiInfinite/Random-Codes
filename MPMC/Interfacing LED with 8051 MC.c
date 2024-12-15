#include <reg51.h>

// Define LCD data port and control pins
sfr lcd_data_port = 0x90;  // Define the LCD data port at address 0x90
sbit rs = P2^0;           // Register select pin
sbit rw = P2^1;           // Read/Write pin
sbit en = P2^2;           // Enable pin

// Delay function
void delay(unsigned int count) {
    int i, j;
    for (i = 0; i < count; i++) {
        for (j = 0; j < 112; j++);
    }
}

// Send a command to the LCD
void LCD_Command(unsigned char cmd) {
    lcd_data_port = cmd;  // Load the command to the data port
    rs = 0;               // Command mode
    rw = 0;               // Write mode
    en = 1;               // Enable the LCD
    delay(1);
    en = 0;               // Disable the LCD
    delay(5);
}

// Send a character to the LCD
void LCD_Char(unsigned char char_data) {
    lcd_data_port = char_data;  // Load the character to the data port
    rs = 1;                    // Data mode
    rw = 0;                    // Write mode
    en = 1;                    // Enable the LCD
    delay(1);
    en = 0;                    // Disable the LCD
    delay(5);
}

// Send a string to the LCD
void LCD_String(unsigned char *str) {
    int i;
    for (i = 0; str[i] != 0; i++) {  // Loop until the null character
        LCD_Char(str[i]);
    }
}

// Initialize the LCD
void LCD_Init(void) {
    delay(20);           // Initial delay for LCD stabilization
    LCD_Command(0x38);   // Configure the LCD in 8-bit mode, 2 lines, 5x7 font
    LCD_Command(0x06);   // Entry mode, auto increment cursor
    LCD_Command(0x01);   // Clear display
    LCD_Command(0x80);   // Move the cursor to the first row, first column
}

// Main function
void main() {
    LCD_Init();               // Initialize the LCD
    LCD_String("WELCOME");    // Display "WELCOME" on the first row
    LCD_Command(0xC0);        // Move cursor to the second row
    LCD_String("PIYUSHTYAGI"); // Display "PIYUSHTYAGI" on the second row
    while (1);                // Infinite loop to keep the program running
}
