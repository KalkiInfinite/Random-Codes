import java.util.Scanner;

public class RectanglePerimeter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] coordinates = new int[4][2];

        System.out.println("Enter coordinates of four points (x, y):");
        for (int i = 0; i < 4; i++) {
            System.out.print("Point " + (i + 1) + ": ");
            coordinates[i][0] = scanner.nextInt(); // x-coordinate
            coordinates[i][1] = scanner.nextInt(); // y-coordinate
        }

        double perimeter = calculateRectanglePerimeter(coordinates);
        System.out.println("Perimeter of the rectangle: " + perimeter);

        scanner.close();
    }

    public static double calculateDistance(int[] point1, int[] point2) {
        int deltaX = point1[0] - point2[0];
        int deltaY = point1[1] - point2[1];
        return Math.sqrt(deltaX * deltaX + deltaY * deltaY);
    }

    public static double calculateRectanglePerimeter(int[][] coordinates) {
        double side1 = calculateDistance(coordinates[0], coordinates[1]);
        double side2 = calculateDistance(coordinates[1], coordinates[2]);
        double side3 = calculateDistance(coordinates[2], coordinates[3]);
        double side4 = calculateDistance(coordinates[3], coordinates[0]);
        
        return side1 + side2 + side3 + side4;
    }
}
