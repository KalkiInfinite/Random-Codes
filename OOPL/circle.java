import java.util.*;
import java.lang.Math;

class Exp1 {
    public static void main(String[] args) {
        Scanner object = new Scanner(System.in);
        System.out.print("Enter the radius: ");
        double radius = object.nextDouble();

        if (radius < 0) {
            System.out.print("Invalid input. Please enter correct input.");
        } else {
            double perimeter = 2 * Math.PI * radius;
            double area = Math.PI * radius * radius;
            System.out.print("Perimeter of the circle is " + perimeter);
            System.out.print("Area of the circle is " + area);
        }
    }
}
