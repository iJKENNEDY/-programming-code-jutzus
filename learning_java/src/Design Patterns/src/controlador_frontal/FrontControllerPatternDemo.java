package controlador_frontal;

public class FrontControllerPatternDemo {
	public static void main(String[] args) {
		
		FrontController froncontr = new FrontController();
		froncontr.dispatchRequest("HOME");
		froncontr.dispatchRequest("STUDENT");
	}
}
