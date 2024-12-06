import java.awt.*;
import javax.swing.*;

class DrawPanel extends JPanel {
    DrawPanel() {
        this.setPreferredSize(new Dimension(500, 300));
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        Graphics2D g2D = (Graphics2D) g;

        g2D.setStroke(new BasicStroke(5));
        g2D.setFont(new Font("Arial Nova Light", Font.BOLD, 20));

        g2D.setPaint(Color.red);
        g2D.fillOval(20, 40, 120, 150);
        g2D.setPaint(Color.black);
        g2D.drawString("Oval", 60, 240);

        g2D.setPaint(Color.green);
        g2D.fillRect(180, 40, 120, 150);
        g2D.setPaint(Color.black);
        g2D.drawString("Rectangle", 193, 240);

        g2D.setPaint(Color.blue);
        g2D.drawLine(340, 115, 460, 115);
        g2D.setPaint(Color.black);
        g2D.drawString("Line", 377, 240);
    }
}

public class DrawShapes {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Drawing");
        frame.setSize(500, 320);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

        DrawPanel panel = new DrawPanel();
        frame.add(panel);
        frame.setVisible(true);
    }
}
