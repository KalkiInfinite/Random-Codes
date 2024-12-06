import java.util.*;
class Exp1p1{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int x, y, z;
        System.out.print("Enter x: ");
        x = sc.nextInt();
        System.out.print("Enter y: ");
        y = sc.nextInt();
        System.out.print("Enter z: ");
        z = sc.nextInt();
        if(x >= y && x >= z) 
            System.out.println("X is the largest number");
        else if(y >= x && y >= z)
            System.out.println("Y is the largest number");
        else
            System.out.println("Z is the largest number");
    }
}