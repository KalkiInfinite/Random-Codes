import java.io.*;

public class Exp7 {
    public static void main(String args[]) {
        try {
            InputStreamReader ir = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(ir);
            
            System.out.print("Enter file path to read: ");
            File rfile = new File(br.readLine());
            
            System.out.print("Enter file path to write: ");
            File wfile = new File(br.readLine());
            
            br.close();
            ir.close();

            if (rfile.isFile() && wfile.isFile()) {
                FileInputStream input = new FileInputStream(rfile);
                byte data[] = new byte[input.available()];
                input.read(data);
                input.close();
                rfile = null;
                FileOutputStream output = new FileOutputStream(wfile);
                output.write(data);
                output.close();
                wfile = null;
                System.out.println("Bytes successfully copied.");
            } else {
                System.out.println("Error: Invalid file path provided.");
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
