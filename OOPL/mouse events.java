import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class MouseEvents extends JFrame implements MouseListener {
    JLabel displayLabel;
    Font myFont = new Font("Arial Nova Light", Font.BOLD, 30);
    Color bgColour = new Color(0x000000);
    Color fgColour = new Color(0x00FF00);

    MouseEvents() {
        this.setTitle("Mouse Events");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500, 420);
        this.setLayout(new BorderLayout()); // Ensures layout is set

        displayLabel = new JLabel("Welcome");
        displayLabel.setBackground(bgColour);
        displayLabel.setForeground(fgColour);
        displayLabel.setOpaque(true);
        displayLabel.setFont(myFont);
        displayLabel.setHorizontalAlignment(JLabel.CENTER);
        displayLabel.setVerticalAlignment(JLabel.CENTER);

        this.addMouseListener(this); // Registers the JFrame to listen for mouse events
        this.add(displayLabel, BorderLayout.CENTER); // Adds label to center of the frame
        this.setVisible(true);
    }

    void displayEvent(String eventName) {
        displayLabel.setText("Mouse Event: " + eventName);
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        displayEvent("Mouse Clicked");
    }

    @Override
    public void mousePressed(MouseEvent e) {
        displayEvent("Mouse Pressed");
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        displayEvent("Mouse Released");
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        displayEvent("Mouse Entered");
    }

    @Override
    public void mouseExited(MouseEvent e) {
        displayEvent("Mouse Exited");
    }

    public static void main(String args[]) {
        MouseEvents window = new MouseEvents();
    }
}
