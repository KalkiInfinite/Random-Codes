import java.util.*;
class Exp1pl1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int x, y, z;
        System.out.print("Enter x: ");
        x = sc.nextInt();
        System.out.print("Enter y: ");
        y = sc.nextInt();
        System.out.print("Enter z: ");
        z = sc.nextInt();
        if (x > y && x > z) {
            System.out.println("x is the largest number");
        } else if (y > x && y > z) {
            System.out.println("y is the largest number");
        } else {
            System.out.println("z is the largest number");
        }
    }
}
