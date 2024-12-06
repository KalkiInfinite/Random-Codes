import java.io.*;
import java.util.StringTokenizer;

public class Test {
    public static void main(String args[]) {
        int line_count = 0, word_count = 0, char_count = 0;

        try {
            FileReader fr = new FileReader(args[0]);
            BufferedReader br = new BufferedReader(fr);
            String line;
            while ((line = br.readLine()) != null) {
                line_count++;
                StringTokenizer st = new StringTokenizer(line, " ");
                while (st.hasMoreTokens()) {
                    word_count++;
                    st.nextToken();
                }
                char_count += line.length();
            }
            br.close();
            fr.close();
            System.out.println("Line count = " + line_count);
            System.out.println("Word count = " + word_count);
            System.out.println("Character count = " + char_count);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
