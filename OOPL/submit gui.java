import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class UserForm extends JFrame implements ActionListener {
    JLabel nameLabel, departmentLabel, phoneLabel, genderLabel, selfLabel;
    JTextField nameField, phoneField;
    JComboBox<String> departmentField;
    JPanel genderPanel;
    JRadioButton maleField, femaleField;
    JTextArea selfField;
    JScrollPane scrollBar;
    JButton submitButton;
    Font myFont = new Font("Ariel Nova Light", Font.BOLD, 15);

    UserForm() {
        this.setSize(700, 700);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null);
        this.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(15, 10, 15, 10);

        // Name Label and Field
        nameLabel = new JLabel("Name");
        nameLabel.setFont(myFont);
        nameLabel.setPreferredSize(new Dimension(130, 25));
        gbc.gridx = 0;
        gbc.gridy = 0;
        this.add(nameLabel, gbc);

        nameField = new JTextField();
        nameField.setFont(myFont);
        nameField.setPreferredSize(new Dimension(270, 25));
        gbc.gridx = 1;
        gbc.gridy = 0;
        this.add(nameField, gbc);

        // Department Label and Field
        departmentLabel = new JLabel("Department");
        departmentLabel.setFont(myFont);
        departmentLabel.setPreferredSize(new Dimension(130, 25));
        gbc.gridx = 0;
        gbc.gridy = 1;
        this.add(departmentLabel, gbc);

        String departments[] = {
            "Computer Science",
            "Electronics and Computer",
            "Electronics and Telecommunication",
            "Information Technology",
            "Mechanical"
        };
        departmentField = new JComboBox<>(departments);
        departmentField.setFont(myFont);
        departmentField.setPreferredSize(new Dimension(270, 25));
        gbc.gridx = 1;
        gbc.gridy = 1;
        this.add(departmentField, gbc);

        // Phone Label and Field
        phoneLabel = new JLabel("Phone");
        phoneLabel.setFont(myFont);
        phoneLabel.setPreferredSize(new Dimension(130, 25));
        gbc.gridx = 0;
        gbc.gridy = 2;
        this.add(phoneLabel, gbc);

        phoneField = new JTextField();
        phoneField.setFont(myFont);
        phoneField.setPreferredSize(new Dimension(270, 25));
        gbc.gridx = 1;
        gbc.gridy = 2;
        this.add(phoneField, gbc);

        // Gender Label and Panel
        genderLabel = new JLabel("Gender");
        genderLabel.setFont(myFont);
        genderLabel.setPreferredSize(new Dimension(130, 25));
        gbc.gridx = 0;
        gbc.gridy = 3;
        this.add(genderLabel, gbc);

        genderPanel = new JPanel();
        genderPanel.setLayout(new GridLayout(1, 2));
        gbc.gridx = 1;
        gbc.gridy = 3;
        this.add(genderPanel, gbc);

        maleField = new JRadioButton("Male");
        maleField.setFont(myFont);
        femaleField = new JRadioButton("Female");
        femaleField.setFont(myFont);

        ButtonGroup genderField = new ButtonGroup();
        genderField.add(maleField);
        genderField.add(femaleField);

        genderPanel.add(maleField);
        genderPanel.add(femaleField);

        // About Yourself Label and Field
        selfLabel = new JLabel("About Yourself");
        selfLabel.setFont(myFont);
        selfLabel.setPreferredSize(new Dimension(130, 25));
        gbc.gridx = 0;
        gbc.gridy = 4;
        this.add(selfLabel, gbc);

        selfField = new JTextArea(5, 19);
        selfField.setFont(myFont);
        selfField.setLineWrap(true);
        scrollBar = new JScrollPane(selfField);
        gbc.gridx = 1;
        gbc.gridy = 4;
        this.add(scrollBar, gbc);

        // Submit Button
        submitButton = new JButton("Submit");
        submitButton.setFont(myFont);
        submitButton.setPreferredSize(new Dimension(100, 25));
        submitButton.addActionListener(this);
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.CENTER;
        this.add(submitButton, gbc);

        this.pack();
        this.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == submitButton) {
            String name = nameField.getText();
            if (name.isEmpty()) {
                JOptionPane.showMessageDialog(
                    this,
                    "Do not leave the name field empty.",
                    "Error",
                    JOptionPane.WARNING_MESSAGE
                );
            } else {
                String department = (String) departmentField.getSelectedItem();
                JOptionPane.showMessageDialog(
                    this,
                    "Name: " + name + "\nDepartment: " + department,
                    "Submission Successful",
                    JOptionPane.PLAIN_MESSAGE
                );
            }
        }
    }

    public static void main(String args[]) {
        UserForm window = new UserForm();
        window.setTitle("Form");
    }
}
