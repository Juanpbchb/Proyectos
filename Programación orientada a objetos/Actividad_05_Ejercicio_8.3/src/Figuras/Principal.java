package Figuras;

/**
 * Esta clase define el punto de ingreso al programa de figuras
 * geometricas. Por lo tanto, cuenta con un metodo main de acceso al
 * programa.
 * @version 1.2/2020
 */
public class Principal {
    /**
     * Metodo main que sirve de punto de entrada al programa
     */
    public static void main(String[] args) {
        VentanaPrincipal miVentanaPrincipal; // Define la ventana principal
        miVentanaPrincipal = new VentanaPrincipal(); // Crea la ventana principal
        miVentanaPrincipal.setVisible(true); // Establece la ventana como visible
        // Establece que la ventana no puede cambiar su tamaño
        miVentanaPrincipal.setResizable(false);
    }
}
