import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class CalcFrame extends JFrame {
    CalcFrame() {
        this.setTitle("Simple Calculator");
        this.setResizable(false);
        this.setLayout(new BorderLayout(3, 3));
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}

public class Calculator implements ActionListener {
    CalcFrame frame;
    JTextField textExpression;
    JPanel buttonPanel, erasePanel;
    JButton numButtons[] = new JButton[10];
    JButton funcButtons[] = new JButton[6];
    JButton delButton, clrButton;

    double num1, num2, result;
    char funcOperators[] = { '+', '-', '*', '/', '%', '=' };
    char operator;

    Font myFont = new Font("Arial Nova Light", Font.BOLD, 30);
    Color bgColour = new Color(0x00EDFF);
    Color textColour = new Color(0x00FF00);
    Color buttonColour = new Color(0xFFFFFF);
    Color errColour = new Color(0xDE1738);

    Calculator() {
        frame = new CalcFrame();

        textExpression = new JTextField();
        textExpression.setPreferredSize(new Dimension(300, 50));
        textExpression.setFont(myFont);
        textExpression.setBackground(new Color(20, 20, 20));
        textExpression.setForeground(textColour);
        textExpression.setEditable(false);
        textExpression.setFocusable(false);

        buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(4, 4, 3, 3));

        for (int i = 0; i < numButtons.length; i++) {
            numButtons[i] = new JButton(Integer.toString(i));
            numButtons[i].setFont(myFont);
            numButtons[i].setBackground(bgColour);
            numButtons[i].setForeground(textColour);
            numButtons[i].setFocusable(false);
            numButtons[i].addActionListener(this);
        }

        for (int i = 0; i < funcButtons.length; i++) {
            funcButtons[i] = new JButton("" + funcOperators[i]);
            funcButtons[i].setFont(myFont);
            funcButtons[i].setBackground(bgColour);
            funcButtons[i].setForeground(textColour);
            funcButtons[i].setFocusable(false);
            funcButtons[i].addActionListener(this);
        }

        buttonPanel.add(numButtons[1]);
        buttonPanel.add(numButtons[2]);
        buttonPanel.add(numButtons[3]);
        buttonPanel.add(funcButtons[0]);
        buttonPanel.add(numButtons[4]);
        buttonPanel.add(numButtons[5]);
        buttonPanel.add(numButtons[6]);
        buttonPanel.add(funcButtons[1]);
        buttonPanel.add(numButtons[7]);
        buttonPanel.add(numButtons[8]);
        buttonPanel.add(numButtons[9]);
        buttonPanel.add(funcButtons[2]);
        buttonPanel.add(funcButtons[3]);
        buttonPanel.add(numButtons[0]);
        buttonPanel.add(funcButtons[4]);
        buttonPanel.add(funcButtons[5]);

        erasePanel = new JPanel();
        erasePanel.setLayout(new GridLayout(1, 2));

        delButton = new JButton("del");
        delButton.setFont(myFont);
        delButton.setBackground(bgColour);
        delButton.setForeground(textColour);
        delButton.setFocusable(false);
        delButton.addActionListener(this);

        clrButton = new JButton("C");
        clrButton.setFont(myFont);
        clrButton.setBackground(bgColour);
        clrButton.setForeground(textColour);
        clrButton.setFocusable(false);
        clrButton.addActionListener(this);

        erasePanel.add(delButton);
        erasePanel.add(clrButton);

        frame.add(textExpression, BorderLayout.NORTH);
        frame.add(buttonPanel, BorderLayout.CENTER);
        frame.add(erasePanel, BorderLayout.SOUTH);
        frame.pack();
        frame.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < numButtons.length; i++) {
            if (e.getSource() == numButtons[i]) {
                textExpression.setText(textExpression.getText() + Integer.toString(i));
            }
        }

        try {
            for (int i = 0; i < funcButtons.length; i++) {
                if (e.getSource() == funcButtons[i]) {
                    if (i == 3) {
                        textExpression.setText(textExpression.getText() + funcOperators[i]);
                        continue;
                    } else if (i == 4) {
                        num2 = Double.parseDouble(textExpression.getText());
                        if (num2 == 0.0) {
                            throw new ArithmeticException();
                        }
                        switch (operator) {
                            case '+':
                                result = num1 + num2;
                                break;
                            case '-':
                                result = num1 - num2;
                                break;
                            case '*':
                                result = num1 * num2;
                                break;
                            case '/':
                                result = num1 / num2;
                                break;
                            case '=':
                                result = Double.parseDouble(textExpression.getText());
                                break;
                            default:
                                break;
                        }
                        textExpression.setText(Double.toString(result));
                        num1 = result;
                        operator = '=';
                        textExpression.setForeground(textColour);
                    }
                }
            }
        } catch (Exception error) {
            textExpression.setForeground(errColour);
            textExpression.setText("Error");
            num1 = num2 = result = 0;
        }

        if (e.getSource() == delButton) {
            String text = textExpression.getText();
            textExpression.setText(text.substring(0, (text.length() > 0) ? (text.length() - 1) : 0));
        }

        if (e.getSource() == clrButton) {
            textExpression.setText("");
        }
    }

    public static void main(String args[]) {
        Calculator calculator = new Calculator();
    }
}
