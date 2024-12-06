interface Product {
    double getPrice();
    String getDescription();
}

class Electronics implements Product {
    private String name;
    private double price;

    public Electronics(String name, double price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public String getDescription() {
        return "Electronic product: " + name;
    }
}

class Clothing implements Product {
    private String type;
    private double price;

    public Clothing(String type, double price) {
        this.type = type;
        this.price = price;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public String getDescription() {
        return "Clothing item: " + type;
    }
}

class Books implements Product {
    private String title;
    private String author;
    private double price;

    public Books(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public String getDescription() {
        return "Book: \"" + title + "\" by " + author;
    }
}

public class Main {
    public static void main(String[] args) {
        Product electronicProduct = new Electronics("Smartphone", 599.99);
        Product clothingItem = new Clothing("T-shirt", 19.99);
        Product book = new Books("The Catcher in the Rye", "J.D. Salinger", 9.99);

        displayProductDetails(electronicProduct);
        displayProductDetails(clothingItem);
        displayProductDetails(book);
    }

    public static void displayProductDetails(Product product) {
        System.out.println("Description: " + product.getDescription());
        System.out.println("Price: $" + product.getPrice());
        System.out.println();
    }
}
