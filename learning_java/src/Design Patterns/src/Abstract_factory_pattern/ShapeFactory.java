package Abstract_factory_pattern;

public class ShapeFactory extends AbstractFactory{

	public ShapeFactory() {
		// TODO Auto-generated constructor stub
	}
	@Override
	public Color getColor(String color) {
		// TODO Auto-generated method stub
		return null;
	}
	@Override
	public Shape getShape(String shape) {
		// TODO Auto-generated method stub
		if (shape == null) {
			return null;
		}
		if (shape.equalsIgnoreCase("CIRCLE")) {
			return new S_Circle();
		}
		else if (shape.equalsIgnoreCase("SQUARE")) {
			return new S_Square();
		}
		else if (shape.equalsIgnoreCase("RECTANGLE")) {
			return new S_Rectangle();
		}
		
		return null;
	}
	
	
	
}
