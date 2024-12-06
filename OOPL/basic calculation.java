import java.util.*;

class Exp1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();

        if (n > 0) {
            String nums = "";
            int sum = 0;
            for (int i = 0; i < n; i++) {
                if (2 * i % 3 == 0) {
                    nums = nums + "+" + 2 * i;
                    sum = sum + 2 * i;
                }
            }
            System.out.println("Sum = " + nums.substring(1) + " = " + sum);
        } else {
            System.out.println("Error: Invalid input. Number should be positive.");
        }
    }
}
