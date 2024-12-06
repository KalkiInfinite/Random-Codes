import java.io.*;

public class Exp4 {
    static void printFiles(File directory, String space) {
        File files[] = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    System.out.println(space + file.getName() + "/");
                    printFiles(file, space + "  ");
                } else {
                    System.out.println(space + file.getName());
                }
            }
        }
    }

    public static void main(String args[]) {
        try {
            InputStreamReader ir = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(ir);
            System.out.print("Enter directory path: ");
            String directory_path = br.readLine();
            File directory = new File(directory_path);
            if (directory.isDirectory()) {
                printFiles(directory, "");
            } else {
                System.out.println("Error: Provided path is not a valid directory.");
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}