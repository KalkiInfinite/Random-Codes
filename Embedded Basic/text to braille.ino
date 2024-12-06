int braille[26][6] = {
  {1, 0, 0, 0, 0, 0}, // A
  {1, 1, 0, 0, 0, 0}, // B
  {1, 0, 0, 1, 0, 0}, // C
  {1, 0, 0, 1, 1, 0}, // D
  {1, 0, 0, 0, 1, 0}, // E
  {1, 1, 0, 1, 0, 0}, // F
  {1, 1, 0, 1, 1, 0}, // G
  {1, 1, 0, 0, 1, 0}, // H
  {0, 1, 0, 1, 0, 0}, // I
  {0, 1, 0, 1, 1, 0}, // J
  {1, 0, 1, 0, 0, 0}, // K
  {1, 1, 1, 0, 0, 0}, // L
  {1, 0, 1, 1, 0, 0}, // M
  {1, 0, 1, 1, 1, 0}, // N
  {1, 0, 1, 0, 1, 0}, // O
  {1, 1, 1, 1, 0, 0}, // P
  {1, 1, 1, 1, 1, 0}, // Q
  {1, 1, 1, 0, 1, 0}, // R
  {0, 1, 1, 1, 0, 0}, // S
  {0, 1, 1, 1, 1, 0}, // T
  {1, 0, 1, 0, 0, 1}, // U
  {1, 1, 1, 0, 0, 1}, // V
  {0, 1, 0, 1, 1, 1}, // W
  {1, 0, 1, 1, 0, 1}, // X
  {1, 0, 1, 1, 1, 1}, // Y
  {1, 0, 1, 0, 1, 1}  // Z
};

int controlPins[6] = {2, 3, 4, 5, 6, 7};

int buttonPin = 8;

char alphabet[] = "abcdefghijklmnopqrstuvwxyz";

String text = "hello";

char letter;
int index;
int length = text.length();

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 6; i++) {
    pinMode(controlPins[i], OUTPUT);
  }

  pinMode(buttonPin, INPUT);
}

void loop() {
  for (int i = 0; i < length; i++) {
    letter = text[i];
    
    for (int j = 0; j < 26; j++) {
      if (letter == alphabet[j]) {
        index = j;
        break;
      }
    }

    Serial.print(letter);
    Serial.print(" ");
    Serial.println(index);
    
    for (int k = 0; k < 6; k++) {
      digitalWrite(controlPins[k], braille[index][k]);
    }

    while (digitalRead(buttonPin) == LOW) {}
    delay(1000);
  }
}
