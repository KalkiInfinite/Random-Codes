public class Piyush {
    public static void main(String[] args) {
        int n1 = Integer.parseInt(args[0]);
        int n2 = Integer.parseInt(args[1]);

        int HCF = hcf(n1, n2);
        int LCM = (n1 * n2) / HCF;

        System.out.print("LCM is: " + LCM);
        System.out.print(" HCF is: " + HCF);
    }

    static int hcf(int n1, int n2) {
        if (n2 != 0)
            return hcf(n2, n1 % n2);
        else
            return n1;
    }
}
