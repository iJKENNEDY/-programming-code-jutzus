package patron_fachada;

public class FacadePatternDemo {
	
	public static void main(String[] args) {
		
		ShapeMaker shapeMarker  = new ShapeMaker();
		shapeMarker.drawCircle();
		shapeMarker.drawRectangle();
		shapeMarker.drawSquare();
	}
}
