class Number {
    protected int a, b;

    public Number(int a, int b) {
        this.a = a;
        this.b = b;
    }
}

class Fraction extends Number {
    public Fraction(int numerator, int denominator) {
        super(numerator, denominator);
    }

    public Fraction add(Fraction other) {
        int newNumerator = (this.a * other.b) + (other.a * this.b);
        int newDenominator = this.b * other.b;
        return new Fraction(newNumerator, newDenominator).simplify();
    }

    public Fraction subtract(Fraction other) {
        int newNumerator = (this.a * other.b) - (other.a * this.b);
        int newDenominator = this.b * other.b;
        return new Fraction(newNumerator, newDenominator).simplify();
    }

    // Simplify the fraction using GCD
    private Fraction simplify() {
        int gcd = gcd(Math.abs(a), Math.abs(b));
        return new Fraction(a / gcd, b / gcd);
    }

    private int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }

    @Override
    public String toString() {
        return a + "/" + b;
    }
}

class Vector {
    private int i, j, k;

    public Vector(int i, int j, int k) {
        this.i = i;
        this.j = j;
        this.k = k;
    }

    public Vector add(Vector other) {
        int newI = this.i + other.i;
        int newJ = this.j + other.j;
        int newK = this.k + other.k;
        return new Vector(newI, newJ, newK);
    }

    public Vector subtract(Vector other) {
        int newI = this.i - other.i;
        int newJ = this.j - other.j;
        int newK = this.k - other.k;
        return new Vector(newI, newJ, newK);
    }

    @Override
    public String toString() {
        return "(" + i + ", " + j + ", " + k + ")";
    }
}

public class Main {
    public static void main(String[] args) {
        Fraction fraction1 = new Fraction(1, 2);
        Fraction fraction2 = new Fraction(3, 4);

        System.out.println("Fraction 1: " + fraction1);
        System.out.println("Fraction 2: " + fraction2);

        Fraction sum = fraction1.add(fraction2);
        Fraction difference = fraction1.subtract(fraction2);

        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);

        Vector vector1 = new Vector(1, 2, 3);
        Vector vector2 = new Vector(4, 5, 6);

        System.out.println("Vector 1: " + vector1);
        System.out.println("Vector 2: " + vector2);

        Vector vectorSum = vector1.add(vector2);
        Vector vectorDifference = vector1.subtract(vector2);

        System.out.println("Vector Sum: " + vectorSum);
        System.out.println("Vector Difference: " + vectorDifference);
    }
}
