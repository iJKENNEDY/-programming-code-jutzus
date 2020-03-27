package patron_decorador;

public abstract class ShapeDecorator implements Shape{
	
	protected Shape decoratedShape;
	
	public ShapeDecorator(Shape decoratedShape) {
		// TODO Auto-generated constructor stub
		this.decoratedShape  = decoratedShape;
	}
	
	public void draw() {
		// TODO Auto-generated method stub
		decoratedShape.draw();
	}
}
