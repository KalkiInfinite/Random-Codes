import java.io.*;

public class Exp7 {
    public static void main(String args[]) {
        if (args.length == 1) {
            try {
                File file = new File(args[0]);
                FileWriter output = new FileWriter(file, true);
                
                InputStreamReader ir = new InputStreamReader(System.in);
                BufferedReader br = new BufferedReader(ir);
                
                System.out.print("Enter data: ");
                String data = br.readLine();
                
                br.close();
                ir.close();
                
                output.write(data);
                output.close();
                file = null;
                
                System.out.println("Data successfully appended to " + args[0]);
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        } else {
            System.out.println("Error: " + args.length + " arguments provided but 1 required.");
        }
    }
}
