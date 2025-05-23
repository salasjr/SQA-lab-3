import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class RectangleCalculatorTest {
    private RectangleCalculator calculator;

    @Before
    public void setUp() {
        calculator = new RectangleCalculator();
    }

    @Test
    public void testCalculateArea() {
        assertEquals(15.0, calculator.calculateArea(5.0, 3.0), 0.001);
        
        assertEquals(16.0, calculator.calculateArea(4.0, 4.0), 0.001);
        
        assertEquals(0.0, calculator.calculateArea(0.0, 5.0), 0.001);
        
        assertEquals(-6.0, calculator.calculateArea(-2.0, 3.0), 0.001);
    }

    @Test
    public void testCalculatePerimeter() {
        
        assertEquals(16.0, calculator.calculatePerimeter(5.0, 3.0), 0.001);
        
        assertEquals(16.0, calculator.calculatePerimeter(4.0, 4.0), 0.001);
        
        assertEquals(10.0, calculator.calculatePerimeter(0.0, 5.0), 0.001);
        
        assertEquals(2.0, calculator.calculatePerimeter(-2.0, 3.0), 0.001);
    }

    @Test
    public void testIsSquare() {
        assertTrue(calculator.isSquare(4.0, 4.0));
        
        assertFalse(calculator.isSquare(5.0, 3.0));
        
        assertTrue(calculator.isSquare(0.0, 0.0));
        
        assertTrue(calculator.isSquare(-2.0, -2.0));
    }

    @Test
    public void testCalculateDiagonal() {
        assertEquals(5.831, calculator.calculateDiagonal(5.0, 3.0), 0.001);
        
        assertEquals(5.657, calculator.calculateDiagonal(4.0, 4.0), 0.001);
        
        assertEquals(5.0, calculator.calculateDiagonal(0.0, 5.0), 0.001);
        
        assertEquals(3.606, calculator.calculateDiagonal(-2.0, 3.0), 0.001);
    }

    @Test
    public void testEdgeCases() {
        assertEquals(1.0E20, calculator.calculateArea(1.0E10, 1.0E10), 0.001);
        
        assertEquals(1.0E-20, calculator.calculateArea(1.0E-10, 1.0E-10), 0.001);
        
        assertTrue(calculator.isSquare(1.0E10, 1.0E10));
        assertTrue(calculator.isSquare(1.0E-10, 1.0E-10));
    }
} 