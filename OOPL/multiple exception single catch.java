class Exp6b {
    public static void main(String[] args) {
        try {
            int number1 = Integer.parseInt(args[0]);
            int number2 = Integer.parseInt(args[1]);
            int result = number1 / number2;
            System.out.println("Result: " + result);
        } catch (NumberFormatException | ArithmeticException e) {
            System.out.println("Invalid number format: " + e);
        }
    }
}
