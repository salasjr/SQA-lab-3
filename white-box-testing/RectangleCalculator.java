public class RectangleCalculator {
    /**
     * Calculates the area of a rectangle.
     * @param length The length of the rectangle
     * @param width The width of the rectangle
     * @return The area of the rectangle
     */
    public double calculateArea(double length, double width) {
        return length * width;
    }

    /**
     * Calculates the perimeter of a rectangle.
     * @param length The length of the rectangle
     * @param width The width of the rectangle
     * @return The perimeter of the rectangle
     */
    public double calculatePerimeter(double length, double width) {
        return 2 * (length + width);
    }

    /**
     * Determines if a rectangle is a square.
     * @param length The length of the rectangle
     * @param width The width of the rectangle
     * @return true if the rectangle is a square, false otherwise
     */
    public boolean isSquare(double length, double width) {
        return length == width;
    }

    /**
     * Calculates the diagonal of a rectangle.
     * @param length The length of the rectangle
     * @param width The width of the rectangle
     * @return The length of the diagonal
     */
    public double calculateDiagonal(double length, double width) {
        return Math.sqrt(length * length + width * width);
    }
} 