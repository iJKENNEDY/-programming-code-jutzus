package Singleton_;

public class SingleObject {
	
	private static SingleObject instance = new SingleObject();	
	private SingleObject() {
		// TODO Auto-generated constructor stub
	}
	public static SingleObject getInstance() {
		return instance;
	}
	public void showMessage() {
		System.out.println("patrin singleton");
	}
	
}
