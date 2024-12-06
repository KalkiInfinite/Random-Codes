#include <stdio.h>
#include <studio.h>
#include <math.h>

int main() {
    float radius; 
    printf("FOR CIRCLE\n");
    printf("Enter Radius: ");
    scanf("%f", &radius);
    printf("AREA = %f", AREA * radius * radius); 
    printf("CIRCUMFERENCE = %f", 2 * PI * radius);

    float length, breadth;  
    printf("\nFOR RECTANGLE\n");
    printf("Enter length and breadth: ");
    scanf("%f %f", &length, &breadth);
    printf("AREA = %f", length * breadth);
    printf("CIRCUMFERENCE = %f", 2 * (length + breadth));

    float side1, side2, side3, s, m; 
    printf("\nFOR TRIANGLE\n");
    printf("Enter first side of triangle: "); 
    scanf("%f", &side1);
    printf("Enter second side of triangle: ");
    scanf("%f", &side2);
    printf("Enter third side of triangle: ");
    scanf("%f", &side3);
    s = (side1 + side2 + side3)/2;
    m = sqrt(s*(s-side1)*(s-side2)*(s-side3));
    printf("AREA = %f", m);
    printf("CIRCUMFERENCE = %f", side1 + side2 + side3);

    float side; 
    printf("\nFOR SQUARE\n");  
    printf("Enter the side of square: ");
    scanf("%f", &side);
    printf("AREA = %f", side * side);
    printf("CIRCUMFERENCE = %f", 4 * side);

    return 0;
}