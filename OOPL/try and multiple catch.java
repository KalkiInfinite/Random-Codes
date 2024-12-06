class Exp6a {
    public static void main(String[] args) {
        try {
            int number1 = Integer.parseInt(args[0]);
            int number2 = Integer.parseInt(args[1]);
            int result = number1 / number2;
            System.out.println("Result: " + result);
        } catch (NumberFormatException e) {
            System.out.println("Invalid number format: " + e);
        } catch (ArithmeticException e) {
            System.out.println("Invalid number format: " + e);
        }
    }
}
