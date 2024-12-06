import java.util.*;

interface Student {
    void displayStudentInfo();
}

interface Teacher {
    void displayTeacherInfo();
}

class College implements Student, Teacher {
    int studentrollno;
    String studentyear;
    String studentname;
    String studentbranch;
    int teacherid;
    String teachername;
    String teachersubject;

    public void displayStudentInfo() {
        System.out.println("Student Roll no. : " + studentrollno);
        System.out.println("Student Academic Year : " + studentyear);
        System.out.println("Student Name : " + studentname);
        System.out.println("Student Branch Name : " + studentbranch);
    }

    public void displayTeacherInfo() {
        System.out.println("Teacher Id no. : " + teacherid);
        System.out.println("Teacher Name : " + teachername);
        System.out.println("Teacher Subject : " + teachersubject);
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int choice;

        while (true) {
            System.out.print("\n1: PUSH\n 2: POP\n 3: DISPLAY\n 4: EXIT\n\nEnter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter Student Roll no. : ");
                    int a = sc.nextInt();
                    System.out.print("Enter Student Year of Study : ");
                    String b = sc.nextLine();
                    System.out.print("Enter Student Name : ");
                    String c = sc.nextLine();
                    System.out.print("Enter Student Branch Name : ");
                    String d = sc.nextLine();
                    College obj1 = new College(a, b, c, d);
                    obj1.displayStudentInfo();
                    break;
                case 2:
                    System.out.print("Enter Teacher Id no. : ");
                    int e = sc.nextInt();
                    System.out.print("Enter Teacher Name : ");
                    String f = sc.nextLine();
                    System.out.print("Enter Teacher Subject : ");
                    String g = sc.nextLine();
                    College obj2 = new College(e, f, g);
                    obj2.displayTeacherInfo();
                    break;
                case 3:
                    College obj3 = new College(a, b, c, d, e, f, g);
                    obj3.displayStudentInfo();
                    obj3.displayTeacherInfo();
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