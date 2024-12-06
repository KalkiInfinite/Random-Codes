import java.util.*;
class Exp1pl2 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        int r, s = 0, t = n;
        while (t > 0) {
            r = t % 10;
            s += r * r * r;
            t = t / 10;
        }
        if (s == n) {
            System.out.println(n + " is an Armstrong number.");
        } else {
            System.out.println(n + " is not an Armstrong number.");
        }
    }
}
