package Abstract_factory_pattern;

public abstract class AbstractFactory {
	
	abstract Shape getShape(String shape);
	
	abstract Color getColor(String color);
}
