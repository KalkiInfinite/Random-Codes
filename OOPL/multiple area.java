import java.util.*;

class Rectangle {
    double length, breadth;

    Rectangle(double l, double b) {
        length = l;
        breadth = b;
    }

    void printPerimeter() {
        System.out.println("Rectangle Perimeter = " + 2 * (length + breadth));
    }

    void printArea() {
        System.out.println("Rectangle Area = " + length * breadth);
    }
}

class Square extends Rectangle {
    double side;

    Square(double s) {
        super(s, s);
        side = s; 
    }

    @Override
    void printPerimeter() {
        System.out.println("Square Perimeter = " + 4 * side);
    }

    @Override
    void printArea() {
        System.out.println("Square Area = " + side * side);
    }
}

public class Main {
    public static void main(String args[]) {
        Square s[] = new Square[10];

        if (args.length == 10) {
            for (int i = 0; i < 10; i++) {
                s[i] = new Square(Double.parseDouble(args[i]));
            }

            for (int i = 0; i < 10; i++) {
                System.out.println("\nObject " + (i + 1) + ": ");
                s[i].printPerimeter();
                s[i].printArea();
            }
        } else {
            System.out.println("Error: " + args.length + " arguments entered but 10 needed.");
        }
    }
}
