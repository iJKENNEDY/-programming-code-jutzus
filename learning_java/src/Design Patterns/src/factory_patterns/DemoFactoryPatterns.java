package factory_patterns;

public class DemoFactoryPatterns {
	
	public static void main(String[] args) {
		ShapeFactory shapeFactory = new ShapeFactory();
		
		Shape shape1 = shapeFactory.getShape("CIRCLE");
		
		shape1.draw();
		
		Shape shape2 = shapeFactory.getShape("Square");
		shape2.draw();
		
		Shape shape3 = shapeFactory.getShape("RECTANGLE");
		shape3.draw();
		
		//Shape shapeNull = shapeFactory.getShape(null);
		//shapeNull.draw();
	}
}
