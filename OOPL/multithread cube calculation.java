import java.util.*;

class Numgen extends Thread
{
    public void run()
    {
        Random random = new Random();
        while (true)
        {
            int number = random.nextInt(28);
            System.out.println("RANDOM NUMBER : " + number);
            if (number % 2 == 0)
            {
                System.out.println("Square of EVEN number " + number + " is : " + number * number);
            }
            else
            {
                System.out.println("Cube of ODD number " + number + " is : " + number * number * number);
            }
            try
            {
                Thread.sleep(1000);
            }
            catch (InterruptedException e)
            {
                System.out.println(e);
            }
        }
    }
}

public class Exp8ver1
{
    public static void main(String[] args)
    {
        Numgen object = new Numgen();
        object.start();
    }
}