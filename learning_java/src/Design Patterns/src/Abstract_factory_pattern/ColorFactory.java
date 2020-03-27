package Abstract_factory_pattern;

public class ColorFactory  extends AbstractFactory 
{	
	@Override
	Shape getShape(String shape) {
		// TODO Auto-generated method stub
		return null;
	}
	@Override
	Color getColor(String color) {
		if (color == null) {
			return null;
		}
		if (color.equalsIgnoreCase("RED")) {
			return new C_Red();
		}
		else if (color.equalsIgnoreCase("GREEN")) {
			return new C_Green();
		}
		else if (color.equalsIgnoreCase("BLUE")) {
			return new C_Blue();
		}
		return null;
	}
}
