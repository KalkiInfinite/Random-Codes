import java.io.*;

public class Test {
    public static void main(String args[]) {
        try {
            FileInputStream fis = new FileInputStream("input.txt");
            BufferedInputStream bis = new BufferedInputStream(fis);
            int data;

            System.out.println("Reading with FileInputStream:");
            while ((data = fis.read()) != -1) {
                System.out.print((char) data);
            }
            System.out.println();

            System.out.println("Reading with BufferedInputStream:");
            while ((data = bis.read()) != -1) {
                System.out.print((char) data);
            }

            fis.close();
            bis.close();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
