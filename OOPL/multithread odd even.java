import java.util.Random;

class Numgen implements Runnable {
    public void run() {
        Random random = new Random();
        while (true) {
            int number = random.nextInt(40) - 20;
            if (number < 0) {
                System.out.println("NEGATIVE NUMBER: " + number);
            } else if (number > 0 && number % 2 == 0) {
                System.out.println("POSITIVE EVEN NUMBER: " + number);
            } else {
                System.out.println("POSITIVE ODD NUMBER: " + number);
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

public class Exp8 {
    public static void main(String[] args) {
        Numgen object = new Numgen();
        Thread thread = new Thread(object);
        thread.start();
    }
}