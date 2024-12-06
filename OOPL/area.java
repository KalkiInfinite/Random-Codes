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
    Square(double s) {
        super(s, s);
    }
    void printPerimeter() {
        System.out.println("Square Perimeter = " + 4 * side);
    }
    void printArea() {
        System.out.println("Square Area = " + side * side);
    }
}
public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter side: ");
    double s = sc.nextDouble();
    Square sq1 = new Square(s);
    sq1.printPerimeter();
    sq1.printArea();
    System.out.print("Enter length: ");
    double l = sc.nextDouble();
    System.out.print("Enter breadth: ");
    double b = sc.nextDouble();
    Rectangle r1 = new Rectangle(l, b);
    r1.printPerimeter();
    r1.printArea();
    sc.close();
}