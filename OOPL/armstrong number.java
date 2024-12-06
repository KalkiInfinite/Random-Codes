import java.util.*;
class Exp1p2{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        int t = n, r, s=0;
        while(t > 0) {
            r = t%10;
            s = s + r*r*r;
            t = t/10;
        }
        if(n == s)
            System.out.println(n + " is an armstrong number");
        else
            System.out.println(n + " is not an armstrong number");
    }
}