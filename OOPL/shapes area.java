public class ShapeAreaCalculator {
    abstract static class Shape {
        int a1, a2;
        
        Shape(int a1, int a2) {
            this.a1 = a1;
            this.a2 = a2;
        }
        
        abstract void printArea();
    }

    static class Rectangle extends Shape {
        Rectangle(int a1, int a2) {
            super(a1, a2);
        }
        
        void printArea() {
            System.out.println("Rectangle area = " + (float)(a1 * a2));
        }
    }

    static class Triangle extends Shape {
        Triangle(int a1, int a2) {
            super(a1, a2);
        }
        
        void printArea() {
            System.out.println("Triangle area = " + (0.5 * a1 * a2));
        }
    }

    static class Circle extends Shape {
        Circle(int a1) {
            super(a1, a1);
        }
        
        void printArea() {
            System.out.println("Circle area = " + (Math.PI * a1 * a1));
        }
    }

    public static void main(String[] args) {
        if (args.length == 5) {
            int l = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            Rectangle r1 = new Rectangle(l, b);
            r1.printArea();

            int h = Integer.parseInt(args[2]);
            int triangleBase = Integer.parseInt(args[3]);
            Triangle t1 = new Triangle(h, triangleBase);
            t1.printArea();

            int r = Integer.parseInt(args[4]);
            Circle c1 = new Circle(r);
            c1.printArea();
        } else {
            System.out.println("Error: " + args.length + " inputs given but 5 needed.");
        }
    }
}