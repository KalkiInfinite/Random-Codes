import java.util.Scanner;

public class MySeries {
    public double power(double x, int n) {
        double result = 1.0;
        for (int i = 1; i <= n; i++) {
            result *= x;
        }
        return result;
    }

    public int factorial(int num) {
        if (num == 0 || num == 1) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }

    public double sumSeries(double x, int n) {
        double sum = 1.0;
        for (int i = 1; i <= n; i++) {
            sum += power(x, i) / factorial(i);
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the value of x: ");
        double x = scanner.nextDouble();
        System.out.print("Enter the value of n: ");
        int n = scanner.nextInt();
        
        Series series = new Series();
        double result = series.sumSeries(x, n);
        System.out.println("Result of the series: " + result);
        
        scanner.close();
    }
}