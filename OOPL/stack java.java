import java.util.*;

interface Stack {
    boolean empty();
    boolean full();
    void push(int n);
    int pop();
    void display();
}

public class Stacking implements Stack {
    static final int size = 100;
    int stackarr[] = new int[size]; 
    int top = -1;

    public boolean empty() { 
        return top == -1;
    }

    public boolean full() {
        return top == size - 1;
    }

    public void push(int n) {
        if (full()) {
            System.out.println("Error: Stack overflow.");
            return;
        }
        stackarr[++top] = n;
    }

    public int pop() {
        if (empty()) {
            System.out.println("Error: Stack underflow.");
            return -1;
        }
        return stackarr[top--];
    }

    public void display() {
        if (top == -1) {
            System.out.println("Stack is empty.");
            return;
        }
        System.out.print("Stack: ");
        for (int i = 0; i <= top; i++) {
            System.out.print(stackarr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        if (args.length != 5) {
            System.out.println("Error: " + args.length + " inputs given but 5 needed.");
            return;
        }

        Stacking stack = new Stacking();
        Scanner sc = new Scanner(System.in);
        int choice;

        while (true) {
            System.out.print("\n1: PUSH\n 2: POP\n 3: DISPLAY\n 4: EXIT\n\nEnter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter number: ");
                    stack.push(sc.nextInt());
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    stack.display();
                    break;
                case 4:
                    System.out.println("Program successfully terminated.");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Error: Invalid input. Try again.");
            }
        }
    }
}