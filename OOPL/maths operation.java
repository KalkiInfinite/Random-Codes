import java.util.Scanner;

public class Fraction {
    private int numerator;
    private int denominator;

    public Fraction(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
    
    public Fraction sum(Fraction other) {
        int commonDenominator = lcm(this.denominator, other.denominator);
        int sumNumerator = (this.numerator * (commonDenominator / this.denominator )) + ( other.numerator * (commonDenominator / other.denominator));
        return new Fraction(sumNumerator, commonDenominator);
    }

    public Fraction difference(Fraction other) {
        int commonDenominator = lcm(this.denominator, other.denominator);
        int diffNumerator = (this.numerator * (commonDenominator / this.denominator)) - (other.numerator * (commonDenominator / other.denominator));
        return new Fraction(diffNumerator, commonDenominator);
    }

    public Fraction product(Fraction other) {
        int productNumerator = this.numerator * other.numerator;
        int productDenominator = this.denominator * other.denominator;
        return new Fraction(productNumerator, productDenominator);
    }

    public Fraction division(Fraction other) {
        int divisionNumerator = this.numerator * other.denominator;
        int divisionDenominator = this.denominator * other.numerator;
        return new Fraction(divisionNumerator, divisionDenominator);
    }

    public int getGCD() {
        return gcd(this.numerator,this.denominator);
    }

    public int getLCM(Fraction other) {
        return gcd(this.denominator, other.denominator);
    }

    public String toString() {
        return numerator + "/" + denominator;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the numerator of fraction 1: ");
        int numerator1 = scanner.nextInt();
        System.out.print("Enter the denominator of fraction 1: ");
        int denominator1 = scanner.nextInt();
        Fraction fraction1 = new Fraction(numerator1, denominator1);

        System.out.print("Enter the numerator of fraction 2: ");
        int numerator2 = scanner.nextInt();
        System.out.print("Enter the denominator of fraction 2: ");
        int denominator2 = scanner.nextInt();
        Fraction fraction2 = new Fraction(numerator2, denominator2);

        Division division = new Division(fraction1, fraction2);
        Fraction result = division.getDi();
        Fraction inverse = division.getII();

        System.out.println("Difference: " + fraction1.difference(fraction2));
        System.out.println("Product: " + fraction1.product(fraction2));
        System.out.println("Division: " + result);
        System.out.println("Inverse: " + inverse);
        System.out.println("Sum: " + fraction1.sum(fraction2));

        scanner.close();
    }
}