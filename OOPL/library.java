interface LibraryItem {
    void checkout();
    void returnItem();
}

class Book implements LibraryItem {
    private String title;
    private boolean checkedOut;

    public Book(String title) {
        this.title = title;
        this.checkedOut = false;
    }

    @Override
    public void checkout() {
        if (!checkedOut) {
            checkedOut = true;
            System.out.println("Checked out: " + title);
        } else {
            System.out.println(title + " is already checked out.");
        }
    }

    @Override
    public void returnItem() {
        if (checkedOut) {
            checkedOut = false;
            System.out.println("Returned: " + title);
        } else {
            System.out.println(title + " is not currently checked out.");
        }
    }
}

class DVD implements LibraryItem {
    private String title;
    private boolean checkedOut;

    public DVD(String title) {
        this.title = title;
        this.checkedOut = false;
    }

    @Override
    public void checkout() {
        if (!checkedOut) {
            checkedOut = true;
            System.out.println("Checked out: " + title);
        } else {
            System.out.println(title + " is already checked out.");
        }
    }

    @Override
    public void returnItem() {
        if (checkedOut) {
            checkedOut = false;
            System.out.println("Returned: " + title);
        } else {
            System.out.println(title + " is not currently checked out.");
        }
    }
}

public class LibrarySimulation {
    public static void main(String[] args) {
        Book book1 = new Book("The Great Gatsby");
        DVD dvd1 = new DVD("Inception");

        book1.checkout();
        dvd1.checkout();
        book1.returnItem();
        dvd1.returnItem();
    }
}
